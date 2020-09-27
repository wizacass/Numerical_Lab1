import helpers as h


def simple_iteration(approx_roots, step, desired_accuracy, func):
    eps = 10 ** -desired_accuracy
    accurate_roots = []
    for root in approx_roots:
        itmax, it = 5, 0
        xn = root
        prec = abs(func(xn))
        while prec > eps and it < itmax:
            it = it + 1
            #xn = func(xn) / step + xn
            xn = func(xn) + xn
            prec = abs(func(xn))

        accurate_roots.append(round(xn, desired_accuracy))

    return accurate_roots


def secant(approx_roots, step, desired_accuracy, func):
    accurate_roots = []
    for root in approx_roots:
        df = (func(root) -
              func(root - step)) / step
        x = root - (df ** -1) * func(root)
        x = round(x, desired_accuracy)
        accurate_roots.append(x)

    return accurate_roots


def scanning(approx_roots, step, accuracy, desired_accuracy, func):
    while accuracy < desired_accuracy:
        accurate_roots = []
        accuracy = accuracy + 1
        step = step * 0.1
        for root in approx_roots:
            x_min = root
            x_max = root + (step * 10)
            roots = h.find_roots(x_min, x_max, step, accuracy, func)
            accurate_roots.extend(roots)
        approx_roots = accurate_roots

    return approx_roots
