from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm, colors

plt.rcParams.update({
    "font.size": 14,
    "axes.labelsize": 26,
    "axes.titlesize": 20,
    "legend.fontsize": 13,
    "mathtext.fontset": "cm",
})

OUTPUT_DIR = Path(__file__).parent


def draw_x1_one_face(ax, eps, color, alpha=0.08):
    if eps <= 0:
        return
    n = 35
    u = np.linspace(0, eps, n)
    v = np.linspace(0, eps, n)
    U, V = np.meshgrid(u, v)
    mask = U + V <= eps
    X = np.where(mask, 1.0, np.nan)
    Y = np.where(mask, U, np.nan)
    Z = np.where(mask, V, np.nan)
    ax.plot_surface(X, Y, Z, color=color, alpha=alpha, linewidth=0, shade=False)

def style_3d_axes(ax):
    ax.set_xlim(0, 1.22)
    ax.set_ylim(0, 1.05)
    ax.set_zlim(0, 1.05)

    ax.set_xlabel(r"$x_1$", labelpad=20)
    ax.set_ylabel(r"$x_2$", labelpad=20)
    ax.set_zlabel(r"$x_3$", labelpad=24)

    # Chosen so that x3 label is visible and the solution fan is readable.
    ax.view_init(elev=23, azim=-47)

    # Remove colored axis spines/axis lines.
    ax.xaxis.line.set_linewidth(0)
    ax.yaxis.line.set_linewidth(0)
    ax.zaxis.line.set_linewidth(0)

    # Light panes and grid for spatial reference.
    for axis in [ax.xaxis, ax.yaxis, ax.zaxis]:
        axis.pane.set_alpha(0.04)
        axis.pane.set_edgecolor("0.75")

    ax.tick_params(axis="both", which="major", labelsize=11)

def draw_example_5_1_1():
    """Draw the existing Example 5.1.1 figure without changing its output."""
    eps_values = [0.00, 0.25, 0.5, 0.75, 1.0]
    positive_eps = [e for e in eps_values if e > 0]

    cmap = cm.viridis
    norm = colors.Normalize(vmin=min(positive_eps), vmax=max(positive_eps))

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")

    ax.scatter([1], [0], [0], s=85, color="black", depthshade=False, zorder=5) # type: ignore
    ax.text(1.03, -0.2, -0.2, r"$\varepsilon=0.00$", fontsize=15, color="red")

    for eps in positive_eps:
        col = cmap(norm(eps))
        draw_x1_one_face(ax, eps, col, alpha=0.085)

        t = np.linspace(0, eps, 100)
        x1 = np.ones_like(t)
        x2 = t
        x3 = eps - t

        ax.plot(x1, x2, x3, linewidth=6, color=col, solid_capstyle="round")
        ax.scatter([1, 1], [0, eps], [eps, 0], s=35, color=col, depthshade=False) # type: ignore
        ax.text(1.03, -0.2, eps + 0.11, rf"$\varepsilon={eps:.2f}$", fontsize=15)

    style_3d_axes(ax)
    ax.set_title(r"Perturbed solution sets $\mathrm{SOL}(q_\varepsilon,M)$ for increasing $\varepsilon$", pad=18)
    ax.view_init(elev=10, azim=-30)

    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "example5.1.1.png", dpi=300)
    plt.close(fig)


def draw_proposition_5_1_2():
    """Add reproducibly randomized choices of x_k to the Example 5.1.1 figure."""
    eps_values = [0.00, 0.25, 0.5, 0.75, 1.0]
    positive_eps = [e for e in eps_values if e > 0]
    cmap = cm.viridis
    norm = colors.Normalize(vmin=min(positive_eps), vmax=max(positive_eps))

    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection="3d")

    # The base is exactly the Example 5.1.1 plot.
    ax.scatter([1], [0], [0], s=85, color="black", depthshade=False, zorder=5) # type: ignore
    ax.text(1.03, -0.2, -0.2, r"$\varepsilon=0.00$", fontsize=15, color="red")

    for eps in positive_eps:
        col = cmap(norm(eps))
        draw_x1_one_face(ax, eps, col, alpha=0.085)
        t = np.linspace(0, eps, 100)
        ax.plot(np.ones_like(t), t, eps - t, linewidth=6, color=col, solid_capstyle="round")
        ax.scatter([1, 1], [0, eps], [eps, 0], s=35, color=col, depthshade=False) # type: ignore
        ax.text(1.03, -0.2, eps + 0.11, rf"$\varepsilon={eps:.2f}$", fontsize=15)

    # Any point of each segment is valid. A fixed seed makes the output stable.
    rng = np.random.default_rng(512)
    chosen_points = []
    for k, eps in enumerate(reversed(positive_eps), start=1):
        t_k = eps * rng.uniform(0.12, 0.88)
        x_k = (1, t_k, eps - t_k)
        chosen_points.append(x_k)
        ax.scatter(*x_k, s=95, color="white", edgecolor="black",
                   linewidth=1.8, depthshade=False, zorder=6) # type: ignore
        ax.text(1.025, t_k, eps - t_k + 0.045, rf"$x_{k}$", fontsize=13)

    chosen = np.asarray(chosen_points + [(1, 0, 0)])
    ax.plot(chosen[:, 0], chosen[:, 1], chosen[:, 2], color="black",
            linestyle="--", linewidth=1.5, alpha=0.7)

    style_3d_axes(ax)
    ax.set_title(r"Perturbed solution sets and choices $x_k\to x^*$", pad=18)
    ax.view_init(elev=10, azim=-30)

    plt.tight_layout()
    fig.savefig(OUTPUT_DIR / "proposition5.1.2.png", dpi=300)
    plt.close(fig)


def main():
    draw_example_5_1_1()
    draw_proposition_5_1_2()


if __name__ == "__main__":
    main()
