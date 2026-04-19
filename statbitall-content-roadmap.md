# Statbitall Content Roadmap & Blog Repository

Single source of truth for all content planning, sequencing, and status tracking.

**Core principle:** Posts are organized by module for site navigation, but published in phase order for reader progression. A reader who starts at Phase 1 and works through sequentially will build a complete statistical foundation.

**Status key:** ✅ Published | 🔲 Draft ready | ⬜ Not started

---

## Publishing Sequence (The Reading Order)

This is the order posts should be written and published. Each post assumes the reader has read the ones before it. Posts within a phase can flex in order, but the phases themselves are sequential.

### Phase 1: Foundational Statistics (Posts 1-8)

Nothing else on the site makes sense without these. A reader who finishes Phase 1 can hold their own in any data conversation.

| Post | ID | Title | Module | Status | Prerequisites | Notes |
|------|----|-------|--------|--------|---------------|-------|
| 1 | A0 | Probability is not about luck. It's about measuring what you don't know. | Foundations | ✅ | None | Gateway post. Establishes the Statbitall voice. |
| 1 | A1 | The central limit theorem is why statistics works | Foundations | ✅ | AO | Gateway post. Establishes the Statbitall voice. |
| 2 | A2 | Probability distributions are just rules for uncertainty | Foundations | ✅ | None | Normal, exponential, uniform, Poisson, binomial. What each looks like, when data follows it, how to identify which one you're dealing with. |
| 3 | A3 | Your sample is lying to you (and how to catch it) | Foundations | ✅ | A1, A2 | Random sampling, sampling bias, stratified vs cluster. Connects back to why CLT matters. |
| 4 | A4 | Variance is risk. Standard deviation is the language of risk. | Foundations | ✅| A1, A2 | What each measures, how they differ, when to use which. Standard error callback to CLT ties the series together. |
| 5 | A12 | Conditional probability is the reason most intuitions fail | Foundations | ⬜ | A2 | Base rate fallacy, medical testing, prosecutor's fallacy. Sets up Bayes. |
| 6 | A11 | Bayes' theorem is how you update beliefs with evidence | Foundations | ⬜ | A12 | Required before Bayesian thinking in Phase 2. |
| 7 | A5 | Confidence intervals don't mean what you think they mean | Foundations | ⬜ | A1, A3, A4 | The most misinterpreted concept in applied statistics. Builds on CLT, sampling, and standard error. |
| 8 | A6 | The bias-variance tradeoff controls every model you'll ever build | Foundations | ⬜ | A4 | The foundational tension behind all ML. Hold until just before Phase 3. |

**Suggested next-4 writing order:** A2 → A3 → A4 → A5. Posts A12 and A11 (conditional probability, Bayes) can slot in before A5. A6 (bias-variance) should wait until just before Phase 3 starts.

---

### Phase 2: Statistical Tests and Inference (Posts 9-16)

Now that readers understand distributions, sampling, and uncertainty, they can learn how to test claims and make decisions.

| Post | ID | Title | Module | Status | Prerequisites | Notes |
|------|----|-------|--------|--------|---------------|-------|
| 9 | B0 | Hypothesis testing from scratch: the logic before the formula | Statistical Tests | ⬜ | Phase 1 | Null vs alternative, test statistics, decision rules. No specific test yet, just the framework. |
| 10 | B5 | p-values are not what you were taught | Statistical Tests | ⬜ | B0 | Neyman-Pearson vs Fisher. Why 0.05 is arbitrary. How p-hacking happens. |
| 11 | B1 | The t-test: what it's really asking | Statistical Tests | ✅ | B0, B5 | One-sample, two-sample, paired. Full derivation, Python, assumptions. |
| 12 | B2 | ANOVA is not just multiple t-tests (and here's why) | Statistical Tests | ⬜ | B1 | Why you can't run multiple t-tests. F-statistic, post-hoc tests. |
| 13 | B3 | Chi-square tests: how to make decisions from categories | Statistical Tests | ⬜ | B0 | Goodness of fit, test of independence. Categorical data. |
| 14 | B4 | Statistical power is why your A/B test found nothing | Statistical Tests | ⬜ | B0, B5 | Underpowered experiments. The real cost of low power. |
| 15 | B8 | A/B testing under the hood: what the platform isn't telling you | Statistical Tests | ⬜ | B1, B4, B5 | Peeking, stopping rules, sequential testing. Business-facing capstone for this phase. |
| 16 | B7 | Bayesian vs frequentist: two ways to think about the same data | Statistical Tests | ⬜ | A11, B5 | Priors, posteriors, updating. Requires Bayes' theorem from Phase 1. |

---

### Phase 3: ML Models, Statistically Explained (Posts 17-24)

Each model explained through its statistical foundations, not its API.

| Post | ID | Title | Module | Status | Prerequisites | Notes |
|------|----|-------|--------|--------|---------------|-------|
| 17 | B9 | Linear regression is a projection (and that changes everything) | Statistical Tests | ⬜ | A4, Phase 2 | OLS derivation, assumptions, residual diagnostics. The actual math. |
| 18 | B10 | Logistic regression: why log-odds are the right way to model probability | Statistical Tests | ⬜ | B9, A2 | Sigmoid, MLE. Ties back to probability distributions. |
| 19 | C1 | Decision trees learn by asking the right questions | ML Models | ✅ | A6 | Entropy, Gini, information gain. Statistical criteria behind every split. |
| 20 | C3 | Random forests: why averaging bad models produces a good one | ML Models | ⬜ | C1, A6 | Bagging, bootstrap, variance reduction. Bias-variance tradeoff pays off. |
| 21 | C4 | Gradient boosting learns from its own mistakes | ML Models | ⬜ | C1, B9 | Residuals, sequential correction. Why it wins competitions. |
| 22 | C5 | PCA finds the directions your data cares about | ML Models | ⬜ | A4 | Eigenvectors, explained variance, scree plots. Linear algebra meets statistics. |
| 23 | C2 | K-means clustering: how distance defines similarity | ML Models | ⬜ | A4 | Objective function, convergence, choosing k. Unsupervised through a statistical lens. |
| 24 | C6 | Naive Bayes works despite being wrong about independence | ML Models | ⬜ | A11, A2 | Conditional probability at scale. Spam detection. |

---

### Phase 4: Business Analytics (Posts 25-30)

Where statistics meets real decision-making. These posts can reference anything from Phases 1-3.

| Post | ID | Title | Module | Status | Prerequisites | Notes |
|------|----|-------|--------|--------|---------------|-------|
| 25 | D11 | Simpson's paradox: the most dangerous pattern in business data | Business Analytics | ⬜ | A3, A8 | Real examples from healthcare and admissions. Why aggregation without stratification lies. |
| 26 | D12 | Survivorship bias is hiding your worst decisions from you | Business Analytics | ⬜ | A3 | Focusing on successful customers only ruins insights. |
| 27 | D1 | How to design experiments that survive contact with reality | Business Analytics | ⬜ | Phase 2 | Randomization, blocking, stratification. |
| 28 | D2 | Forecasting is not prediction (and the difference costs companies millions) | Business Analytics | ⬜ | B9 | Prediction intervals vs point estimates. |
| 29 | D3 | Churn models: when to use regression and when to use trees | Business Analytics | ⬜ | B10, C1 | Tradeoffs, interpretability vs performance. |
| 30 | D22 | Metric design: choosing what to measure before you measure it | Business Analytics | ⬜ | Phase 2 | Leading vs lagging indicators, Goodhart's Law, composite metrics. |

---

### Phase 5: AI and Deep Learning Foundations (Posts 31-38)

Statistical thinking applied to modern AI. Assumes the reader has completed Phases 1-3.

| Post | ID | Title | Module | Status | Prerequisites | Notes |
|------|----|-------|--------|--------|---------------|-------|
| 31 | E3 | Loss functions tell models what to care about | AI & Deep Learning | ⬜ | B9 | MSE, cross-entropy, hinge. Each derived from a statistical assumption. |
| 32 | E5 | Gradient descent is the engine behind every trained model | AI & Deep Learning | ⬜ | E3 | Learning rate, convergence, local minima. Light calculus, deep intuition. |
| 33 | E4 | Embeddings turn meaning into geometry | AI & Deep Learning | ⬜ | C5 | word2vec, dimensionality, cosine similarity. Connects back to PCA. |
| 34 | C8 | Neural networks are just weighted sums with a twist | ML Models | ⬜ | E3, E5 | Layers, activation functions. The statistical intuition. |
| 35 | E2 | Attention is just a weighted average (with learned weights) | AI & Deep Learning | ⬜ | C8 | Self-attention, key-query-value, positional encoding. |
| 36 | E1 | LLMs are probability machines (and that explains everything) | AI & Deep Learning | ⬜ | A2, E2 | Temperature, top-k, softmax. Full circle to probability distributions. |
| 37 | E10 | Why AI hallucinates: a statistical explanation | AI & Deep Learning | ⬜ | E1 | Distribution gaps, miscalibrated confidence. |
| 38 | E7 | Uncertainty quantification: what "confident" means for an AI model | AI & Deep Learning | ⬜ | A11, E1 | Calibration, Bayesian deep learning. |

---

## Full Module Reference (Site Navigation View)

Same posts as above, but grouped by module for how they appear on the site.

### Module A: Foundations

| # | Title | Phase | Status |
|---|-------|-------|--------|
| A1 | The central limit theorem is why statistics works | 1 | ✅ |
| A2 | Probability distributions are just rules for uncertainty | 1 | ✅ |
| A3 | Your sample is lying to you (and how to catch it) | 1 | ⬜ |
| A4 | Variance is risk. Standard deviation is the language of risk. | 1 | ⬜ |
| A5 | Confidence intervals don't mean what you think they mean | 1 | ⬜ |
| A6 | The bias-variance tradeoff controls every model you'll ever build | 1 | ⬜ |
| A7 | The law of large numbers is why A/B testing works | 2* | ⬜ |
| A8 | Correlation is not causation (and Simpson's paradox proves it) | 2* | ⬜ |
| A9 | Random variables and expectation: the mental model behind probability | 1* | ⬜ |
| A10 | Separating signal from noise in messy data | 1* | ⬜ |
| A11 | Bayes' theorem is how you update beliefs with evidence | 1 | ⬜ |
| A12 | Conditional probability is the reason most intuitions fail | 1 | ⬜ |

### Module B: Statistical Tests

| # | Title | Phase | Status |
|---|-------|-------|--------|
| B0 | Hypothesis testing from scratch: the logic before the formula | 2 | ⬜ |
| B1 | The t-test: what it's really asking | 2 | ✅ |
| B2 | ANOVA is not just multiple t-tests (and here's why) | 2 | ⬜ |
| B3 | Chi-square tests: how to make decisions from categories | 2 | ⬜ |
| B4 | Statistical power is why your A/B test found nothing | 2 | ⬜ |
| B5 | p-values are not what you were taught | 2 | ⬜ |
| B6 | When your data breaks the rules: nonparametric tests | 2* | ⬜ |
| B7 | Bayesian vs frequentist: two ways to think about the same data | 2 | ⬜ |
| B8 | A/B testing under the hood: what the platform isn't telling you | 2 | ⬜ |
| B9 | Linear regression is a projection (and that changes everything) | 3 | ⬜ |
| B10 | Logistic regression: why log-odds are the right way to model probability | 3 | ⬜ |
| B11 | The multiple comparison problem: why testing everything finds nothing real | 2* | ⬜ |
| B12 | Effect size matters more than significance | 2* | ⬜ |

### Module C: ML Models

| # | Title | Phase | Status |
|---|-------|-------|--------|
| C1 | Decision trees learn by asking the right questions | 3 | ✅ |
| C2 | K-means clustering: how distance defines similarity | 3 | ⬜ |
| C3 | Random forests: why averaging bad models produces a good one | 3 | ⬜ |
| C4 | Gradient boosting learns from its own mistakes | 3 | ⬜ |
| C5 | PCA finds the directions your data cares about | 3 | ⬜ |
| C6 | Naive Bayes works despite being wrong about independence | 3 | ⬜ |
| C7 | SVMs find the widest gap between classes | 3* | ⬜ |
| C8 | Neural networks are just weighted sums with a twist | 5 | ⬜ |
| C9 | Regularization is how you punish a model for being too clever | 3* | ⬜ |
| C10 | Accuracy is lying to you: evaluation metrics that actually matter | 3* | ⬜ |
| C11 | The curse of dimensionality: why more features make models worse | 3* | ⬜ |
| C12 | Cross-validation is the only honest way to test a model | 3* | ⬜ |

### Module D: Business Analytics

| # | Title | Phase | Status |
|---|-------|-------|--------|
| D1 | How to design experiments that survive contact with reality | 4 | ⬜ |
| D2 | Forecasting is not prediction (and the difference costs companies millions) | 4 | ⬜ |
| D3 | Churn models: when to use regression and when to use trees | 4 | ⬜ |
| D4 | Revenue attribution is a statistical problem most companies solve wrong | 4* | ⬜ |
| D5 | Customer lifetime value has a formula (and most companies ignore it) | 4* | ⬜ |
| D6 | Pricing experiments fail for three statistical reasons | 4* | ⬜ |
| D7 | A/B/n testing at scale: sequential methods and when to stop | 4* | ⬜ |
| D8 | Customer segmentation: statistical methods vs ML methods | 4* | ⬜ |
| D9 | Marketing attribution models and their statistical weak spots | 4* | ⬜ |
| D10 | Fraud detection often doesn't need ML (statistics is enough) | 4* | ⬜ |
| D11 | Simpson's paradox: the most dangerous pattern in business data | 4 | ⬜ |
| D12 | Survivorship bias is hiding your worst decisions from you | 4 | ⬜ |
| D22 | Metric design: choosing what to measure before you measure it | 4 | ⬜ |

### Module E: AI & Deep Learning

| # | Title | Phase | Status |
|---|-------|-------|--------|
| E1 | LLMs are probability machines (and that explains everything) | 5 | ⬜ |
| E2 | Attention is just a weighted average (with learned weights) | 5 | ⬜ |
| E3 | Loss functions tell models what to care about | 5 | ⬜ |
| E4 | Embeddings turn meaning into geometry | 5 | ⬜ |
| E5 | Gradient descent is the engine behind every trained model | 5 | ⬜ |
| E6 | Overfitting in deep learning: dropout is approximate Bayesian inference | 5* | ⬜ |
| E7 | Uncertainty quantification: what "confident" means for an AI model | 5 | ⬜ |
| E8 | The transformer architecture, explained statistically | 5* | ⬜ |
| E9 | Data leakage: the silent killer of ML projects | 5* | ⬜ |
| E10 | Why AI hallucinates: a statistical explanation | 5 | ⬜ |

*Posts marked with * are flexible in timing. They can be published whenever their prerequisites are met, outside the strict phase sequence.

---

## Companion Posts (Code-First & Pitfalls)

These are not standalone posts. They're companions to a main post and should publish within 1-2 weeks of their parent.

| Companion title | Parent post | Module | Notes |
|-----------------|------------|--------|-------|
| Visualizing the CLT in Python | A1 | Foundations | Hands-on follow-up |
| Sampling distributions in Python | A3 | Foundations | Simulation-based teaching |
| Bootstrapping confidence intervals in Python | A5 | Foundations | Code-first companion |
| Misinterpreting confidence intervals | A5 | Foundations | Pitfall companion |
| Misuse of correlation matrices | A8 | Foundations | Pitfall companion |
| Statistical power analysis in Python | B4 | Statistical Tests | Code-first companion |
| A/B testing in SQL | B8 | Statistical Tests | Code-first companion |
| Logistic regression MLE in R | B10 | Statistical Tests | Code-first companion |
| Normality assumptions: the silent killer | B6 | Statistical Tests | Pitfall companion |
| p-hacking: how analysts mislead without meaning to | B5 | Statistical Tests | Pitfall companion |
| K-means from scratch in Python | C2 | ML Models | Code-first companion |
| Decision tree splits using entropy in Python | C1 | ML Models | Code-first companion |
| PCA walkthrough with NumPy | C5 | ML Models | Code-first companion |
| When analysts add too many features | C11 | ML Models | Pitfall companion |
| Monte Carlo simulation for forecasting in Python | D2 | Business Analytics | Code-first companion |
| Confirmation bias in data science | D (general) | Business Analytics | Pitfall companion |
| "Big data" creates more mistakes than it solves | D (general) | Business Analytics | Pitfall companion |

---

## Publishing Cadence

One post per week. At this pace:
- Phase 1 (8 posts): weeks 1-8
- Phase 2 (8 posts): weeks 9-16
- Phase 3 (8 posts): weeks 17-24
- Phase 4 (6 posts): weeks 25-30
- Phase 5 (8 posts): weeks 31-38

38 core posts = ~9.5 months. Add companion posts between phases for ~12 months total.

**Immediate next 4 posts to write:**
1. A2 (Probability distributions)
2. A3 (Sampling)
3. A4 (Variance and standard deviation)
4. A5 (Confidence intervals)

---

## Publishing Workflow

1. **Draft** the post in Claude using the statbitall-content skill (6-part structure)
2. **Humanize** with the humanizer skill (strip AI patterns, score, rewrite)
3. **Save** as .mdx file
4. **Drop** into src/content/blog/ in VS Code
5. **Preview** at localhost:4321
6. **Push** to GitHub (auto-deploys to Vercel)
7. **Update this document** (change status from ⬜ to ✅, add publish date)

---

## Score

✅ Published: 3 posts (A1, B1, C1)
⬜ Remaining: 55+ core posts, 17 companion posts
