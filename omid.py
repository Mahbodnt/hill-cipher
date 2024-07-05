import numpy as np
import time

def cofactor_matrix(a, m, n):
    # Return the (n-1) x (n-1) cofactor matrix of a after removing row m and column n
    return np.delete(np.delete(a, m, axis=0), n, axis=1)

def determinant_recursive(a):
    n = a.shape[0]
    if n == 1:
        return a[0, 0]
    elif n == 2:
        return a[0, 0] * a[1, 1] - a[1, 0] * a[0, 1]
    else:
        det = 0
        for j in range(n):
            sign = (-1) ** j
            sub_det = determinant_recursive(cofactor_matrix(a, 0, j))
            det += sign * a[0, j] * sub_det
        return det

def measure_time_complexity(n):
    # Generate a random n x n matrix
    a = np.random.randint(1, 10, size=(n, n))

    # Measure the time taken to compute the determinant
    start_time = time.time()
    determinant_recursive(a)
    end_time = time.time()

    return end_time - start_time

def main():
    # Example matrix
    matrix_data =\
            [[1, 6, 3, 3, 2],
              [5, 5, 6, 4, 9],
              [7, 6, 6, 3, 6],
              [7, 1, 8, 1, 3],
              [8, 5, 3, 2, 2],]
    a = np.array(matrix_data)

    det = determinant_recursive(a)

    print(f"Determinant of the matrix:\n{a}\nis {det}")

    # Measure time complexity for various matrix sizes



    time_taken = measure_time_complexity(len(matrix_data))
    print(f"Time taken for {len(matrix_data)}x{len(matrix_data)} matrix: {time_taken * 1000:.6f} milli_seconds")

if __name__ == "__main__":
    main()
