# Statbitall: Probability distributions are just rules for uncertainty
# statbitall.com/blog/probability-distributions-explained

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Normal: symmetric, bell-shaped
normal_data = rng.normal(loc=50, scale=10, size=5000)
axes[0, 0].hist(normal_data, bins=50, density=True, alpha=0.7, color='steelblue')
x = np.linspace(10, 90, 200)
axes[0, 0].plot(x, stats.norm.pdf(x, 50, 10), 'k-', lw=2)
axes[0, 0].set_title('Normal (mu=50, sigma=10)')

# Binomial: discrete counts of successes
binom_data = rng.binomial(n=20, p=0.3, size=5000)
values, counts = np.unique(binom_data, return_counts=True)
axes[0, 1].bar(values, counts / counts.sum(), alpha=0.7, color='coral')
axes[0, 1].set_title('Binomial (n=20, p=0.3)')

# Poisson: count of rare events
poisson_data = rng.poisson(lam=4, size=5000)
values, counts = np.unique(poisson_data, return_counts=True)
axes[1, 0].bar(values, counts / counts.sum(), alpha=0.7, color='seagreen')
axes[1, 0].set_title('Poisson (lambda=4)')

# Exponential: time between events
exp_data = rng.exponential(scale=5, size=5000)
axes[1, 1].hist(exp_data, bins=50, density=True, alpha=0.7, color='goldenrod')
x = np.linspace(0, 30, 200)
axes[1, 1].plot(x, stats.expon.pdf(x, scale=5), 'k-', lw=2)
axes[1, 1].set_title('Exponential (mean=5)')

plt.tight_layout()
plt.savefig('distributions.png', dpi=150)
plt.show()

# Test: does this data look normal?
sample = rng.exponential(scale=5, size=100)
stat, p_value = stats.shapiro(sample)
print(f"Shapiro-Wilk test: stat={stat:.4f}, p={p_value:.4f}")
print(f"Conclusion: {'Looks normal' if p_value > 0.05 else 'Not normal'}")
