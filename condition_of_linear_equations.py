import numpy as np
from inverse_matrix import inverse
from colors import bcolors
from matrix_utility import print_matrix


def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row


def condition_number(A):
    # Step 1: Calculate the max norm (infinity norm) of A
    norm_A = norm(A)

    # Step 2: Calculate the inverse of A
    A_inv = inverse(A)

    # Step 3: Calculate the max norm of the inverse of A
    norm_A_inv = norm(A_inv)

    # Step 4: Compute the condition number
    cond = norm_A * norm_A_inv

    print(bcolors.OKBLUE, "A:", bcolors.ENDC)
    print_matrix(A)

    print(bcolors.OKBLUE, "inverse of A:", bcolors.ENDC)
    print_matrix(A_inv)

    print(bcolors.OKBLUE, "Max Norm of A:", bcolors.ENDC, norm_A, "\n")

    print(bcolors.OKBLUE, "max norm of the inverse of A:", bcolors.ENDC, norm_A_inv)

    return cond


if __name__ == '__main__':
    # Date: 19.02.2024
    # Group: Eytan Stryzhack 336244959,
    # Daniel Boguslavsky 207915729
    # , Shifra Avigdor 207067125,
    # David Moalem 203387337
    # Git:https://github.com/danielbogus99/Numerical-analysis-task-1/tree/main
    # Name: Daniel Boguslavsky
    A = np.array([[-5, -6, -5],
                  [-2, -5, 0],
                  [-3, -11, -8]])
    cond = condition_number(A)

    print(bcolors.OKGREEN, "\n condition number: ", cond, bcolors.ENDC)






