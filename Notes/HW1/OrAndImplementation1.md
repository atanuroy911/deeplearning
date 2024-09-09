
### Linear Threshold Neuron
The function for a linear threshold neuron is given by:

$$
f(x_1, x_2) = 
\begin{cases}
1 & \text{if } w_1 x_1 + w_2 x_2 + b \geq 0 \\
0 & \text{if } w_1 x_1 + w_2 x_2 + b < 0
\end{cases}
$$

### 1. AND Gate Implementation

The AND gate outputs 1 only if both inputs are 1.

**Truth Table:**

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

**Weights and Bias Selection:**

To satisfy the conditions:
- When $(x_1, x_2) = (0, 0)$: $w_1 \cdot 0 + w_2 \cdot 0 + b < 0$ (outputs 0)
- When $(x_1, x_2) = (0, 1)$: $w_1 \cdot 0 + w_2 \cdot 1 + b < 0$ (outputs 0)
- When $(x_1, x_2) = (1, 0)$: $w_1 \cdot 1 + w_2 \cdot 0 + b < 0$ (outputs 0)
- When $(x_1, x_2) = (1, 1)$: $w_1 \cdot 1 + w_2 \cdot 1 + b \geq 0$ (outputs 1)

A possible solution is $w_1 = 1$, $w_2 = 1$, and $b = -1.5$.

**Tabular Solution:**

$$
\begin{array}{|c|c|c|c|}
\hline
x_1 & x_2 & w_1 x_1 + w_2 x_2 + b & f(x_1, x_2) \\
\hline
0 & 0 & 0 \cdot 1 + 0 \cdot 1 - 1.5 = -1.5 & 0 \\
0 & 1 & 0 \cdot 1 + 1 \cdot 1 - 1.5 = -0.5 & 0 \\
1 & 0 & 1 \cdot 1 + 0 \cdot 1 - 1.5 = -0.5 & 0 \\
1 & 1 & 1 \cdot 1 + 1 \cdot 1 - 1.5 = 0.5 & 1 \\
\hline
\end{array}
$$

### 2. OR Gate Implementation

The OR gate outputs 1 if at least one input is 1.

**Truth Table:**

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

**Weights and Bias Selection:**

To satisfy the conditions:
- When $(x_1, x_2) = (0, 0)$: $w_1 \cdot 0 + w_2 \cdot 0 + b < 0$ (outputs 0)
- When $(x_1, x_2) = (0, 1)$: $w_1 \cdot 0 + w_2 \cdot 1 + b \geq 0$ (outputs 1)
- When $(x_1, x_2) = (1, 0)$: $w_1 \cdot 1 + w_2 \cdot 0 + b \geq 0$ (outputs 1)
- When $(x_1, x_2) = (1, 1)$: $w_1 \cdot 1 + w_2 \cdot 1 + b \geq 0$ (outputs 1)

A possible solution is $w_1 = 1$, $w_2 = 1$, and $b = -0.5$.

**Tabular Solution:**

$$
\begin{array}{|c|c|c|c|}
\hline
x_1 & x_2 & w_1 x_1 + w_2 x_2 + b & f(x_1, x_2) \\
\hline
0 & 0 & 0 \cdot 1 + 0 \cdot 1 - 0.5 = -0.5 & 0 \\
0 & 1 & 0 \cdot 1 + 1 \cdot 1 - 0.5 = 0.5 & 1 \\
1 & 0 & 1 \cdot 1 + 0 \cdot 1 - 0.5 = 0.5 & 1 \\
1 & 1 & 1 \cdot 1 + 1 \cdot 1 - 0.5 = 1.5 & 1 \\
\hline
\end{array}
$$

### Conclusion

Using the weights and biases provided, the linear threshold neuron correctly implements the AND and OR gates, as verified by the tabular solutions.