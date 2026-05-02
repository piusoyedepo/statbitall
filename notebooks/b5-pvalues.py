# Statbitall: p-values are not what you were taught
# statbitall.com/blog/pvalues-explained

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# --- Panel 1: p-value as tail area ---
x = np.linspace(-4, 4, 300)
null_dist = stats.norm.pdf(x)
observed = 2.1
p_val = 2 * (1 - stats.norm.cdf(abs(observed)))

axes[0].plot(x, null_dist, color='#0B1D3A', linewidth=2)
axes[0].fill_between(x, null_dist, where=(x >= abs(observed)),
                     color='#D85A30', alpha=0.7, label=f'p-value = {p_val:.3f}')
axes[0].fill_between(x, null_dist, where=(x <= -abs(observed)),
                     color='#D85A30', alpha=0.7)
axes[0].axvline(x=observed, color='#D85A30', linestyle='--', linewidth=1.5)
axes[0].axvline(x=-observed, color='#D85A30', linestyle='--', linewidth=1.5)
axes[0].set_title('p-value as tail probability under H0')
axes[0].set_xlabel('Test statistic')
axes[0].set_ylabel('Density')
axes[0].legend(fontsize=9)

# --- Panel 2: p-hacking simulation ---
n_experiments = 1000
n_per_experiment = 30
p_values_null = []

for _ in range(n_experiments):
    group_a = rng.normal(0, 1, n_per_experiment)
    group_b = rng.normal(0, 1, n_per_experiment)  # same distribution
    _, p = stats.ttest_ind(group_a, group_b)
    p_values_null.append(p)

p_values_null = np.array(p_values_null)
false_positive_rate = (p_values_null < 0.05).mean()

axes[1].hist(p_values_null, bins=20, density=True, alpha=0.7, color='#1B9E77')
axes[1].axvline(x=0.05, color='#D85A30', linestyle='--', linewidth=2,
                label=f'alpha = 0.05 ({false_positive_rate:.1%} false positives)')
axes[1].set_title('p-values when H0 is TRUE\n(1000 experiments)')
axes[1].set_xlabel('p-value')
axes[1].set_ylabel('Density')
axes[1].legend(fontsize=9)

# --- Panel 3: Multiple testing inflation ---
m_tests = range(1, 101)
fpr = [1 - (0.95 ** m) for m in m_tests]

axes[2].plot(list(m_tests), fpr, color='#0B1D3A', linewidth=2)
axes[2].axhline(y=0.05, color='#D85A30', linestyle='--', linewidth=1.5,
                label='5% target rate')
axes[2].axhline(y=0.64, color='#2A5BA0', linestyle=':', linewidth=1.5,
                label='64% at m=20 tests')
axes[2].axvline(x=20, color='#2A5BA0', linestyle=':', linewidth=1.5)
axes[2].set_title('False positive rate vs number of tests')
axes[2].set_xlabel('Number of tests (m)')
axes[2].set_ylabel('P(at least one false positive)')
axes[2].legend(fontsize=8)
axes[2].set_ylim(0, 1)

plt.tight_layout()
plt.savefig('pvalue_demo.png', dpi=150, bbox_inches='tight')
plt.show()

# Demonstrate p-hacking
print("Simulating p-hacking (peeking at results):")
group_a = rng.normal(0, 1, 100)
group_b = rng.normal(0, 1, 100)  # truly null effect

for n in range(10, 101, 5):
    _, p = stats.ttest_ind(group_a[:n], group_b[:n])
    if p < 0.05:
        print(f"  Stopped at n={n}: p={p:.4f} (FALSE POSITIVE)")
        break
