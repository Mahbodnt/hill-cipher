
import numpy as np
import time


def determinant_gauss_jordan(matrix, threshold=1e-10):
    # Check if the matrix is square
    rows, cols = matrix.shape
    if rows != cols:
        raise ValueError("Input matrix must be square")

    # Make a copy of the matrix with float64 dtype
    mat = matrix.astype(np.float64)

    # Start timing
    start_time = time.time()

    # Apply Gauss-Jordan elimination to the matrix
    for i in range(rows):
        # Find the pivot row
        max_row = i
        for j in range(i + 1, rows):
            if abs(mat[j, i]) > abs(mat[max_row, i]):
                max_row = j

        # Swap the maximum row with the current row (if needed)
        if max_row != i:
            mat[[i, max_row]] = mat[[max_row, i]]

        # Check if the matrix is singular
        if abs(mat[i, i]) < threshold:
            return 0, 0.0  # If matrix is singular (or close to), determinant is 0

        # Make all the entries below this pivot 0
        for j in range(i + 1, rows):
            ratio = mat[j, i] / mat[i, i]
            mat[j, i:] -= ratio * mat[i, i:]

    # End timing
    end_time = time.time()

    # Calculate elapsed time
    elapsed_time = end_time - start_time

    # Calculate determinant (product of diagonal elements)
    determinant = np.prod(np.diag(mat))

    # Convert determinant to int if possible
    determinant_int = int(round(determinant))

    return determinant_int, elapsed_time


# Example usage:
A = np.array([[1, 6, 3, 3, 2],
              [5, 5, 6, 4, 9],
              [7, 6, 6, 3, 6],
              [7, 1, 8, 1, 3],
              [8, 5, 3, 2, 2],])

det_A, time_A = determinant_gauss_jordan(A)
print(f"Determinant of A:\n{det_A}")
print(f"Elapsed time for matrix {len(A)} x {len(A)}: {time_A * 1000} milli_seconds")
