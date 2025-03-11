import numpy as np
import matplotlib.pyplot as plt


def plot_K_alpha(alpha):
    x1_vals = np.linspace(0.1, 2, 100)
    x2_vals = np.linspace(0.1, 2, 100)
    X1, X2 = np.meshgrid(x1_vals, x2_vals)
    Xi = (X1**alpha) * (X2 ** (1 - alpha))
    Z_upper = Xi
    Z_lower = -Xi
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X1, X2, Z_upper, color="blue", alpha=0.5, edgecolor="none")
    ax.plot_surface(X1, X2, Z_lower, color="blue", alpha=0.5, edgecolor="none")
    ax.set_xlabel("$x^{(1)}$")
    ax.set_ylabel("$x^{(2)}$")
    ax.set_zlabel("$z$")
    ax.set_title("$K_\\alpha$ Region")
    plt.show()


alpha = 0.5
plot_K_alpha(alpha)
