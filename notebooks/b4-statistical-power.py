# Statbitall: Statistical power is why your A/B test found nothing
# statbitall.com/blog/statistical-power-explained

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)

# --- Sample size calculation ---
def required_n(alpha, power, delta, sigma):
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    z_beta = stats.norm.ppf(power)
    return int(np.ceil(2 * (z_alpha + z_beta)**2 * sigma**2 / delta**2))

# Business scenario: conversion rate baseline = 10%, detect 2% lift
baseline = 0.10
sigma = np.sqrt(baseline * (1 - baseline))
delta = 0.02

n_80 = required_n(alpha=0.05, power=0.80, delta=delta, sigma=sigma)
n_90 = required_n(alpha=0.05, power=0.90, delta=delta, sigma=sigma)
n_95 = required_n(alpha=0.05, power=0.95, delta=delta, sigma=sigma)

print(f"To detect a {delta:.0%} lift from {baseline:.0%} baseline:")
print(f"  80% power: {n_80:,} per group ({2*n_80:,} total)")
print(f"  90% power: {n_90:,} per group ({2*n_90:,} total)")
print(f"  95% power: {n_95:,} per group ({2*n_95:,} total)")

# --- Power curves ---
sample_sizes = np.arange(10, 500, 5)
for d, label in [(0.2, 'Small (d=0.2)'),
                  (0.5, 'Medium (d=0.5)'),
                  (0.8, 'Large (d=0.8)')]:
    powers = []
    for n in sample_sizes:
        nc = d * np.sqrt(n / 2)
        power = 1 - stats.norm.cdf(1.96 - nc) + stats.norm.cdf(-1.96 - nc)
        powers.append(power)
    print(f"{label}: needs n={sample_sizes[next(i for i,p in enumerate(powers) if p >= 0.8)]} for 80% power")
