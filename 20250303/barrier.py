import matplotlib.pyplot as plt
import numpy as np

# p.415 Section 5.4.8 Separable Optimization

x = np.linspace(-5, 5, 500)
t = np.linspace(-5, 5, 500)
X, T = np.meshgrid(x, t)


def F1(x, t):
    return -np.log(x) - np.log(np.log(x) + t)


def F2(x, t):
    valid = t > np.exp(x)
    result = -np.log(t) - np.log(np.log(t) - x)
    result[~valid] = np.nan
    return result


def F3(x, t):
    valid = (t > x * np.log(x)) & (x > 0)
    result = -np.log(x) - np.log(t - x * np.log(x))
    result[~valid] = np.nan
    return result


def F4(x, t, p=2):
    valid = t > np.abs(x) ** p
    result = -np.log(t) - np.log(t ** (2 / p) - x**2)
    result[~valid] = np.nan
    return result


def F5(x, t, p=0.5):
    valid = (t > 0) & (t**p > x)
    result = -np.log(t) - np.log(t**p - x)
    result[~valid] = np.nan
    return result


def F6(x, t, p=2):
    alpha = p / (p + 1)
    valid = (t > 1 / x**p) & (x > 0)
    result = -np.log(x) - np.log(t) - np.log(x**alpha * t ** (1 - alpha) - 1)
    result[~valid] = np.nan
    return result


fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs = axs.flatten()

for i, (func, title) in enumerate(
    [
        (F1, "F1(x, t) = -ln(x) - ln(ln(x) + t)"),
        (F2, "F2(x, t) = -ln(t) - ln(ln(t) - x)"),
        (F3, "F3(x, t) = -ln(x) - ln(t - x ln(x))"),
        (F4, "F4(x, t) = -ln(t) - ln(t^(2/p) - x^2)"),
        (F5, "F5(x, t) = -ln(t) - ln(t^p - x)"),
        (F6, "F6(x, t) = -ln(x) - ln(t) - ln(x^α t^(1-α) - 1)"),
    ]
):
    Z = func(X, T)
    axs[i].contourf(X, T, Z, levels=20, cmap="viridis")
    axs[i].set_title(title, fontsize=12)
    axs[i].set_xlabel("x")
    axs[i].set_ylabel("t")

plt.tight_layout()
# plt.show()
plt.savefig("20250303/barrier.png")
