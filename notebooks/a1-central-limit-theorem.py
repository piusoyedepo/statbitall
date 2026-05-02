# Statbitall: The central limit theorem is why statistics works
# statbitall.com/blog/central-limit-theorem

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

# Population: exponential distribution (skewed right, mean = 1)
population = rng.exponential(scale=1.0, size=100_000)

sample_sizes = [5, 30, 100]
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

for ax, n in zip(axes, sample_sizes):
    # Draw 5000 samples of size n, compute the mean of each
    sample_means = [
        rng.choice(population, size=n).mean()
        for _ in range(5_000)
    ]
    ax.hist(sample_means, bins=60, density=True, color='#1B9E77', alpha=0.8)
    ax.set_title(f'n = {n}', fontsize=12)
    ax.set_xlabel('Sample mean')
    ax.set_ylabel('Density')

plt.suptitle(
    'CLT: sample means from an exponential population',
    y=1.02, fontsize=13
)
plt.tight_layout()
plt.show()
