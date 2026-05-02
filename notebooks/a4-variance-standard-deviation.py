# Statbitall: Variance is risk. Standard deviation is the language of risk.
# statbitall.com/blog/variance-and-standard-deviation

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# --- Panel 1: Same mean, different variance ---
fund_a = rng.normal(loc=8, scale=2, size=100)    # low volatility
fund_b = rng.normal(loc=8, scale=12, size=100)   # high volatility

axes[0].hist(fund_a, bins=20, alpha=0.6, label=f"Fund A (sd={fund_a.std():.1f})", color="steelblue")
axes[0].hist(fund_b, bins=20, alpha=0.6, label=f"Fund B (sd={fund_b.std():.1f})", color="coral")
axes[0].axvline(x=8, color="black", linestyle="--", label="Mean = 8%")
axes[0].set_xlabel("Annual return (%)")
axes[0].set_title("Same mean, different risk")
axes[0].legend(fontsize=8)

# --- Panel 2: Standard deviation vs standard error ---
population = rng.normal(loc=50, scale=15, size=100_000)
sample_sizes = [10, 25, 50, 100, 250, 500, 1000]
sds = []
ses = []

for n in sample_sizes:
    sample = rng.choice(population, size=n)
    sds.append(sample.std(ddof=1))
    ses.append(sample.std(ddof=1) / np.sqrt(n))

axes[1].plot(sample_sizes, sds, 'o-', color="steelblue", label="Std Dev (s)")
axes[1].plot(sample_sizes, ses, 's-', color="coral", label="Std Error (SE)")
axes[1].set_xlabel("Sample size")
axes[1].set_ylabel("Value")
axes[1].set_title("SD stays flat, SE shrinks with n")
axes[1].legend(fontsize=8)
axes[1].set_xscale("log")

# --- Panel 3: Bessel's correction matters for small n ---
true_var = 15**2  # population variance = 225
sample_sizes_small = [3, 5, 10, 20, 50, 100, 500]
bias_n = []     # dividing by n
bias_n1 = []    # dividing by n-1

for n in sample_sizes_small:
    vars_n = []
    vars_n1 = []
    for _ in range(5000):
        sample = rng.normal(loc=50, scale=15, size=n)
        vars_n.append(sample.var(ddof=0))    # divide by n
        vars_n1.append(sample.var(ddof=1))   # divide by n-1
    bias_n.append(np.mean(vars_n) - true_var)
    bias_n1.append(np.mean(vars_n1) - true_var)

axes[2].plot(sample_sizes_small, bias_n, 'o-', color="coral", label="Divide by n (biased)")
axes[2].plot(sample_sizes_small, bias_n1, 's-', color="seagreen", label="Divide by n-1 (unbiased)")
axes[2].axhline(y=0, color="black", linestyle="--")
axes[2].set_xlabel("Sample size")
axes[2].set_ylabel("Average bias")
axes[2].set_title("Bessel's correction matters for small n")
axes[2].legend(fontsize=8)

plt.tight_layout()
plt.savefig("variance_demo.png", dpi=150)
plt.show()

# Print the key distinction
sample = rng.normal(loc=50, scale=15, size=100)
print(f"Sample std dev (s):    {sample.std(ddof=1):.2f}  -- describes the data")
print(f"Standard error (SE):   {sample.std(ddof=1)/np.sqrt(100):.2f}  -- describes estimate precision")
