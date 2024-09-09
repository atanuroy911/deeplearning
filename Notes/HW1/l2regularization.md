In L2 regularization, the cost function is modified by adding a penalty term that depends on the magnitude of the weights. For a neural network with weights $W_1$ and $W_2$, the regularized cost function $J$ can be expressed as:

$$
J_{\text{reg}} = J_{\text{original}} + \frac{\lambda}{2} \left( \| W_1 \|^2 + \| W_2 \|^2 \right)
$$

Where:
- $J_{\text{original}}$ is the original cost (e.g., cross-entropy or mean squared error).
- $\lambda$ is the regularization parameter.
- $\| W_1 \|^2$ and $\| W_2 \|^2$ represent the sum of the squared elements of $W_1$ and $W_2$ (the L2 norm).

When computing the gradients during backpropagation, without regularization, the gradients of the loss with respect to the weights would be $\frac{\partial J_{\text{original}}}{\partial W_1}$ and $\frac{\partial J_{\text{original}}}{\partial W_2}$.

With L2 regularization, the gradients are adjusted as follows:

$$
\frac{\partial J_{\text{reg}}}{\partial W_1} = \frac{\partial J_{\text{original}}}{\partial W_1} + \lambda W_1
$$

$$
\frac{\partial J_{\text{reg}}}{\partial W_2} = \frac{\partial J_{\text{original}}}{\partial W_2} + \lambda W_2
$$

This corresponds to the code snippet you provided:
- `model.gradients["W1"] += self.reg * model.weights["W1"]` adds the term $\lambda W_1$ to the gradient for $W_1$.
- `model.gradients["W2"] += self.reg * model.weights["W2"]` adds the term $\lambda W_2$ to the gradient for $W_2$.

Thus, L2 regularization modifies the gradient by adding $\lambda W$ to the gradient of each weight matrix, effectively pushing the weights to smaller values.