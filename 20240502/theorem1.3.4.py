import matplotlib.pyplot as plt
import numpy as np
import os

R = 6


def f0_1(x):
    return (x - 2) ** 2


def f0_2(x):
    return (x - 8) ** 2


def f1(x):
    return x**2 - R**2


def F(x):
    return 1 / (-f1(x))


def minimum(x, fx):
    minXIndex = np.argmin(fx)
    return x[minXIndex], fx[minXIndex]


x = np.linspace(-5.8, 5.8, 1000)

for f0, expression in zip([f0_1, f0_2], ["$f_0(x)=(x-2)^2$", "$f_0(x)=(x-8)^2$"]):
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(111, facecolor="w")
    for k in range(7):
        tk = 0.001 * (1 + k)
        y = f0(x) + (1 / tk) * F(x)
        ax.plot(x, y, label=f"$t_{k+1} = {tk}$")
        ax.plot(*minimum(x, y), "r*", markersize=7)
    x2 = np.linspace(-R, R, 1000)
    ax.plot(x2, f0(x2), label=expression, linestyle="--", color="k")
    ax.plot([-R, -R], [f0(-R), 100], linestyle="--", color="k")
    ax.plot([R, R], [f0(R), 100], linestyle="--", color="k")
    ax.plot(*minimum(x2, f0(x2)), "r*", markersize=7)
    ax.legend()
    ax.set_ylim(0, 100)
    ax.set_title(
        "Barrier Function Method"
        + "\n"
        + expression
        + "\n"
        + "$f_1(x)=x^2-6^2, F(x)=1/((-f_1(x))^2)$",
        fontsize=30,
    )
    plt.tight_layout()
    plt.savefig(os.path.basename(__file__)[:-3] + f"_{expression[8:15]}.png")
