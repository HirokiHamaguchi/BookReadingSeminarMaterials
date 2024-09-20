import matplotlib.pyplot as plt
import numpy as np
import os


def f(x):
    return 0.75 * x**2 + 0.5 * x + 4


def fPrime(x):
    return 1.5 * x + 0.5


x = np.linspace(-5, 5, 100)
y = f(x)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111)

for idx in np.linspace(5, 95, 25):
    x0 = x[int(idx)]
    plt.plot([x0, x0], [fPrime(1) * x0, f(x0)], "tab:orange")

plt.plot(x, y)
plt.plot(x, fPrime(1) * (x - 1) + f(1), "g--")
plt.plot(x, fPrime(1) * x, "g-")
plt.plot(1, f(1), "ro")

ax.annotate(r"$f(x)$", xy=(1.5, 9), fontsize=20, color="tab:blue")
ax.annotate(
    r"$\langle \nabla f(x_0), y \rangle$", xy=(2.5, 3.5), fontsize=20, color="green"
)
ax.annotate(
    r"$\phi(y) = f(y) + \langle -\nabla f(x_0), y \rangle$",
    xy=(0.3, -2),
    fontsize=20,
    color="tab:orange",
)
ax.annotate(
    "$x_0$",
    xy=(0.9, f(1) + 0.7),
    fontsize=20,
    color="red",
)

ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.xaxis.set_ticks_position("bottom")
ax.spines["bottom"].set_position(("data", 0))
ax.yaxis.set_ticks_position("left")
ax.spines["left"].set_position(("data", 0))

plt.xlim(-4, 4)
plt.ylim(-5, 15)
plt.title(r"$f(y) \geq f(x_0) + \langle \nabla f(x_0), y-x_0 \rangle$", fontsize=30)

plt.tight_layout()
plt.savefig(os.path.basename(__file__).replace(".py", ".png"))
