import numpy as np
import matplotlib.pyplot as plt

# draw 3d plot of f(x,y)=gamma max(x,y) + mu/2 norm((x,y))^2

gamma = 8
mu = 1

x = np.linspace(-10, 0, 1000)
y = np.linspace(-10, 0, 1000)
X, Y = np.meshgrid(x, y)
Z1 = gamma * X + mu / 2 * (X**2 + Y**2)
Z2 = gamma * np.maximum(X, Y) + mu / 2 * (X**2 + Y**2)


for k in range(1, 2 + 1):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    if k == 1:
        ax.plot_surface(X, Y, Z1, cmap="viridis")
    else:
        ax.plot_surface(X, Y, Z2, cmap="viridis")

    ax.set_xlabel("$x^{(1)}$")
    ax.set_ylabel("$x^{(2)}$")

    if k == 1:
        ax.set_zlabel("$f_1(x)$")
    else:
        ax.set_zlabel("$f_2(x)$")

    ax.set_title("$\gamma = 8, \mu = 1$")

    ax.view_init(30, 30)
    plt.savefig(f"20241030/fk_{k}_1.png", dpi=300, bbox_inches="tight")

    ax.view_init(0, 0)
    plt.savefig(f"20241030/fk_{k}_2.png", dpi=300, bbox_inches="tight")

    plt.close()

# fig = plt.figure()
# ax = fig.add_subplot()
# ax.imshow(Z, cmap="viridis", extent=[-10, 0, -10, 0], origin="lower")
# # add star at (-gamma/2mu, -gamma/2mu)
# ax.plot(-gamma / (2 * mu), -gamma / (2 * mu), "r*", markersize=10)
# ax.plot([0, -gamma / (2 * mu)], [0, -gamma / (2 * mu)], "b--")
# ax.text(-gamma / (4 * mu), -gamma / (4 * mu), "   $R_k$", fontsize=12, color="b")
# ax.plot(-5, -5, "yo", markersize=5)
# ax.arrow(
#     -5,
#     -5,
#     mu * (-5) + gamma - 0.5,
#     0,
#     head_width=0.5,
#     head_length=0.5,
#     fc="y",
#     ec="y",
# )
# ax.arrow(
#     -5,
#     -5,
#     0,
#     mu * (-5) + gamma - 0.5,
#     head_width=0.5,
#     head_length=0.5,
#     fc="y",
#     ec="y",
# )
# ax.plot([-5, -5 + mu * (-5) + gamma], [-5 + mu * (-5) + gamma, -5], "y-")
# ax.set_xlabel("$x^{(1)}$")
# ax.set_ylabel("$x^{(2)}$")
# ax.set_title("$\gamma = 8, \mu = 1$")
# plt.savefig("20241030/fkImshow.png", dpi=300, bbox_inches="tight")
# plt.close()
