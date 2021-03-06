def read_matrix(string_to_split):
    rows, cols = [int(x) for x in string_to_split.split()]
    main_matrix_construction = []

    for _ in range(rows):
        main_matrix_construction.append(list(x for x in input().split(' ')))

    return main_matrix_construction


def is_command_valid(command, valid_command, valid_length):
    command_length = len(command.split(' '))

    if not command.startswith(valid_command):
        return False
    elif not command_length == valid_length:
        return False

    return command


def are_indices_valid(matrix, command):
    rows_range = len(matrix)
    cols_range = len(matrix[0])
    swap, *coordinates = command.split(' ')
    row1, col1, row2, col2 = [int(x) for x in coordinates]

    if row1 and row2 not in range(rows_range) and col1 and col2 not in range(cols_range):
        return False
    else:
        return True


def matrix_swapping(matrix, command):
    swap, *coordinates = command.split(' ')
    row1, col1, row2, col2 = [int(x) for x in coordinates]
    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    return matrix


def print_current_swap_result(matrix):
    for current_row in range(len(matrix)):
        row = []
        for current_column in range(len(matrix[current_row])):
            row.append(matrix[current_row][current_column])
        print(' '.join(str(x) for x in row))


def main(matrix, command):
    while not command == "END":

        if not is_command_valid(command, VALID_COMMAND, VALID_COMMAND_LENGTH):
            print('Invalid input!')

        elif not are_indices_valid(matrix, command):
            print('Invalid input!')

        else:
            current_swap = matrix_swapping(matrix, command)
            print_current_swap_result(matrix)
            matrix = current_swap
        command = input()

    return command


VALID_COMMAND = 'swap'
VALID_COMMAND_LENGTH = len(['swap', 'row1', 'col1', 'row2', 'col2'])

command = main(matrix=read_matrix(input()), command=input())
