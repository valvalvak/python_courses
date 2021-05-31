def read_matrix(rows):
    matrix_build = []

    for i in range(rows):
        matrix_build.append(list(input().split(" ")))

    return matrix_build


def sub_matrix_counter(matrix, size):
    counter = 0
    last_symbol = matrix[0][0]
    matrix_size = len(matrix)
    for row_index in range(matrix_size - size + 1):
        for col_index in range(matrix_size - size + 1):
            if last_symbol == matrix[row_index][col_index + 1] and matrix[row_index + 1]:
                counter += 1
            current_symbol = matrix[row][col]
    return counter


SUB_MATRIX_SQUARE_SIZE = 2

row, col = [int(x) for x in input().split()]

matrix = read_matrix(row)

counter_result = sub_matrix_counter(matrix, SUB_MATRIX_SQUARE_SIZE)

print(counter_result)
