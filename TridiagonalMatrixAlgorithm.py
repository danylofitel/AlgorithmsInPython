__author__ = 'Danylo'

import math


def TMA(a, b, c, f):
    a, b, c, f = map(lambda k_list: map(float, k_list), (a, b, c, f))

    alpha = [0]
    beta = [0]
    n = len(f)
    x = [0] * n

    for i in range(n - 1):
        alpha.append(-b[i] / (a[i] * alpha[i] + c[i]))
        beta.append((f[i] - a[i] * beta[i]) / (a[i] * alpha[i] + c[i]))

    x[n - 1] = (f[n - 1] - a[n - 2] * beta[n - 1]) / (c[n - 1] + a[n - 2] * alpha[n - 1])

    for i in reversed(range(n - 1)):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]

    return x


def c_test(x, t, v, d):
    return math.exp(-((x - 0.2 - v * t) ** 2) / (d * (4 * t + 1))) / math.sqrt(4 * t + 1)


def characteristics(n, v, tau, d, h):
    t_0 = 0
    c_prev = [c_test(x, t_0, v, d) for x in range(n)]

    a = [-tau * d / (h ** 2) for x in range(n)]
    b = [1 + 2 * tau * d / (h ** 2) for x in range(n)]
    c = [-tau * d / (h * h) for x in range(n)]

    return TMA(a, b, c, c_prev)

n = 3
v = 1
tau = 1
d = 1
h = 1

print characteristics(n, v, tau, d, h)