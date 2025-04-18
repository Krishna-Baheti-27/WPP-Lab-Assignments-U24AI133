import numpy as np
import matplotlib.pyplot as plt
import random

def f(x):
    return x**3 - 4*x - 9  # Example polynomial function

def find_initial_interval():
    while True:
        a, b = random.uniform(-10, 10), random.uniform(-10, 10)
        if a > b:
            a, b = b, a
        if f(a) * f(b) < 0:
            return a, b

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    iterations = []
    for _ in range(max_iter):
        c = (a + b) / 2.0
        iterations.append(c)
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            break
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return np.array(iterations)

a, b = find_initial_interval()
root_iterations = bisection_method(f, a, b)

x_vals = np.linspace(-5, 5, 400)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label='f(x)')
plt.axhline(0, color='black', linewidth=0.5)
plt.scatter(root_iterations, f(root_iterations), color='red', marker='o', label='Iterations')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Bisection Method Root Finding Process')
plt.show()
