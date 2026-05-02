# Statbitall: Confidence intervals don't mean what you think they mean
# statbitall.com/blog/confidence-intervals-explained

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)

# True population
true_mean = 100
true_sd = 15
n = 30

# --- Simulation: what does "95% confidence" really mean? ---
n_intervals = 100
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Generate 100 confidence intervals
captured = 0
for i in range(n_intervals):
    sample = rng.normal(loc=true_mean, scale=true_sd, size=n)
    x_bar = sample.mean()
    se = sample.std(ddof=1) / np.sqrt(n)
    t_crit = stats.t.ppf(0.975, df=n-1)
    ci_low = x_bar - t_crit * se
    ci_high = x_bar + t_crit * se

    contains = ci_low <= true_mean <= ci_high
    if contains:
        captured += 1
    color = "steelblue" if contains else "coral"
    axes[0].plot([ci_low, ci_high], [i, i], color=color, linewidth=1.5)
    axes[0].plot(x_bar, i, 'o', color=color, markersize=3)

axes[0].axvline(x=true_mean, color="black", linestyle="--", linewidth=1.5,
                label=f"True mean = {true_mean}")
axes[0].set_xlabel("Value")
axes[0].set_ylabel("Sample number")
axes[0].set_title(f"100 confidence intervals ({captured} captured the true mean)")
axes[0].legend(fontsize=9)

# --- Effect of sample size on interval width ---
sample_sizes = [10, 20, 50, 100, 250, 500, 1000]
widths = []

for n_size in sample_sizes:
    sample = rng.normal(loc=true_mean, scale=true_sd, size=n_size)
    se = sample.std(ddof=1) / np.sqrt(n_size)
    t_crit = stats.t.ppf(0.975, df=n_size-1)
    width = 2 * t_crit * se
    widths.append(width)

axes[1].plot(sample_sizes, widths, 'o-', color="steelblue", linewidth=2)
axes[1].set_xlabel("Sample size")
axes[1].set_ylabel("95% CI width")
axes[1].set_title("Larger samples produce narrower intervals")
axes[1].set_xscale("log")

plt.tight_layout()
plt.savefig("confidence_intervals.png", dpi=150)
plt.show()

print(f"Intervals containing true mean: {captured}/100")
print(f"CI width at n=30:   {widths[2]:.1f}")
print(f"CI width at n=1000: {widths[-1]:.1f}")
