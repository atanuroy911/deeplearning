Momentum is a technique used in optimization algorithms, such as Stochastic Gradient Descent (SGD), to speed up convergence and improve the stability of the training process, especially in scenarios with noisy gradients or when the objective function has a lot of curvature.

### What does momentum do?
In standard SGD, the weight update rule is:

$$
W_{\text{new}} = W_{\text{old}} - \eta \cdot \nabla W
$$

Where:
- $W_{\text{new}}$ and $W_{\text{old}}$ are the updated and previous weights, respectively.
- $\eta$ is the learning rate.
- $\nabla W$ is the gradient of the loss with respect to the weights.

With momentum, the update takes into account not only the current gradient but also the past updates, allowing it to "build speed" in directions where the gradient consistently points. The update rule with momentum is as follows:

$$
v_t = \gamma v_{t-1} + \eta \cdot \nabla W_t
$$
$$
W_{\text{new}} = W_{\text{old}} - v_t
$$

Where:
- $v_t$ is the velocity or accumulated gradient at time step $t$.
- $\gamma$ is the momentum coefficient (e.g., 0.9).
- $\eta$ is the learning rate.
- $\nabla W_t$ is the current gradient.

### Key Terms:
- **Momentum coefficient ($\gamma$):** A number between 0 and 1 (like 0.9) that determines how much of the past velocity should be carried over to the current step. Higher values of momentum encourage the optimizer to keep moving in the same direction.
- **Velocity $v_t$:** The moving average of the gradients, allowing the optimizer to have smoother and faster progress across noisy or slow-learning regions.

### Benefits of Momentum:
1. **Faster Convergence:** By building velocity in directions of consistent gradients, momentum allows faster convergence than standard SGD.
2. **Smoothing Out Oscillations:** Especially in regions where gradients oscillate (e.g., along valleys), momentum smooths the updates and prevents the optimizer from getting stuck.
3. **Escaping Local Minima:** Momentum helps overcome small local minima by maintaining speed in the more promising direction.

In summary, a momentum value of 0.9 means that 90% of the previous velocity is carried forward, which accelerates gradient descent in the relevant directions.