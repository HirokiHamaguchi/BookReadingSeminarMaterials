import os
from tkinter import font

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

L = 1


def f(k, x):
    term = x[0] ** 2
    for i in range(k - 1):
        term += (x[i] - x[i + 1]) ** 2
    term += x[k - 1] ** 2
    term *= 1 / 2
    term -= x[0]
    return (L / 4) * term


def calc_A(n, k):
    A = np.zeros((n, n))
    for i in range(k):
        A[i, i] = 2
        if 0 < i:
            A[i, i - 1] = -1
        if i < k - 1:
            A[i, i + 1] = -1
    print(A)
    return A


def grad_f(n, k, x):
    e0 = np.zeros(n)
    e0[0] = 1
    return calc_A(n, k) @ x - e0


def bestSolution(n, k):
    x = np.zeros(n)
    for i in range(k):
        x[i] = 1 - (i + 1) / (k + 1)
    return x


def vis():
    n = 2
    k = 2
    X, Y = np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100))
    Z = np.zeros(X.shape)
    for i in range(100):
        for j in range(100):
            Z[i, j] = f(k, np.array([X[i, j], Y[i, j]]))
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d", computed_zorder=False)
    bestX, bestY = bestSolution(n, k)
    ax.plot_surface(X, Y, Z, cmap="plasma")
    ax.scatter(
        bestX,
        bestY,
        f(k, np.array([bestX, bestY])),
        c="r",
        marker="x",
        s=30,
        depthshade=False,
    )
    ax.set_title(
        "$f(x) = \\frac{L}{4} \\left( \\frac{1}{2} \\left[ x_1^2 + (x_1 - x_2)^2 + x_2^2 \\right] - x_1 \\right)$",
        fontsize=30,
    )
    plt.tight_layout()
    plt.savefig(os.path.basename(__file__)[:-3] + "_vis.png")
    plt.close()


def main():
    n = 12
    answers = np.zeros((n + 1, n))
    for k in range(n + 1):
        answers[k] = bestSolution(n, k)
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111)
    plt.imshow(answers.T)
    plt.colorbar()
    plt.xticks(np.arange(0, n, 1))
    plt.yticks(np.arange(0, n, 1))
    plt.tick_params(
        axis="both",
        which="major",
        labelsize=10,
        bottom=False,
        top=False,
        labeltop=True,
        labelbottom=False,
    )
    secax = ax.secondary_xaxis("top")
    secax.set_xlabel("$k$-th iteration", fontsize=20)
    plt.ylabel("index $i$", fontsize=20)
    plt.title(
        "Best solutions $\\overline{x}_k$ for $f_k(x)$ with $n=12$\n"
        + "$f_k(x) = \\frac{L}{4} \\left( \\frac{1}{2} \\left[ x_1^2 + \\Sigma_{i=1}^{k-1}(x_i - x_{i+1})^2 + x_k^2 \\right] - x_1 \\right)$",
        fontsize=20,
    )
    plt.tight_layout()
    plt.savefig(os.path.basename(__file__)[:-3] + "_main.png")


if __name__ == "__main__":
    vis()
    main()
