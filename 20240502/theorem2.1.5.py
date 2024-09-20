import matplotlib.pyplot as plt
import numpy as np
import os


def f(x):
    return 0.05 * (x**4 + 12 * x**2)


def fPrime(x):
    return 0.05 * (4 * x**3 + 24 * x)


def fPrimePrime(x):
    return 0.05 * (12 * x**2 + 24)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect("equal")
X = np.linspace(-2, 2, 100)
Y = f(X)
L = 4
assert np.all(0 <= fPrimePrime(X)) and np.all(fPrimePrime(X) <= L)

plt.plot(X, Y)
plt.xlim(-2, 2)
plt.ylim(-1, 3)

x = 0.4
fx = f(x)
fpx = fPrime(x)
y = 1.5
fy = f(y)
fpy = fPrime(y)

plt.plot(
    X,
    fx + fpx * (X - x) + (L / 2) * (X - x) ** 2,
    "r--",
    label="$f(x)+\\langle\\nabla f(x),y-x \\rangle+\\frac{L}{2}||x-y||^2$",
)
plt.plot(
    X,
    fx + fpx * (X - x) + (1 / (2 * L)) * (fpx - fPrime(X)) ** 2,
    "g--",
    label="$f(x)+\\langle\\nabla f(x),y-x \\rangle+\\frac{1}{2L}||\\nabla f(x)-\\nabla f(y)||^2$",
)
plt.plot(x, fx, "ro")
plt.plot(y, fy, "ro")
ax.annotate(
    "$x$",
    (x, fx),
    textcoords="offset points",
    xytext=(0, 10),
    ha="center",
    fontsize=20,
    color="r",
)
ax.annotate(
    "$y$",
    (y, fy),
    textcoords="offset points",
    xytext=(0, 10),
    ha="center",
    fontsize=20,
    color="r",
)

plt.legend(fontsize=10)
plt.title("$f(x)=\\frac{1}{20}(x^4+12x^2), L=4$", fontsize=30)
plt.tight_layout()
plt.savefig(os.path.basename(__file__).replace(".py", ".png"))
