# Statbitall: Hypothesis testing from scratch: the logic before the formula
# statbitall.com/blog/b0-hypothesis-testing-logic

import numpy as np
from scipy.stats import t as t_dist

# Scenario: did daily active users change after a product update?
# Null hypothesis: mean DAU = 1000 (no change)
np.random.seed(42)
n = 40
sample = np.random.normal(loc=1045, scale=120, size=n)  # true effect: +45 users

# Pre-specified before data collection
mu_0 = 1000
alpha = 0.05

# Compute test statistic
x_bar = np.mean(sample)
s = np.std(sample, ddof=1)   # sample std dev (ddof=1 corrects for bias)
se = s / np.sqrt(n)           # standard error of the mean
t_stat = (x_bar - mu_0) / se

# p-value: two-tailed test
df = n - 1
p_value = 2 * t_dist.sf(np.abs(t_stat), df=df)

print(f"Sample mean:    {x_bar:.2f}")
print(f"Test statistic: t = {t_stat:.4f}")
print(f"p-value:        {p_value:.4f}")
print(f"Decision:       {'Reject H0' if p_value < alpha else 'Fail to reject H0'}")
