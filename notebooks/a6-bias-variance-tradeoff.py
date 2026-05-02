# Statbitall: The bias-variance tradeoff controls every model you'll ever build
# statbitall.com/blog/bias-variance-tradeoff

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

rng = np.random.default_rng(42)

# True function: a gentle curve
def true_function(x):
    return np.sin(2 * x) + 0.5 * x

# Generate multiple training sets to measure bias and variance
n_datasets = 200
n_train = 30
n_test = 100
x_test = np.linspace(0, 5, n_test).reshape(-1, 1)
y_true = true_function(x_test.ravel())

degrees = [1, 3, 5, 10, 15]
fig, axes = plt.subplots(2, 3, figsize=(15, 9))

# Top row: show fits for three complexity levels
for idx, degree in enumerate([1, 5, 15]):
    ax = axes[0, idx]
    ax.plot(x_test, y_true, 'k-', linewidth=2, label="True function")

    for i in range(20):  # show 20 fits
        x_train = rng.uniform(0, 5, n_train).reshape(-1, 1)
        y_train = true_function(x_train.ravel()) + rng.normal(0, 0.5, n_train)
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        ax.plot(x_test, y_pred, alpha=0.15, color="steelblue")

    ax.set_title(f"Degree {degree}")
    ax.set_ylim(-3, 6)
    if idx == 0:
        ax.set_ylabel("y")

# Bottom row: compute bias^2, variance, and MSE across degrees
all_degrees = range(1, 16)
bias_sq_list = []
var_list = []
mse_list = []

for degree in all_degrees:
    predictions = np.zeros((n_datasets, n_test))

    for i in range(n_datasets):
        x_train = rng.uniform(0, 5, n_train).reshape(-1, 1)
        y_train = true_function(x_train.ravel()) + rng.normal(0, 0.5, n_train)
        model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
        model.fit(x_train, y_train)
        predictions[i] = model.predict(x_test).ravel()

    mean_pred = predictions.mean(axis=0)
    bias_sq = np.mean((mean_pred - y_true) ** 2)
    variance = np.mean(predictions.var(axis=0))
    mse = np.mean((predictions - y_true) ** 2)

    bias_sq_list.append(bias_sq)
    var_list.append(variance)
    mse_list.append(mse)

# Plot decomposition
ax = axes[1, 0]
ax.plot(list(all_degrees), bias_sq_list, 'o-', label="Bias²", color="coral")
ax.plot(list(all_degrees), var_list, 's-', label="Variance", color="steelblue")
ax.plot(list(all_degrees), mse_list, '^-', label="MSE (total)", color="black")
ax.axhline(y=0.25, color="gray", linestyle=":", label="Noise (sigma^2=0.25)")
ax.set_xlabel("Polynomial degree")
ax.set_ylabel("Error")
ax.set_title("Bias-variance decomposition")
ax.legend(fontsize=8)

# Hide unused subplots
axes[1, 1].axis("off")
axes[1, 2].axis("off")

plt.tight_layout()
plt.savefig("bias_variance.png", dpi=150)
plt.show()
