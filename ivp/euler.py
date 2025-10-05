import math

def euler_method(f, interval, y_0, h, M):
    Y = [0] * (M+1)
    T = [0] * (M+1)
    Y[0] = y_0
    T[0] = interval[0]
    for i in range(M):
        T[i+1] = T[i] + h
        k1 = h * f(T[i], Y[i])
        Y[i+1] = Y[i] + k1
    return T, Y

# Define the function to be used in the Euler method
def function(t, y):
    return y - 0.5*(math.e**(t/2))*math.sin(5*t) + 5*(math.e**(t/2))*math.cos(5*t)

if __name__ == "__main__":
    # Define the parameters for the euler method
    interval = [0, 1]
    y0 = 0
    # Remember that steps = (b - a) / h
    h = 0.1
    steps = 10
    # Call the euler method
    T, Y = euler_method(function, interval, y0, h, steps)
    # Print the results
    for i in range(len(T)):
        print(f"T[{i}] = {T[i]}, Y[{i}] = {Y[i]}")