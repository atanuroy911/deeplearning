
### 1. **Inheriting from `_BaseOptimizer`**
The class `SGD` inherits from a base optimizer class `_BaseOptimizer`. The base class likely handles generic functionality like initializing the optimizer's parameters.

- The constructor `__init__(self, learning_rate=1e-4, reg=1e-3)` sets the learning rate and regularization strength (`reg`), and passes them to the base class.

### 2. **Updating Weights with Gradients**
The core of the SGD update process happens in the `update` method. The goal is to modify the weights and biases of the model using their respective gradients:

$$
W_{\text{new}} = W_{\text{old}} - \eta \cdot \nabla W
$$

Where:
- $W_{\text{new}}$ is the updated weight matrix.
- $W_{\text{old}}$ is the current weight matrix.
- $\eta$ is the learning rate.
- $\nabla W$ is the gradient of the loss function with respect to the weights.

### Steps in the `update` function:
1. **Apply Regularization:**
   The method `self.apply_regularization(model)` applies regularization (likely L2) to the gradients of the weights, as seen in your earlier code where the regularization term is added to the gradients.

2. **Weight Update:**
   The update occurs for each weight matrix and bias term, following the SGD rule:
   - For `W1` (first layer weights), the update is:
     $$
     W1_{\text{new}} = W1_{\text{old}} - \eta \cdot \nabla W1
     $$
   - Similarly for `W2` (second layer weights):
     $$
     W2_{\text{new}} = W2_{\text{old}} - \eta \cdot \nabla W2
     $$
   - The same applies to the biases `b1` and `b2`.

### Example Equations for Updates:
- For weights:
  $$
  W1_{\text{new}} = W1_{\text{old}} - \text{learning\_rate} \cdot \text{gradients["W1"]}
  $$
- For biases:
  $$
  b1_{\text{new}} = b1_{\text{old}} - \text{learning\_rate} \cdot \text{gradients["b1"]}
  $$

This ensures that the model’s weights and biases are updated iteratively during each training step to minimize the loss.