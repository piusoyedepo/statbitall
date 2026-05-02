# Statbitall: A/B testing under the hood: what the platform isn't telling you
# statbitall.com/blog/ab-testing-explained

import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

def required_sample_size(p_baseline, mde, alpha=0.05, power=0.80):
    p_treatment = p_baseline + mde
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)
    var_baseline = p_baseline * (1 - p_baseline)
    var_treatment = p_treatment * (1 - p_treatment)
    n = (z_alpha + z_beta)**2 * (var_baseline + var_treatment) / mde**2
    return int(np.ceil(n))

def run_ab_test(n_a, n_b, conv_a, conv_b, alpha=0.05):
    p_a = conv_a / n_a
    p_b = conv_b / n_b
    p_pooled = (conv_a + conv_b) / (n_a + n_b)
    se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n_a + 1/n_b))
    z = (p_b - p_a) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))
    return p_a, p_b, z, p_value

# --- Step 1: Calculate required sample size ---
p_baseline = 0.10
mde = 0.02
n_required = required_sample_size(p_baseline, mde)
print(f"Required sample size: {n_required:,} per variant")
print(f"Total experiment size: {2*n_required:,} users")

# --- Step 2: Simulate peeking vs fixed sample ---
n_total = n_required
daily_users = 100
false_positives_peeking = 0
false_positives_fixed = 0
n_simulations = 1000

for _ in range(n_simulations):
    # Null is TRUE: both groups have same conversion rate
    conv_a = rng.binomial(1, p_baseline, n_total)
    conv_b = rng.binomial(1, p_baseline, n_total)

    # Fixed sample: test once at the end
    _, _, _, p_fixed = run_ab_test(
        n_total, n_total, conv_a.sum(), conv_b.sum()
    )
    if p_fixed < 0.05:
        false_positives_fixed += 1

    # Peeking: test at every 100-user increment
    declared = False
    for day in range(1, n_total // daily_users + 1):
        n_so_far = day * daily_users
        _, _, _, p_peek = run_ab_test(
            n_so_far, n_so_far,
            conv_a[:n_so_far].sum(), conv_b[:n_so_far].sum()
        )
        if p_peek < 0.05:
            declared = True
            break
    if declared:
        false_positives_peeking += 1

print(f"\nSimulation results ({n_simulations} experiments, null TRUE):")
print(f"  Fixed sample FPR: {false_positives_fixed/n_simulations:.3f} (target 0.05)")
print(f"  Peeking FPR:      {false_positives_peeking/n_simulations:.3f} (inflated)")

# --- Step 3: Multiple metrics ---
n_metrics = 8
alpha_bonferroni = 0.05 / n_metrics
fwer_uncorrected = 1 - (0.95 ** n_metrics)
print(f"\nWith {n_metrics} metrics at alpha=0.05:")
print(f"  Family-wise error rate: {fwer_uncorrected:.3f}")
print(f"  Bonferroni threshold: {alpha_bonferroni:.4f} per metric")
