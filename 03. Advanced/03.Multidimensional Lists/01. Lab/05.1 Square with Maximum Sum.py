def build_matrix(rows):
    main_matrix = []

    for i in range(rows):
        main_matrix.append([int(x) for x in input().split(", ")])

    return main_matrix


def get_all_square_in_matrix(matrix):
    squares_in_matrix = []
    for row in range(len(matrix) - 1):
        squares_in_matrix.append([])
        for col in range(row, len(matrix[row]) - 1):
            squares_in_matrix[row].append(matrix[row][col])
            squares_in_matrix[row].append(matrix[row + 1][col + 1])
    return squares_in_matrix


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
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(' '.join(str(x) for x in row))
    print(get_sum_sub_matrix(matrix, row_index, col_index, size))


SUB_MATRIX_SIZE = 2

rows, columns = [int(x) for x in input().split(", ")]
matrix = build_matrix(rows)
sub_matrix = get_most_left_square_matrix(matrix, SUB_MATRIX_SIZE)
print_result(sub_matrix, SUB_MATRIX_SIZE)
