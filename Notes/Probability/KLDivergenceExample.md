## Kullback-Leibler (KL) Divergence

Kullback-Leibler (KL) divergence is a measure of how one probability distribution diverges from a second, reference probability distribution. It's often used in statistics and machine learning to quantify the difference between two probability distributions.

### Mathematical Definition

Given two probability distributions \(P\) and \(Q\) over the same probability space, the KL divergence from \(Q\) to \(P\) is defined as:

$$
D_{KL}(P \parallel Q) = \sum_{x} P(x) \log \frac{P(x)}{Q(x)}
$$

Or in the continuous case:

$$
D_{KL}(P \parallel Q) = \int_{-\infty}^{\infty} P(x) \log \frac{P(x)}{Q(x)} \, dx
$$

### Intuition
- **\(P\)** is the true distribution (or the distribution you want to approximate).
- **\(Q\)** is the approximation or reference distribution.

The KL divergence measures how much information is lost when \(Q\) is used to approximate \(P\). It is always non-negative, and \(D_{KL}(P \parallel Q) = 0\) if and only if \(P = Q\) almost everywhere.

### Example

Suppose you have two discrete probability distributions over a random variable \(X\), where \(X\) can take on three values: \(x_1\), \(x_2\), and \(x_3\).

Let \(P\) and \(Q\) be defined as follows:

- \(P(x_1) = 0.1\), \(P(x_2) = 0.4\), \(P(x_3) = 0.5\)
- \(Q(x_1) = 0.2\), \(Q(x_2) = 0.3\), \(Q(x_3) = 0.5\)

To calculate the KL divergence \(D_{KL}(P \parallel Q)\):

$$
D_{KL}(P \parallel Q) = 0.1 \log \frac{0.1}{0.2} + 0.4 \log \frac{0.4}{0.3} + 0.5 \log \frac{0.5}{0.5}
$$

Calculating each term:

- \(0.1 \log \frac{0.1}{0.2} = 0.1 \log 0.5 = 0.1 \times (-0.3010) = -0.0301\)
- \(0.4 \log \frac{0.4}{0.3} = 0.4 \log \frac{4}{3} = 0.4 \times 0.1249 = 0.04996\)
- \(0.5 \log \frac{0.5}{0.5} = 0.5 \times 0 = 0\)

Summing these values:

$$
D_{KL}(P \parallel Q) = -0.0301 + 0.04996 + 0 = 0.01986
$$

### Interpretation

The KL divergence \(D_{KL}(P \parallel Q) = 0.01986\) indicates that there is a small amount of information lost when using \(Q\) to approximate \(P\). The lower the KL divergence, the closer the two distributions are.
