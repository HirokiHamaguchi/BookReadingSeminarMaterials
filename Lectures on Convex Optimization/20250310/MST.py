import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar


def f(x):
    return 0.5 * (x - 3) ** 2 + 1


def grad_f(x):
    return x - 3


L = 1  # Lipschitz constant
max_iter = 5
Q = [-5, 5]


# prox-function
def d(x):
    return 0.5 * x**2


x_k = 0
v_k = x_k
phi_history = [lambda x: L * d(x)]

x_history = [x_k]
v_history = [v_k]
y_history = []

max_iter = 5

for k in range(max_iter):
    # (a) y_k
    y_k = (k / (k + 2)) * x_k + (2 / (k + 2)) * v_k
    y_history.append(y_k)

    # (b) φ_{k+1}(x)
    prev_phi_k = phi_history[-1]

    def phi_k1(x, prev_phi=prev_phi_k, y_k=y_k, k=k):
        return prev_phi(x) + (k + 1) / 2 * (f(y_k) + grad_f(y_k) * (x - y_k))

    phi_history.append(phi_k1)

    # (c) v_{k+1}（Minimize φ_{k+1}(x)）
    result = minimize_scalar(phi_k1, bounds=Q, method="bounded")
    v_k1 = result.x

    # (d) x_{k+1}
    x_k1 = (k / (k + 2)) * x_k + (2 / (k + 2)) * v_k1
    print(x_k, v_k1, x_k1)

    v_k = v_k1
    x_k = x_k1
    x_history.append(x_k)
    v_history.append(v_k)

x_vals = np.linspace(Q[0], Q[1], 100)
f_vals = f(x_vals)

fig, axes = plt.subplots(max_iter, 1, figsize=(8, 4 * max_iter), sharex=True)

for k in range(max_iter):
    ax = axes[k]
    phi_vals = [phi_history[k](x) for x in x_vals]

    ax.plot(x_vals, f_vals, label="f(x)", linestyle="--", color="black")
    ax.plot(x_vals, phi_vals, label=f"φ_{k}(x)", linestyle=":", color="gray")

    ax.scatter(x_history[k], f(x_history[k]), color="red", label=f"x_{k}", zorder=5)
    ax.scatter(
        x_history[k + 1],
        f(x_history[k + 1]),
        color="orange",
        label=f"x_{k+1}",
        zorder=5,
    )
    ax.scatter(
        v_history[k],
        f(v_history[k]),
        color="blue",
        marker="x",
        label=f"v_{k}",
        zorder=5,
    )
    ax.scatter(
        v_history[k + 1],
        f(v_history[k + 1]),
        color="cyan",
        marker="x",
        label=f"v_{k+1}",
        zorder=5,
    )
    ax.scatter(
        y_history[k],
        f(y_history[k]),
        color="green",
        marker="o",
        label=f"y_{k}",
        zorder=5,
    )

    ax.arrow(
        x_history[k],
        f(x_history[k]),
        x_history[k + 1] - x_history[k],
        f(x_history[k + 1]) - f(x_history[k]),
        head_width=0.2,
        head_length=0.1,
        fc="red",
        ec="red",
        alpha=0.7,
    )
    ax.arrow(
        v_history[k],
        f(v_history[k]),
        v_history[k + 1] - v_history[k],
        f(v_history[k + 1]) - f(v_history[k]),
        head_width=0.2,
        head_length=0.1,
        fc="blue",
        ec="blue",
        alpha=0.7,
    )

    ax.set_title(f"Iteration {k}")
    ax.set_ylabel("f(x)")
    ax.grid(True)
    ax.legend()

axes[-1].set_xlabel("x")
plt.tight_layout()
# plt.show()
plt.savefig("MST.png")
