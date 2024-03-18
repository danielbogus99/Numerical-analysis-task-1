import numpy as np
from numpy.linalg import norm
from colors import bcolors


def jacobi_iterative(A, b, X0, TOL=1e-16, N=500):
    n = len(A)
    k = 1

    print( "Iteration" + "\t\t\t".join([" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(A) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")

    while k <= N:
        x = np.zeros(n, dtype=np.double)
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * X0[j]
            x[i] = (b[i] - sigma) / A[i][i]

        print("{:<15} ".format(k) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if norm(x - X0, np.inf) < TOL:
            return tuple(x)

        k += 1
        X0 = x.copy()

    print("Maximum number of iterations exceeded")
    return "not found"


if __name__ == "__main__":
    # Git:https://github.com/danielbogus99/Numerical-analysis-task-1
    # Date: 18.03.2024
    # Group: Eytan Stryzhack 336244959,
    # Daniel Boguslavsky 207915729
    # , Shifra Avigdor 207067125,
    # David Moalem 203387337

    # Name: Daniel Boguslavsky
    A = np.array([[3, -1, 1],
                  [3, 4, -1],
                  [2, 6, -7]])
    b = np.array([1, -1, -3])

    x = np.zeros_like(b, dtype=np.double)
    solution = jacobi_iterative(A, b, x)

    print(bcolors.OKBLUE,"\nApproximate solution:", solution)