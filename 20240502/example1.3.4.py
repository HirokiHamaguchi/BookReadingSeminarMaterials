import matplotlib.pyplot as plt
import numpy as np
import os

R = 6


def f1(x, y):
    return x**2 + y**2 - R**2


def quadraticPenalty(x, y):
    return np.maximum(0, f1(x, y)) ** 2


def nonSmoothPenalty(x, y):
    return np.maximum(0, f1(x, y))


def powerFunctionBarrier_withP2(x, y):
    return 1 / ((-f1(x, y)) ** 2)


def logarithmicBarrier(x, y):
    return -np.log(-f1(x, y))


def exponentialBarrier(x, y):
    return np.exp(1 / (-f1(x, y)))


X, Y = np.meshgrid(np.linspace(-10, 10, 50), np.linspace(0, 10, 50))
psi = np.linspace(0, 2 * np.pi, 100)

for name, expression in zip(
    [
        "f1",
        "quadraticPenalty",
        "nonSmoothPenalty",
        "powerFunctionBarrier_withP2",
        "logarithmicBarrier",
        "exponentialBarrier",
    ],
    [
        "$f_1(x)$",
        "$\max\{f_1(x),0\}^2$",
        "$\max\{f_1(x),0\}$",
        "$1/(-f_1(x))^2$",
        "$-\log(-f_1(x))$",
        "$\exp(1/(-f_1(x)))$",
    ],
):
    func = eval(name)
    Z = func(X, Y)
    if "Barrier" in name:
        isOutside = f1(X, Y) > -1
        Z[isOutside] = np.nan
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111, projection="3d", facecolor="w")
    ax.plot_surface(X, Y, Z, cmap="plasma")
    ax.plot(R * np.sin(psi), R * np.cos(psi), 0.1, color="gray", lw=3, zorder=100)
    ax.set_title(name + "\n" + expression, fontsize=30)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-5.5, 10)
    fig.tight_layout()
    plt.savefig(os.path.basename(__file__)[:-3] + "_" + name + ".png")
