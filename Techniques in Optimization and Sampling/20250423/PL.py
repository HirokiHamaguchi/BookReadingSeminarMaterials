import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

f = x**2 + 2 * np.sin(x) ** 2
grad_f = 2 * x + 2 * np.sin(2 * x)

mu = 0.5
lhs = grad_f**2
rhs = 2 * mu * f

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].plot(x, f, label=r"$f(x) = x^2 + 2\sin^2(x)$", color="blue")
axes[0].set_title("Function $f(x)$")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(x, lhs, label=r"$\|\nabla f(x)\|^2$", color="red")
axes[1].plot(x, rhs, label=r"$2 \mu (f(x) - f(x^*))$", color="green")
axes[1].set_title(f"Verification of PL Inequality (μ = {mu})")
axes[1].set_xlabel("x")
axes[1].set_ylabel("Value")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
# plt.show()
plt.savefig("PL.png", dpi=300, bbox_inches="tight")
