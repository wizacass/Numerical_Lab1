import math
import numpy as np
import matplotlib.pyplot as plt
import helpers as h
import methods as m

precision = 6
scan_accuracy = 2
scan_step = 10. ** -scan_accuracy

fx_coeffs = [-1.33, -2.93, 18.22, 9.70, -8.15]

gx_min = -10
gx_max = 10


# f(x) = -1.33x^4 - 2.93x^3 + 18.22x^2 + 9.70x - 8.15
def func_f(x):
    result = 0
    n = len(fx_coeffs) - 1
    for a in fx_coeffs:
        result = round(result + a * (x ** n), precision)
        n = n - 1
    return float(round(result, precision))


def func_g(x):
    return x * math.cos(x) ** 2 - (x / 2) ** 2


def rough_estimate(list):
    data = h.list_abs(list)
    m = max(data[1:])
    x = 1 + (m / list[0])
    return abs(x)


def accurate_estimate(list):
    data = h.inverted(list) if (list[0] < 0) else list
    n = len(data) - 1
    B = abs(min(data[1:]))
    k = n - h.max_negative_index(data[::-1])
    root = 1. ** k
    return 1 + (B / data[0]) ** root


def solve(x_min, x_max, y_min, y_max, func, header, show_graph=False):
    approx_roots = h.find_roots(x_min, x_max, scan_step, scan_accuracy, func)
    simple_roots = m.simple_iteration(approx_roots, scan_step, precision, func)
    secant_roots = m.secant(approx_roots, scan_step, precision, func)
    scanned_roots = m.scanning(
        approx_roots, scan_step, scan_accuracy, precision, func)

    if show_graph:
        plot(header, x_min, x_max, y_min, y_max, scanned_roots, func)

    print(f"Solving {header}")
    print(f"Accurate estimate:      [{x_min} : {x_max}]")
    print(f"Approximate roots:      {approx_roots}")
    print(f"Simple iteration roots: {simple_roots}")
    print(f"Secant roots:           {secant_roots}")
    print(f"Scanned roots:          {scanned_roots}")
    print()


def plot(header, x_min, x_max, y_min, y_max, roots, func):
    data = []
    counts = []
    zeros = []
    i = round(x_min, scan_accuracy)
    while i < round(x_max, scan_accuracy):
        data.append(func(i))
        counts.append(i)
        i += scan_step

    for i in roots:
        zeros.append(0)

    plt.axis([x_min, x_max, y_min, y_max])
    plt.plot(counts, data)
    plt.title(header)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(roots, zeros, 'ro')
    plt.grid(True)
    plt.show()


def main():
    coeffs = fx_coeffs
    r = rough_estimate(coeffs)

    r_pos = accurate_estimate(coeffs)
    r_neg = accurate_estimate(h.inverted(coeffs))
    fx_min = round(-min(r, r_neg), scan_accuracy)
    fx_max = round(min(r, r_pos), scan_accuracy)

    solve(fx_min, fx_max, -750, 250, func_f, "f(x)")
    solve(gx_min, gx_max, -20, 5, func_g, "g(x)")


main()