# Statbitall: Chi-square tests: how to make decisions from categories
# statbitall.com/blog/chisquare-explained

import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

# --- Goodness of fit: equal traffic across pages? ---
observed_traffic = np.array([245, 198, 312, 245])
n_total = observed_traffic.sum()
expected_equal = np.full(4, n_total / 4)

chi2_gof, p_gof = stats.chisquare(observed_traffic, expected_equal)
print("Goodness-of-fit test (equal traffic across 4 pages):")
print(f"  Observed: {observed_traffic}")
print(f"  Expected: {expected_equal}")
print(f"  chi2 = {chi2_gof:.3f}, p = {p_gof:.4f}")

# --- Test of independence: customer segment vs purchase ---
# Rows: New customers, Returning customers
# Columns: Purchased, Did not purchase
contingency = np.array([
    [142, 358],
    [231, 269]
])

chi2_ind, p_ind, dof, expected_ind = stats.chi2_contingency(contingency)
print(f"\nTest of independence (segment vs purchase):")
print(f"  Observed:\n{contingency}")
print(f"  Expected:\n{expected_ind.astype(int)}")
print(f"  chi2 = {chi2_ind:.3f}, p = {p_ind:.4f}, df = {dof}")

# Cramer's V: effect size for chi-square
n = contingency.sum()
cramers_v = np.sqrt(chi2_ind / (n * (min(contingency.shape) - 1)))
print(f"  Cramer's V = {cramers_v:.3f}")

# Manual verification
chi2_manual = 0
for i in range(2):
    for j in range(2):
        chi2_manual += (contingency[i,j] - expected_ind[i,j])**2 / expected_ind[i,j]
print(f"\nManual chi2 = {chi2_manual:.3f} (matches scipy: {np.isclose(chi2_manual, chi2_ind)})")
