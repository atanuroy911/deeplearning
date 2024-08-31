Let's walk through an example of performing Singular Value Decomposition (SVD) on a simple matrix \( A \), and then use it to compute the pseudoinverse of \( A \).

### Example Matrix

Consider the matrix \( A \):

\[
A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}
\]

This is a \( 3 \times 2 \) matrix, which means it's not square.

### Step 1: Compute \( A^\top A \) and \( AA^\top \)

First, let's compute \( A^\top A \) and \( AA^\top \):

\[
A^\top = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}
\]

\[
A^\top A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\]

\[
AA^\top = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}
\]

### Step 2: Compute Eigenvalues and Eigenvectors

- **Right-singular vectors** (columns of \( V \)) are the eigenvectors of \( A^\top A \).
- **Left-singular vectors** (columns of \( U \)) are the eigenvectors of \( AA^\top \).
- **Singular values** are the square roots of the eigenvalues of \( A^\top A \) or \( AA^\top \).

#### Eigenvalues and Eigenvectors of \( A^\top A \):

\[
A^\top A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\]

The eigenvalues are \( 1 \) and \( 1 \), with corresponding eigenvectors:

\[
V = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\]

#### Eigenvalues and Eigenvectors of \( AA^\top \):

\[
AA^\top = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}
\]

The eigenvalues are \( 1 \), \( 1 \), and \( 0 \), with corresponding eigenvectors:

\[
U = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
\]

### Step 3: Construct the Diagonal Matrix \( \Sigma \)

The singular values (square roots of the nonzero eigenvalues) are \( \sigma_1 = 1 \) and \( \sigma_2 = 1 \). Thus, \( \Sigma \) is:

\[
\Sigma = \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}
\]

### Step 4: Assemble the SVD

Now, we can write the SVD of \( A \) as:

\[
A = U \Sigma V^\top = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\]

### Step 5: Compute the Pseudoinverse \( A^\dagger \)

To compute the pseudoinverse \( A^\dagger \), we invert the nonzero singular values in \( \Sigma \) and transpose \( U \) and \( V \):

\[
\Sigma^\dagger = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}
\]

\[
A^\dagger = V \Sigma^\dagger U^\top = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}
\]

So the pseudoinverse \( A^\dagger \) is:

\[
A^\dagger = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}
\]

### Summary

The SVD allowed us to decompose \( A \) into orthogonal matrices \( U \) and \( V \) and a diagonal matrix \( \Sigma \). We then used this decomposition to compute the pseudoinverse \( A^\dagger \). This pseudoinverse is particularly useful for solving systems of linear equations when \( A \) is not square or not of full rank.