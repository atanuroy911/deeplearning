To solve the problem shown in the image, we need to compute the derivative of the matrix-valued function $y = f(x)$ with respect to the vector $\vec{x}$. The function $f: \mathbb{R}^3 \to \mathbb{R}^{2 \times 4}$ maps a 3-dimensional vector $\vec{x}$ to a $2 \times 4$ matrix $y$.

Given:
- $\vec{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$
- $y = f(\vec{x}) = \begin{bmatrix} \sum_i x_i & x_1 x_3 & x_2 x_3 & x_2 \\ x_1 x_2 & x_1^2 & x_2^2 & x_3 \end{bmatrix}$

We need to find the Jacobian matrix $\frac{\partial y}{\partial \vec{x}}$, which is a matrix of partial derivatives. The Jacobian matrix will be of size $(2 \times 4) \times 3 = 8 \times 3$.

### Steps to Solve:

1. **Identify the components of $y$:**
   - $y_{11} = x_1 + x_2 + x_3$
   - $y_{12} = x_1 x_3$
   - $y_{13} = x_2 x_3$
   - $y_{14} = x_2$
   - $y_{21} = x_1 x_2$
   - $y_{22} = x_1^2$
   - $y_{23} = x_2^2$
   - $y_{24} = x_3$

2. **Compute the partial derivatives:**

   - For $y_{11}$:
     $$
     \frac{\partial y_{11}}{\partial x_1} = 1, \quad \frac{\partial y_{11}}{\partial x_2} = 1, \quad \frac{\partial y_{11}}{\partial x_3} = 1
     $$
   - For $y_{12}$:
     $$
     \frac{\partial y_{12}}{\partial x_1} = x_3, \quad \frac{\partial y_{12}}{\partial x_2} = 0, \quad \frac{\partial y_{12}}{\partial x_3} = x_1
     $$
   - For $y_{13}$:
     $$
     \frac{\partial y_{13}}{\partial x_1} = 0, \quad \frac{\partial y_{13}}{\partial x_2} = x_3, \quad \frac{\partial y_{13}}{\partial x_3} = x_2
     $$
   - For $y_{14}$:
     $$
     \frac{\partial y_{14}}{\partial x_1} = 0, \quad \frac{\partial y_{14}}{\partial x_2} = 1, \quad \frac{\partial y_{14}}{\partial x_3} = 0
     $$
   - For $y_{21}$:
     $$
     \frac{\partial y_{21}}{\partial x_1} = x_2, \quad \frac{\partial y_{21}}{\partial x_2} = x_1, \quad \frac{\partial y_{21}}{\partial x_3} = 0
     $$
   - For $y_{22}$:
     $$
     \frac{\partial y_{22}}{\partial x_1} = 2x_1, \quad \frac{\partial y_{22}}{\partial x_2} = 0, \quad \frac{\partial y_{22}}{\partial x_3} = 0
     $$
   - For $y_{23}$:
     $$
     \frac{\partial y_{23}}{\partial x_1} = 0, \quad \frac{\partial y_{23}}{\partial x_2} = 2x_2, \quad \frac{\partial y_{23}}{\partial x_3} = 0
     $$
   - For $y_{24}$:
     $$
     \frac{\partial y_{24}}{\partial x_1} = 0, \quad \frac{\partial y_{24}}{\partial x_2} = 0, \quad \frac{\partial y_{24}}{\partial x_3} = 1
     $$

3. **Assemble the Jacobian matrix**:

   The Jacobian matrix $J = \frac{\partial y}{\partial \vec{x}}$ will be:

   $$
   J = \begin{bmatrix}
   \frac{\partial y_{11}}{\partial x_1} & \frac{\partial y_{11}}{\partial x_2} & \frac{\partial y_{11}}{\partial x_3} \\
   \frac{\partial y_{12}}{\partial x_1} & \frac{\partial y_{12}}{\partial x_2} & \frac{\partial y_{12}}{\partial x_3} \\
   \frac{\partial y_{13}}{\partial x_1} & \frac{\partial y_{13}}{\partial x_2} & \frac{\partial y_{13}}{\partial x_3} \\
   \frac{\partial y_{14}}{\partial x_1} & \frac{\partial y_{14}}{\partial x_2} & \frac{\partial y_{14}}{\partial x_3} \\
   \frac{\partial y_{21}}{\partial x_1} & \frac{\partial y_{21}}{\partial x_2} & \frac{\partial y_{21}}{\partial x_3} \\
   \frac{\partial y_{22}}{\partial x_1} & \frac{\partial y_{22}}{\partial x_2} & \frac{\partial y_{22}}{\partial x_3} \\
   \frac{\partial y_{23}}{\partial x_1} & \frac{\partial y_{23}}{\partial x_2} & \frac{\partial y_{23}}{\partial x_3} \\
   \frac{\partial y_{24}}{\partial x_1} & \frac{\partial y_{24}}{\partial x_2} & \frac{\partial y_{24}}{\partial x_3} \\
   \end{bmatrix}
   $$

   Substituting the values:

   $$
   J = \begin{bmatrix}
   1 & 1 & 1 \\
   x_3 & 0 & x_1 \\
   0 & x_3 & x_2 \\
   0 & 1 & 0 \\
   x_2 & x_1 & 0 \\
   2x_1 & 0 & 0 \\
   0 & 2x_2 & 0 \\
   0 & 0 & 1 \\
   \end{bmatrix}
   $$

This matrix $J$ represents the derivative of the matrix-valued function $y = f(x)$ with respect to the vector $\vec{x}$.