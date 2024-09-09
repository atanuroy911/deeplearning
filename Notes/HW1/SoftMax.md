To derive the gradient of the softmax function $s(z)$ with respect to its input $z$, we can build on the work done in Problem Set 0, where the gradient of the log-sum-exp function was derived. The softmax function is defined as:

$$
s_i(z) = \frac{e^{z_i}}{\sum_{k} e^{z_k}}
$$

where $z$ is a vector, and $s_i(z)$ is the $i$th component of the softmax output.

### Step 1: Recalling the Gradient of the Log-Sum-Exp Function

In Problem Set 0, the log-sum-exp function was defined as:

$$
\text{LSE}(z) = \log\left(\sum_{k} e^{z_k}\right)
$$

The gradient of the log-sum-exp function with respect to $z_i$ is:

$$
\frac{\partial \text{LSE}(z)}{\partial z_i} = \frac{e^{z_i}}{\sum_{k} e^{z_k}} = s_i(z)
$$

### Step 2: Deriving the Gradient of the Softmax Function

Now, let's derive the gradient of the softmax function $s(z)$ with respect to $z$. We want to compute the Jacobian matrix $\frac{\partial s_i}{\partial z_j}$, which gives us the partial derivative of each component of the softmax output with respect to each component of the input vector $z$.

The softmax function can be written explicitly as:

$$
s_i(z) = \frac{e^{z_i}}{\sum_{k} e^{z_k}}
$$

Taking the derivative of $s_i(z)$ with respect to $z_j$ for $i$ and $j$, we have two cases to consider:

1. **Case 1: $i = j$**

$$
\frac{\partial s_i(z)}{\partial z_i} = \frac{\partial}{\partial z_i} \left(\frac{e^{z_i}}{\sum_{k} e^{z_k}}\right)
$$

Using the quotient rule:

$$
\frac{\partial s_i(z)}{\partial z_i} = \frac{e^{z_i} \cdot \sum_{k} e^{z_k} - e^{z_i} \cdot e^{z_i}}{\left(\sum_{k} e^{z_k}\right)^2}
$$

Simplifying:

$$
\frac{\partial s_i(z)}{\partial z_i} = s_i(z) \left(1 - s_i(z)\right)
$$

2. **Case 2: $i \neq j$**

For $i \neq j$:

$$
\frac{\partial s_i(z)}{\partial z_j} = \frac{\partial}{\partial z_j} \left(\frac{e^{z_i}}{\sum_{k} e^{z_k}}\right)
$$

Again, using the quotient rule:

$$
\frac{\partial s_i(z)}{\partial z_j} = \frac{0 \cdot \sum_{k} e^{z_k} - e^{z_i} \cdot e^{z_j}}{\left(\sum_{k} e^{z_k}\right)^2}
$$

Simplifying:

$$
\frac{\partial s_i(z)}{\partial z_j} = -s_i(z) \cdot s_j(z)
$$

### Step 3: Expressing the Gradient in Matrix Form

The gradient of the softmax function with respect to the logits $z$ can be expressed as the Jacobian matrix $\frac{\partial s}{\partial z}$, where each element is:

$$
\frac{\partial s_i(z)}{\partial z_j} = s_i(z) \left(\delta_{ij} - s_j(z)\right)
$$

Here, $\delta_{ij}$ is the Kronecker delta, which is 1 if $i = j$ and 0 otherwise. In matrix form, this can be expressed as:

$$
\frac{\partial s}{\partial z} = \text{diag}(s) - s s^T
$$

Where $\text{diag}(s)$ is a diagonal matrix with the elements of $s(z)$ on the diagonal, and $s s^T$ is the outer product of $s(z)$ with itself.

This matrix gives the gradient of the softmax function with respect to its input vector $z$.