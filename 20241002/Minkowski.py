import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 3, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)


def calcZ(x, y):
    # Q: (x-0.5)^2 + 2y^2 <= 1
    # find 1/t such that (tx, ty) is on the boundary of Q
    # (tx-0.5)^2 + 2(ty)^2 = 1
    # t^2(x^2+2y^2) - tx - 0.75 = 0
    # t = (x +/- sqrt(4x^2+6y^2))/2(x^2+2y^2)
    assert np.all(
        (x + np.sqrt(4 * x**2 + 6 * y**2)) * (x - np.sqrt(4 * x**2 + 6 * y**2)) <= 0
    )
    t = np.maximum(
        x + np.sqrt(4 * x**2 + 6 * y**2), x - np.sqrt(4 * x**2 + 6 * y**2)
    ) / (2 * (x**2 + 2 * y**2))
    Z = 1 / t
    return Z


Z = calcZ(X, Y)

plt.figure(figsize=(10, 6))
plt.imshow(Z, extent=[-2, 3, -2, 2], origin="lower", cmap="viridis")

# Plot the ellipse
theta = np.linspace(0, 2 * np.pi, 100)
x_ellipse = np.cos(theta) + 0.5
y_ellipse = np.sin(theta) / np.sqrt(2)
plt.plot(
    x_ellipse, y_ellipse, label="$\partial Q$: $(x-0.5)^2 + 2y^2 = 1$", color="red"
)

plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.xlabel("x")
plt.ylabel("y")
plt.gca().set_aspect("equal", adjustable="box")
plt.colorbar()
plt.legend()

plt.title(
    "Minkowski function of Q: $1/t$ where $t=\\frac{x \pm \sqrt{4x^2+6y^2}}{2(x^2+2y^2)}$",
    fontsize=20,
)

# plt.show()
plt.savefig("20241002/Minkowski.pdf")
