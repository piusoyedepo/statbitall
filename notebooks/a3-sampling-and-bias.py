# Statbitall: Your sample is lying to you (and how to catch it)
# statbitall.com/blog/sampling-and-bias

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# True population: income is right-skewed (log-normal)
population_size = 100_000
population = rng.lognormal(mean=10.5, sigma=0.8, size=population_size)
true_mean = population.mean()

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# --- Panel 1: Sample size vs precision ---
sample_sizes = [10, 50, 100, 500, 1000, 5000]
n_repeats = 1000
means_by_size = {}

for n in sample_sizes:
    sample_means = [rng.choice(population, size=n).mean() for _ in range(n_repeats)]
    means_by_size[n] = sample_means

axes[0].boxplot(
    [means_by_size[n] for n in sample_sizes],
    labels=[str(n) for n in sample_sizes]
)
axes[0].axhline(y=true_mean, color="red", linestyle="--", label=f"True mean: {true_mean:,.0f}")
axes[0].set_xlabel("Sample size")
axes[0].set_ylabel("Sample mean")
axes[0].set_title("Precision improves with sample size")
axes[0].legend(fontsize=8)

# --- Panel 2: Bias from non-random sampling ---
# Biased sample: only top 30% of incomes (like surveying luxury shoppers)
biased_pool = population[population > np.percentile(population, 70)]
biased_means = [rng.choice(biased_pool, size=1000).mean() for _ in range(n_repeats)]
random_means = [rng.choice(population, size=1000).mean() for _ in range(n_repeats)]

axes[1].hist(random_means, bins=30, alpha=0.6, label="Random sample", color="steelblue")
axes[1].hist(biased_means, bins=30, alpha=0.6, label="Biased sample", color="coral")
axes[1].axvline(x=true_mean, color="red", linestyle="--", label=f"True mean")
axes[1].set_xlabel("Sample mean")
axes[1].set_title("Bias vs random (both n=1000)")
axes[1].legend(fontsize=8)

# --- Panel 3: Stratified vs simple random ---
# Create 3 income strata
low = population[population < np.percentile(population, 33)]
mid = population[(population >= np.percentile(population, 33)) &
                 (population < np.percentile(population, 66))]
high = population[population >= np.percentile(population, 66)]

n_total = 300
simple_means = []
strat_means = []

for _ in range(n_repeats):
    # Simple random sample
    simple = rng.choice(population, size=n_total)
    simple_means.append(simple.mean())

    # Stratified: 100 from each stratum, weighted by stratum proportion
    s_low = rng.choice(low, size=100)
    s_mid = rng.choice(mid, size=100)
    s_high = rng.choice(high, size=100)
    w_low = len(low) / population_size
    w_mid = len(mid) / population_size
    w_high = len(high) / population_size
    strat_mean = w_low * s_low.mean() + w_mid * s_mid.mean() + w_high * s_high.mean()
    strat_means.append(strat_mean)

axes[2].hist(simple_means, bins=30, alpha=0.6, label="Simple random", color="steelblue")
axes[2].hist(strat_means, bins=30, alpha=0.6, label="Stratified", color="seagreen")
axes[2].axvline(x=true_mean, color="red", linestyle="--")
axes[2].set_xlabel("Sample mean")
axes[2].set_title("Stratified reduces variance (n=300)")
axes[2].legend(fontsize=8)

plt.tight_layout()
plt.savefig("sampling_demo.png", dpi=150)
plt.show()

print(f"True population mean: {true_mean:,.0f}")
print(f"Simple random SE:     {np.std(simple_means):,.0f}")
print(f"Stratified SE:        {np.std(strat_means):,.0f}")
