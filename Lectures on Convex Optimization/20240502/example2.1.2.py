import matplotlib.pyplot as plt
import numpy as np
import os

X, Y = np.meshgrid(np.linspace(0, 1, 1000), np.linspace(0, 1, 1000))
Z = X * np.log(X) + Y * np.log(Y)
Z[np.isnan(Z)] = 0
idx = np.argmin(Z.flatten())
Z[X + Y > 1] = np.nan

XStar = X.flatten()[idx]
YStar = Y.flatten()[idx]
print(f"{XStar=}, {YStar=}")
print(f"{1/np.e}")

plt.contour(X, Y, Z, levels=20)
plt.plot([0, 1], [1, 0], "k")
plt.plot([XStar], [YStar], "r*", markersize=10)
plt.text(XStar + 0.15, YStar + 0.15, "(1/e, 1/e)", fontsize=15)
plt.colorbar()
plt.title("$f(x) = \\Sigma_i x_i log(x_i)$", fontsize=30)
plt.tight_layout()
plt.savefig(os.path.basename(__file__).replace(".py", ".png"))
