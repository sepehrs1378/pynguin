class Matrix:
    def __init__(self, data: list[list[int | float]]):
        """Initialize matrix with 2D list data."""
        if (
            not isinstance(data, list)
            or len(data) == 0
            or not all(isinstance(row, list) for row in data)
            or not all(len(row) == len(data[0]) for row in data)
            or not all(all(isinstance(cell, (int, float)) for cell in row) for row in data)
        ):
            raise ValueError("Matrix must be a 2D list")
        self.data: list[list[int | float]] = data
        self.rows: int = len(data)
        self.cols: int = len(data[0]) if self.rows > 0 else 0

    # 1. Basic Operations
    def add(self, other: "Matrix"):
        """Add another matrix to this one."""
        self._check_dimensions(other)
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def subtract(self, other: "Matrix"):
        """Subtract another matrix from this one."""
        self._check_dimensions(other)
        return Matrix([[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)])

    def scale(self, scalar: float):
        """Multiply matrix by a scalar."""
        return Matrix([[self.data[i][j] * scalar for j in range(self.cols)] for i in range(self.rows)])

    # 2. Matrix Multiplication
    def multiply(self, other: "Matrix"):
        """Multiply with another matrix."""
        if self.cols != other.rows:
            raise ValueError("Columns of A must match rows of B")

        result: list[list[int | float]] = [[0 for j in range(other.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    # 3. Transpose
    def transpose(self):
        """Return the transpose of the matrix."""
        return Matrix([list(col) for col in zip(*self.data)])

    # 4. Trace
    def trace(self):
        """Sum of diagonal elements."""
        if not self.is_square():
            raise ValueError("Matrix must be square")
        return sum(self.data[i][i] for i in range(self.rows))

    # 5. Determinant
    def determinant(self):
        """Calculate the determinant of a square matrix using recursive approach."""
        if not self.is_square():
            raise ValueError("Determinant is only defined for square matrices")

        n = self.rows

        # Base case for 1x1 matrix
        if n == 1:
            return self.data[0][0]

        # Base case for 2x2 matrix
        if n == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]

        det = 0

        # Iterate over the first row for cofactor expansion
        for col in range(n):
            # Create the minor matrix by excluding the first row and current column
            minor_data = [[self.data[i][j] for j in range(n) if j != col] for i in range(1, n)]

            # Create a new matrix instance for the minor (assuming Matrix class exists)
            minor = Matrix(minor_data)

            # Calculate the cofactor and add to determinant
            det += ((-1) ** col) * self.data[0][col] * minor.determinant()

        return det

    # 6. Row Operations
    def swap_rows(self, i: int, j: int):
        """Swap two rows."""
        self.data[i], self.data[j] = self.data[j], self.data[i]

    def scale_row(self, row: int, scalar: float):
        """Multiply a row by a scalar."""
        self.data[row] = [x * scalar for x in self.data[row]]

    def add_scaled_row(self, src_row: int, target_row: int, scalar: float):
        """Add scaled version of src_row to target_row."""
        self.data[target_row] = [x + scalar * self.data[src_row][i] for i, x in enumerate(self.data[target_row])]

    # 7. General Matrix Inverse (using Gauss-Jordan elimination)
    def inverse(self):
        """Calculate the inverse using Gauss-Jordan elimination."""
        if not self.is_square():
            raise ValueError("Only square matrices can be inverted")

        n = self.rows
        # Create augmented matrix [A|I]
        augmented = [row + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(self.data)]

        # Perform Gauss-Jordan elimination
        for col in range(n):
            # Partial pivoting
            max_row = max(range(col, n), key=lambda r: abs(augmented[r][col]))
            augmented[col], augmented[max_row] = augmented[max_row], augmented[col]

            pivot = augmented[col][col]
            if abs(pivot) < 1e-10:
                raise ValueError("Matrix is singular (no inverse exists)")

            # Normalize the pivot row
            augmented[col] = [x / pivot for x in augmented[col]]

            # Eliminate other rows
            for r in range(n):
                if r != col and augmented[r][col] != 0:
                    factor = augmented[r][col]
                    augmented[r] = [x - factor * augmented[col][i] for i, x in enumerate(augmented[r])]

        # Extract the inverse from the right half
        inverse_data = [row[n:] for row in augmented]
        return Matrix(inverse_data)

    # 8. Eigenvalues/Eigenvectors (using Power Iteration)
    def power_iteration(self, max_iter: int = 100, tol: float = 1e-10):
        """Find the dominant eigenvalue and eigenvector using Power Iteration.

        Returns: (eigenvalue, eigenvector)
        """
        if not self.is_square():
            raise ValueError("Only square matrices have eigenvalues")

        n = self.rows
        # Start with a random vector
        b_k = [1.0 for _ in range(n)]

        for _ in range(max_iter):
            # Calculate the matrix-by-vector product Ab
            Ab = [sum(self.data[i][j] * b_k[j] for j in range(n)) for i in range(n)]

            # Calculate the norm
            norm = sum(x**2 for x in Ab) ** 0.5
            if norm < tol:
                break

            # Re-normalize the vector
            b_k1 = [x / norm for x in Ab]

            # Check for convergence
            if sum((b_k1[i] - b_k[i]) ** 2 for i in range(n)) ** 0.5 < tol:
                break

            b_k = b_k1

        # Rayleigh quotient for eigenvalue
        Ab = [sum(self.data[i][j] * b_k[j] for j in range(n)) for i in range(n)]
        eigenvalue = sum(Ab[i] * b_k[i] for i in range(n))

        return eigenvalue, b_k

    def eigenvalues(self, max_iter: int = 100, tol: float = 1e-6):
        """Find all eigenvalues using QR algorithm (simplified version).

        Returns: list of eigenvalues
        """
        if not self.is_square():
            raise ValueError("Only square matrices have eigenvalues")

        A = Matrix([row.copy() for row in self.data])
        n = self.rows

        for _ in range(max_iter):
            # QR decomposition (simplified Gram-Schmidt)
            Q = []
            R = [[0] * n for _ in range(n)]
            for j in range(n):
                v = [A.data[i][j] for i in range(n)]
                for k in range(j):
                    R[k][j] = sum(Q[k][i] * A.data[i][j] for i in range(n))
                    v = [v[i] - R[k][j] * Q[k][i] for i in range(n)]
                norm = sum(x**2 for x in v) ** 0.5
                Q.append([x / norm for x in v])
                R[j][j] = norm

            # Reconstruct A
            A = Matrix([[sum(R[i][k] * Q[k][j] for k in range(n)) for j in range(n)] for i in range(n)])

        # Eigenvalues are on the diagonal
        return [A.data[i][i] for i in range(n)]

    # Helper Methods
    def is_square(self):
        return self.rows == self.cols

    def _check_dimensions(self, other: "Matrix"):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")
