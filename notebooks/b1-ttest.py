# Statbitall: The t-test: what it's really asking
# statbitall.com/blog/t-test-explained

import numpy as np
from scipy import stats

rng = np.random.default_rng(42)

# Simulate an A/B test: control vs. treatment
# Treatment has higher mean AND higher variance
control = rng.normal(loc=10.0, scale=2.0, size=50)
treatment = rng.normal(loc=11.2, scale=4.0, size=50)

# Standard t-test (assumes equal variance)
t_equal, p_equal = stats.ttest_ind(control, treatment, equal_var=True)
print(f"Equal-variance t-test:  t = {t_equal:.3f}, p = {p_equal:.4f}")

# Welch's t-test (does NOT assume equal variance)
t_welch, p_welch = stats.ttest_ind(control, treatment, equal_var=False)
print(f"Welch's t-test:         t = {t_welch:.3f}, p = {p_welch:.4f}")

# Check the variance ratio
print(f"\nVariance ratio: {treatment.var() / control.var():.2f}")
print(f"Control std:    {control.std():.2f}")
print(f"Treatment std:  {treatment.std():.2f}")
