def matrix_multiply(A, B):
    # Get the dimensions of matrices A and B
    rows_A = len(A)
    cols_A = len(A[0]) if A else 0
    rows_B = len(B)
    cols_B = len(B[0]) if B else 0

    # Check if matrices are compatible for multiplication
    if cols_A != rows_B:
        raise ValueError("Matrices are not compatible for multiplication")

    # Initialize the result matrix C with zeros
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform matrix multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C

# Test Case 1: Correct Input and Output
A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
expected_result = [[4, 4], [10, 8]]  # Expected result of A.B
assert matrix_multiply(A, B) == expected_result, "Test Case 1 Failed"

# Test Case 2: Incompatible Matrices
A = [[1, 2], [3, 4]]
B = [[1, 2, 3]]
try:
    matrix_multiply(A, B)
    assert False, "Test Case 2 Failed: ValueError expected"
except ValueError:
    pass

# Test Case 3: Empty Matrices
A = []
B = [[1, 2], [3, 4]]
try:
    matrix_multiply(A, B)
    assert False, "Test Case 3 Failed: Error expected with empty matrix"
except ValueError:
    pass

# Test Case 4: Non-Numerical Entries
A = [["a", "b"], ["c", "d"]]
B = [[1, 2], [3, 4]]
try:
    matrix_multiply(A, B)
    assert False, "Test Case 4 Failed: Error expected with non-numerical entries"
except TypeError:
    pass

print("All tests passed!")
