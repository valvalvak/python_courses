def read_matrix(rows):
    matrix_build = []

    for i in range(rows):
        matrix_build.append([int(x) for x in input().split(' ')])

    return matrix_build


def get_sum_sub_matrix(matrix, row_index, column_index, size):
    sum_result = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            sum_result += matrix[r][c]
    return sum_result


def get_most_left_square_matrix(matrix, sub_matrix_size):
    best_row_index = 0
    best_column_index = 0
    best_sum = get_sum_sub_matrix(matrix, 0, 0, sub_matrix_size)

    for row_index in range(len(matrix) - sub_matrix_size + 1):
        for col_index in range(len(matrix[row_index]) - sub_matrix_size + 1):
            current_sum = get_sum_sub_matrix(matrix, row_index, col_index, sub_matrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = col_index
    return (best_row_index, best_column_index)


def print_result(coordinates, size):
    (row_index, col_index) = coordinates
    print(f'Sum = {get_sum_sub_matrix(matrix, row_index, col_index, size)}')
    
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))


SUB_MATRIX_SIZE = 3

rows, columns = [int(x) for x in input().split(" ")]
matrix = read_matrix(rows)
sub_matrix = get_most_left_square_matrix(matrix, SUB_MATRIX_SIZE)
print_result(sub_matrix, SUB_MATRIX_SIZE)
