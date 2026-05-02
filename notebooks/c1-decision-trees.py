# Statbitall: Decision trees learn by asking the right questions
# statbitall.com/blog/decision-trees-explained

import numpy as np
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split

rng = np.random.default_rng(42)

# Create a dataset with 2 informative features and 1 noisy one
X, y = make_classification(
    n_samples=500,
    n_features=3,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Unpruned tree (will overfit)
tree_deep = DecisionTreeClassifier(random_state=42)
tree_deep.fit(X_train, y_train)
print(f"Unpruned depth:    {tree_deep.get_depth()}")
print(f"Unpruned train acc: {tree_deep.score(X_train, y_train):.3f}")
print(f"Unpruned test acc:  {tree_deep.score(X_test, y_test):.3f}")

# Pruned tree (controlled complexity)
tree_pruned = DecisionTreeClassifier(
    max_depth=4,
    min_samples_leaf=10,
    random_state=42
)
tree_pruned.fit(X_train, y_train)
print(f"\nPruned depth:      {tree_pruned.get_depth()}")
print(f"Pruned train acc:   {tree_pruned.score(X_train, y_train):.3f}")
print(f"Pruned test acc:    {tree_pruned.score(X_test, y_test):.3f}")

# Print the pruned tree's rules
print("\nDecision rules:")
print(export_text(tree_pruned, feature_names=["feat_0", "feat_1", "noise"]))
