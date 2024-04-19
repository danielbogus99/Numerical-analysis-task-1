import numpy as np


def trapezoidal_rule(func, a, b, n):
    """
    Approximates the integral of a function using the trapezoidal rule.

    Parameters:
        func (function): The function to integrate.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): The number of subintervals to use for approximation.

    Returns:
        float: The approximate value of the integral.
    """
    # Calculate the width of each subinterval
    h = (b - a) / n

    # Calculate the endpoints and the function values at these endpoints
    x = np.linspace(a, b, n + 1)
    y = func(x)

    # Use the trapezoidal rule formula
    integral = h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

    return integral


# Define the function to integrate (in this case, sin(x))
def func(x):
    return np.sin(x)


# Define the limits of integration
a = 0
b = np.pi

# Define the number of subintervals
n = 4

# Calculate the integral using the trapezoidal rule
approx_integral = trapezoidal_rule(func, a, b, n)
print("Approximate value of the integral using the trapezoidal rule:", approx_integral)
