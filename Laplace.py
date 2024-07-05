import numpy as np
import time


def determinant_recursive(matrix):
    # Check if the matrix is square
    rows, cols = matrix.shape
    if rows != cols:
        raise ValueError("Input matrix must be square")

    # Base case for 1x1 matrix
    if rows == 1:
        return matrix[0, 0], 0.0  # Return determinant and elapsed time 0 for base case

    determinant = 0
    sign = 1

    start_time = time.time()  # Start timing

    for col in range(cols):
        # Calculate the minor matrix by removing the current row and column
        minor_matrix = np.delete(matrix, 0, axis=0)
        minor_matrix = np.delete(minor_matrix, col, axis=1)

        # Calculate the determinant recursively
        det_minor, _ = determinant_recursive(minor_matrix)
        determinant += sign * matrix[0, col] * det_minor

        # Flip the sign for the next term
        sign = -sign

    end_time = time.time()  # End timing
    elapsed_time = end_time - start_time

    return determinant, elapsed_time


# Example usage:
A = np.array([[1, 6, 3, 3, 2],
              [5, 5, 6, 4, 9],
              [7, 6, 6, 3, 6],
              [7, 1, 8, 1, 3],
              [8, 5, 3, 2, 2],])

det_A, time_A = determinant_recursive(A)
print(f"Determinant of A:\n{det_A}")
print(f"Elapsed time for matrix {len(A)} x {len(A)}: {time_A * 1000} milli_seconds")



