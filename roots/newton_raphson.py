import math

epsilon = 10**-20

def newton_raphson(f, df, x0, iterations, tolerance):
    if(df(x0) == 0):
        print(f"Derivative of function is zero at x0")
        return
    x = x0
    iter_count = 0
    error = abs(f(x0) / df(x0))
    for i in range(iterations):
        if abs(df(x)) < epsilon:
            print(f"Derivate too close to zero at iteration {i}")
            break
        xn = x - (f(x) / df(x))
        error = abs(xn - x)
        if error < tolerance:
            break
        x = xn
        iter_count = i + 1
        print(f"Iteration {iter_count}: x = {x}, error = {error}")

    print(f"Root found at x = {x} after {iter_count} iterations with error = {error}")

# Define function to find the root of here
# The function must be C2 in the interval
# Check if f(x) * f''(x) > 0 for monotonus convergence
def function(x):
    return math.e**(2*x)-x-6

# Define the derivative of the function
def derivative(x):
    return 2*math.e**(2*x) - 1


if __name__ == "__main__":
    # Define the parameters for the bisection method
    x0 = 1.5
    # Use a high number of iterations if it is not known
    iterations = 100
    tolerance = 10**-5
    # Call the bisection method
    newton_raphson(function, derivative, x0, iterations, tolerance)