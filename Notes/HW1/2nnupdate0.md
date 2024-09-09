To derive the weight update equations for the two-layer neural network, let's break down the process into the gradients of the loss function with respect to each weight and bias term. 

For simplicity, let:

- $W_1$: weights of the first layer (input to hidden)
- $b_1$: bias of the first layer
- $W_2$: weights of the second layer (hidden to output)
- $b_2$: bias of the second layer
- $Z_1 = XW_1 + b_1$
- $O_1 = \sigma(Z_1)$ (applying the sigmoid activation)
- $Z_2 = O_1W_2 + b_2$
- $\text{softmax}(Z_2) = \hat{y}$: probabilities of the output layer

### Gradient with respect to $W_2$ and $b_2$:

The output of the network is passed through a softmax function, and the loss is computed using cross-entropy. The gradients for $W_2$ and $b_2$ are:

1. **Gradient of the loss with respect to $Z_2$**:
   $$
   \frac{\partial L}{\partial Z_2} = \hat{y} - y_{\text{true}}
   $$
   where $y_{\text{true}}$ is the one-hot encoded true label and $\hat{y}$ is the softmax output.

2. **Gradient of the loss with respect to $W_2$**:
   The gradient of the loss with respect to $W_2$ is calculated using the chain rule:
   $$
   \frac{\partial L}{\partial W_2} = O_1^T \cdot (\hat{y} - y_{\text{true}})
   $$
   where $O_1^T$ is the transpose of the output of the first layer (after the sigmoid activation).

3. **Gradient of the loss with respect to $b_2$**:
   The bias gradient is obtained by summing the loss gradients over all examples in the batch:
   $$
   \frac{\partial L}{\partial b_2} = \sum_{i=1}^{N} (\hat{y}_i - y_{\text{true},i})
   $$
   where $N$ is the number of samples in the batch.

### Gradient with respect to $W_1$ and $b_1$:

To compute the gradients for $W_1$ and $b_1$, we need to propagate the error backwards through the network using the chain rule.

1. **Gradient of the loss with respect to $Z_1$**:
   $$
   \frac{\partial L}{\partial Z_1} = \left( (\hat{y} - y_{\text{true}}) \cdot W_2^T \right) \cdot \sigma'(Z_1)
   $$
   where $\sigma'(Z_1)$ is the derivative of the sigmoid activation function.

2. **Gradient of the loss with respect to $W_1$**:
   $$
   \frac{\partial L}{\partial W_1} = X^T \cdot \left( \frac{\partial L}{\partial Z_1} \right)
   $$
   Here, $X^T$ is the transpose of the input matrix.

3. **Gradient of the loss with respect to $b_1$**:
   $$
   \frac{\partial L}{\partial b_1} = \sum_{i=1}^{N} \frac{\partial L}{\partial Z_1}
   $$

### Weight Update Rule:

In gradient descent, the weights are updated using the gradients computed above. The update rule for each weight and bias is:

$$
W_2 \leftarrow W_2 - \eta \cdot \frac{\partial L}{\partial W_2}
$$
$$
b_2 \leftarrow b_2 - \eta \cdot \frac{\partial L}{\partial b_2}
$$
$$
W_1 \leftarrow W_1 - \eta \cdot \frac{\partial L}{\partial W_1}
$$
$$
b_1 \leftarrow b_1 - \eta \cdot \frac{\partial L}{\partial b_1}
$$

where $\eta$ is the learning rate.