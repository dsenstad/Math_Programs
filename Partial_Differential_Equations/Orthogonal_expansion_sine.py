import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
"""
Author: David Senstad

As we all know, the set of functions f_n = sin(nx) forms an orthogonal set of functions on [0,π]. This program lets you define any
function you want under def f_x and then calculate its Fourier sine series coefficients c_n up to N terms. It will then graph the original
function with the approximation on top.
"""

# Number of terms you want the function to be approximated with
N = 10

#This is our origianl function
def f_x(x):
    return (8 * x) * (math.pi - x) * np.exp(-(x**2))

# Integrand of our c_n coefficients
def integrand(x, n):
    return f_x(x) * math.sin(n * x)

# Uses quad to numerically approximate the Fourier sine series coefficients c_n
def calc_coefficients(n):
    return (2/math.pi) * quad(integrand, 0, math.pi, args=n)[0]

#Creates list of Fourier sine series coefficients and calculates them starting at c_1 up to c_N
coefficients = []
while len(coefficients) < N:
    coefficients.append(calc_coefficients(len(coefficients) + 1))

"""
def fourier_approx(x, coeffs):
    total = 0.0
    for n, c_n in enumerate(coeffs, start=1):
        total += c_n * np.sin(n * x)
    return total

# Calculates the mean-square error of the approximation.
def mse_integrand(x, coeffs):
    return (f_x(x) - fourier_approx(x, coeffs))**2

def mean_square_error(coeffs):
    return quad(mse_integrand, 0, np.pi, args=(coeffs,))[0]

print(f"Mean-square error in the Fourier sine series for {N} terms: {mean_square_error(coefficients)}")

#Create x-values on our interval
x_vals = np.linspace(0, math.pi, 500)
y_original = f_x(x_vals)
y_approx = fourier_approx(x_vals, coefficients)

#Plot both
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_original, color="k", label="Original function")
plt.plot(x_vals, y_approx, color = "r", label=f"Fourier sine series approximation (N={N})")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Original Function vs Fourier Sine Series Approximation")
plt.legend()
plt.grid(True)
plt.show()
"""