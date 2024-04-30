import matplotlib.pyplot as plt
import numpy as np
import os


if True:

    def f(x):
        return 0.75 * x**2 + 0.5 * x + 0.5

    def fPrime(x):
        return 1.5 * x + 0.5

    x = np.linspace(-5, 5, 100)
    y = f(x)
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111)
    plt.plot(x, y)
    plt.plot(x, fPrime(-2) * (x + 2) + f(-2), "g")
    plt.plot(x, fPrime(+3) * (x - 3) + f(+3), "g")
    plt.annotate(
        "y",
        (-2, f(-2)),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=20,
    )
    plt.annotate(
        "x",
        (+3, f(+3)),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=20,
    )
    plt.plot(-2, f(-2), "ro")
    plt.plot(+3, f(+3), "ro")
    ax.arrow(2, -3, 0, 3, head_width=0.3, head_length=0.3, fc="g", ec="g")
    plt.annotate(
        r"$\nabla f(x) - \nabla f(y)$",
        (2.75, -2.25),
        textcoords="offset points",
        xytext=(10, 10),
        ha="center",
        fontsize=20,
    )
    plt.xlim(-4, 4)
    plt.ylim(-5, 15)
    plt.title(r"$\langle \nabla f(x) - \nabla f(y), x - y \rangle \geq 0$", fontsize=30)

    plt.savefig(os.path.basename(__file__)[:-3] + "_1d" + ".png")

if True:
    A = np.array([[1, 0.5], [0.5, 1]])
    a = np.array([1, 2])
    alpha = 1

    def f(x):
        return alpha + np.dot(a, x) + 0.5 * np.dot(A @ x, x)

    def fPrime(x):
        return a + A @ x

    X, Y = np.meshgrid(np.linspace(-6, 4, 100), np.linspace(-5, 4, 100))
    XYs = np.concatenate([X.reshape(-1, 1), Y.reshape(-1, 1)], axis=1)
    Z = np.array([f(xy) for xy in XYs]).reshape(X.shape)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, aspect="equal")
    plt.contour(X, Y, Z, 30)
    p1 = np.array([-4, -2])
    p2 = np.array([1, 2])
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], "b")
    p1Prime = 0.2 * fPrime(p1) + p1
    p2Prime = 0.2 * fPrime(p2) + p2
    plt.plot([p1[0], p1Prime[0]], [p1[1], p1Prime[1]], "r")
    plt.plot([p2[0], p2Prime[0]], [p2[1], p2Prime[1]], "r")

    plt.title(r"$\alpha + \langle a, x \rangle + \langle A x, x \rangle$", fontsize=30)
    plt.savefig(os.path.basename(__file__)[:-3] + "_2d" + ".png")
