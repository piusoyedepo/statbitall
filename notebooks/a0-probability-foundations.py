# Statbitall: Probability is not about luck. It's about measuring what you don't know.
# statbitall.com/blog/probability-theory-foundations

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# --- Law of Large Numbers ---
# Flip a fair coin n times, track running proportion of heads
n_flips = 10_000
flips = rng.binomial(1, 0.5, n_flips)
running_proportion = np.cumsum(flips) / np.arange(1, n_flips + 1)

axes[0].plot(running_proportion, color="steelblue", linewidth=1)
axes[0].axhline(y=0.5, color="black", linestyle="--", linewidth=1.5,
                label="True P(heads) = 0.5")
axes[0].set_xlabel("Number of flips")
axes[0].set_ylabel("Proportion of heads")
axes[0].set_title("Law of Large Numbers")
axes[0].set_xscale("log")
axes[0].legend()
axes[0].set_ylim(0.3, 0.7)

# --- Conditional Probability ---
# Simulate 10,000 website visitors: device type and purchase behavior
n_visitors = 10_000
is_mobile = rng.binomial(1, 0.4, n_visitors)

# Mobile users purchase at 5%, desktop at 8%
purchase_prob = np.where(is_mobile, 0.05, 0.08)
purchased = rng.binomial(1, purchase_prob)

# Compute conditional probabilities from simulated data
mobile_rate = purchased[is_mobile == 1].mean()
desktop_rate = purchased[is_mobile == 0].mean()

axes[1].bar(["Mobile", "Desktop"], [mobile_rate, desktop_rate],
            color=["steelblue", "coral"], width=0.5)
axes[1].set_ylabel("P(Purchase | Device)")
axes[1].set_title("Conditional Probability")
axes[1].set_ylim(0, 0.12)
for i, rate in enumerate([mobile_rate, desktop_rate]):
    axes[1].text(i, rate + 0.003, f"{rate:.3f}", ha="center", fontweight="bold")

# --- Expected Value: Dice Rolls ---
# Roll a die many times, track cumulative average vs E[X] = 3.5
n_rolls = 5_000
rolls = rng.integers(1, 7, n_rolls)
cumulative_avg = np.cumsum(rolls) / np.arange(1, n_rolls + 1)

axes[2].plot(cumulative_avg, color="steelblue", linewidth=1)
axes[2].axhline(y=3.5, color="black", linestyle="--", linewidth=1.5,
                label="E[X] = 3.5")
axes[2].set_xlabel("Number of rolls")
axes[2].set_ylabel("Cumulative average")
axes[2].set_title("Expected Value (Fair Die)")
axes[2].legend()
axes[2].set_ylim(2.5, 4.5)

plt.tight_layout()
plt.savefig("probability_foundations.png", dpi=150)
plt.show()
