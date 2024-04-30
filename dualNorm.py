# draw ellipses of dual norm

import matplotlib.pyplot as plt
import numpy as np
import os

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 - 0.5 * X * Y + Y**2

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_aspect("equal")
ax.contour(X, Y, Z, levels=[1], colors="k")

# g
ax.arrow(0, 0, 1.5, 0.75, head_width=0.1, head_length=0.1, fc="r", ec="r")

# maximize 2x+y subject to x^2-0.5xy+y^2=1
ax.arrow(
    0,
    0,
    0.9 * 0.948683,
    0.9 * 0.632456,
    head_width=0.1,
    head_length=0.1,
    fc="g",
    ec="g",
)

ax.set_title(
    "$||g||_* = \max_{x \in \mathbb{R}^n} \{\\langle g, x \\rangle : ||x||_A \leq 1\}$",
    fontsize=30,
)

plt.tight_layout()
plt.savefig(os.path.basename(__file__).split(".")[0] + ".png")
