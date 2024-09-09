To implement the AND and OR functions for pairs of binary inputs using a single linear threshold neuron, we need to define the weights $\mathbf{w} \in \mathbb{R}^2$, bias $b \in \mathbb{R}$, and the input vector $\mathbf{x} \in \{0, 1\}^2$. The neuron outputs 1 if the linear combination of inputs is greater than or equal to zero, and 0 otherwise:

$$
f(\mathbf{x}) =
\begin{cases}
1 & \text{if } \mathbf{w}^T \mathbf{x} + b \geq 0 \\
0 & \text{if } \mathbf{w}^T \mathbf{x} + b < 0
\end{cases}
$$

### AND Gate Implementation

For an AND gate, the neuron should output 1 only when both inputs are 1 (i.e., $x_1 = 1$ and $x_2 = 1$). The truth table for an AND gate is:

$$
\begin{array}{|c|c|c|}
\hline
x_1 & x_2 & \text{AND}(x_1, x_2) \\
\hline
0 & 0 & 0 \\
0 & 1 & 0 \\
1 & 0 & 0 \\
1 & 1 & 1 \\
\hline
\end{array}
$$

We need to find $\mathbf{w} = [w_1, w_2]$ and $b$ such that:

$$
f(x_1, x_2) =
\begin{cases}
1 & \text{if } w_1 x_1 + w_2 x_2 + b \geq 0 \\
0 & \text{if } w_1 x_1 + w_2 x_2 + b < 0
\end{cases}
$$

For $(x_1, x_2) = (1, 1)$, we want $w_1 + w_2 + b \geq 0$.

For the other input pairs, we need:

- $(x_1, x_2) = (0, 0):$ $b < 0$
- $(x_1, x_2) = (1, 0):$ $w_1 + b < 0$
- $(x_1, x_2) = (0, 1):$ $w_2 + b < 0$

A solution that works is:

- $w_1 = 1$
- $w_2 = 1$
- $b = -1.5$

Thus, the neuron computes:

$$
f(\mathbf{x}) = \begin{cases}
1 & \text{if } x_1 + x_2 - 1.5 \geq 0 \\
0 & \text{if } x_1 + x_2 - 1.5 < 0
\end{cases}
$$

### OR Gate Implementation

For an OR gate, the neuron should output 1 if at least one of the inputs is 1. The truth table for an OR gate is:

$$
\begin{array}{|c|c|c|}
\hline
x_1 & x_2 & \text{OR}(x_1, x_2) \\
\hline
0 & 0 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1 \\
1 & 1 & 1 \\
\hline
\end{array}
$$

We need to find $\mathbf{w} = [w_1, w_2]$ and $b$ such that:

$$
f(x_1, x_2) =
\begin{cases}
1 & \text{if } w_1 x_1 + w_2 x_2 + b \geq 0 \\
0 & \text{if } w_1 x_1 + w_2 x_2 + b < 0
\end{cases}
$$

For $(x_1, x_2) = (1, 0)$, $(0, 1)$, and $(1, 1)$, we need:

- $w_1 + b \geq 0$
- $w_2 + b \geq 0$
- $w_1 + w_2 + b \geq 0$

For $(x_1, x_2) = (0, 0)$, we need:

- $b < 0$

A solution that works is:

- $w_1 = 1$
- $w_2 = 1$
- $b = -0.5$

Thus, the neuron computes:

$$
f(\mathbf{x}) = \begin{cases}
1 & \text{if } x_1 + x_2 - 0.5 \geq 0 \\
0 & \text{if } x_1 + x_2 - 0.5 < 0
\end{cases}
$$

### Summary

- **AND Gate**: $\mathbf{w} = [1, 1]$, $b = -1.5$
- **OR Gate**: $\mathbf{w} = [1, 1]$, $b = -0.5$

These configurations allow a single linear threshold neuron to correctly implement the AND and OR logic gates.