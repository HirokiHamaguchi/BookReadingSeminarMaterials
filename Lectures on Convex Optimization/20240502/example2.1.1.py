import matplotlib.pyplot as plt
import numpy as np
import os

x = np.linspace(-10, 10, 100)

y1 = (x**2) / (1 - np.abs(x))
y2 = np.abs(x) - np.log(1 + np.abs(x))

for y, name, expression in zip(
    [y1, y2], ["2", "3"], ["$x^2 / (1 - |x|)$", "$|x| - \log(1 + |x|)$"]
):
    plt.plot(x, y)
    plt.title(expression, fontsize=30)
    plt.savefig(os.path.basename(__file__)[:-3] + f"_{name}.png")
    plt.close()

X, Y = np.meshgrid(np.linspace(-10, 10, 30), np.linspace(-10, 10, 30))
Z = np.log(np.exp(X) + np.exp(Y))
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="plasma")
ax.set_title("$\\log\\left(\\Sigma_i \\exp(x_i)\\right)$", fontsize=30)
ax.view_init(25, -115)
plt.tight_layout()
plt.savefig(os.path.basename(__file__)[:-3] + "_3d.png")
