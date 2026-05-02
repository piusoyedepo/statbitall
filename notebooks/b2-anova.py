# Statbitall: ANOVA is not just multiple t-tests (and here's why)
# statbitall.com/blog/anova-explained

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)

# Three checkout variants with different conversion rates
n_per_group = 100
group_a = rng.normal(loc=8.0, scale=3.0, size=n_per_group)
group_b = rng.normal(loc=10.0, scale=3.0, size=n_per_group)
group_c = rng.normal(loc=12.0, scale=3.0, size=n_per_group)

# One-way ANOVA
f_stat, p_value = stats.f_oneway(group_a, group_b, group_c)
print(f"F-statistic: {f_stat:.3f}")
print(f"p-value:     {p_value:.6f}")

# Manual decomposition to show the math
all_data = np.concatenate([group_a, group_b, group_c])
grand_mean = all_data.mean()
groups = [group_a, group_b, group_c]
k = len(groups)
N = len(all_data)

ss_between = sum(len(g) * (g.mean() - grand_mean)**2 for g in groups)
ss_within = sum(((g - g.mean())**2).sum() for g in groups)
ss_total = ((all_data - grand_mean)**2).sum()

ms_between = ss_between / (k - 1)
ms_within = ss_within / (N - k)
f_manual = ms_between / ms_within

print(f"\nManual decomposition:")
print(f"SS_between: {ss_between:.2f}  (df={k-1})")
print(f"SS_within:  {ss_within:.2f}  (df={N-k})")
print(f"SS_total:   {ss_total:.2f}  (df={N-1})")
print(f"F = {ms_between:.2f} / {ms_within:.2f} = {f_manual:.3f}")

# Post-hoc pairwise comparisons
from itertools import combinations
pairs = list(combinations(['A', 'B', 'C'], 2))
group_dict = {'A': group_a, 'B': group_b, 'C': group_c}

print(f"\nPairwise t-tests (no correction):")
for g1, g2 in pairs:
    t, p = stats.ttest_ind(group_dict[g1], group_dict[g2])
    sig = "significant" if p < 0.05 else "not significant"
    print(f"  {g1} vs {g2}: p={p:.4f} ({sig})")

# Show the multiple comparison problem
n_tests = 3
alpha = 0.05
family_wise = 1 - (1 - alpha) ** n_tests
print(f"\nWith {n_tests} tests at alpha={alpha}:")
print(f"Family-wise error rate: {family_wise:.3f} (not {alpha})")
print(f"Bonferroni correction:  alpha per test = {alpha/n_tests:.4f}")
