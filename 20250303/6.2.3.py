import numpy as np
import matplotlib.pyplot as plt

# f(x) = 0.5 ||x||_E1^2
#        + max_{1<=j<=m} {f_j + <g_j, x-x_j>_E1}
# where
# E1 = R^n
# ||x||_E1 = ||x||_2 (TOO CONFUSING!!!)
# E_2 = R^m
# f^(x) = 0.5 ||x||_1^2
# phi^(u) = <b, u>_E2
# b^(j) = <g_j, x_j>_E1 - f_j
# A^T = [g_1, ..., g_m]


np.random.seed(2)

# E1 = R^n
n = 2
# E2 = R^m
m = 2
# [f_j for j=1,...,m]
f_vals = np.array([1.0, 1.0])
# [g_j for j=1,...,m]
g_list = np.random.randn(m, n)
# [x_j for j=1,...,m]
x_list = np.random.randn(m, n)
# [b^(j) = <g_j, x_j> - f_j for j=1,...,m]
# (constant for given data)
b = np.array([np.dot(g_list[j], x_list[j]) - f_vals[j] for j in range(m)])
# A^T = [g_1, ..., g_m]
A = np.array(g_list)
assert A.shape == (m, n)

################

# この問題を最小化したい (p.446 (6.2.1))
# Find f^* = min_{x in Q1} f(x)


# p.447
def f_hat(x):
    # p.459
    # f^(x) = 0.5 ||x||_{E1}^2 = 0.5 ||x||_2^2
    return 0.5 * np.linalg.norm(x) ** 2


# p.447
def f_max_part(x):
    # p.458 notationマジで終わってる 誤植注意
    # max_{1<=j<=m} {f_j + <g_j, x-x_j>_E1}
    return np.max([f_vals[j] + np.dot(g_list[j], x - x_list[j]) for j in range(m)])


# p.447
def f(x):
    # p.458
    # f(x) = f^(x) + max_{1<=j<=m} {f_j + <g_j, x-x_j>_E1}
    return f_hat(x) + f_max_part(x)


################

# adjoin formを考える
# f_* = max_{u in Q2} phi(u)


# p.447
def phi_hat(u):
    # p.459
    # φ^(u) = <b, u>_E2
    return np.dot(b, u)


# p.447
# φ(u) = -φ^(u) + min_{x in Q1} {<Ax, u>_E2 + f^(x)}
def phi(u):
    # return -phi_hat(u) + np.min([np.dot(A @ x, u) + f_hat(x) for x in Q1])
    # p.460 3 微分すれば容易に分かる
    return -phi_hat(u) - 0.5 * np.linalg.norm(A.T @ u) ** 2


################

# これらのsmoothingを考える まずはf(x)のsmoothing


# entropy distance function
# convexity parameter: 1
# D_2 = ln m (defined in p.449 D_2 = max_{u in Q2} d_2(u))
def d2(u):
    # d2(u) = ln m + \sum_{j=1}^m u(j) ln u(j)
    return np.log(m) + np.sum(u * np.log(u))


D2 = np.log(m)


# Q2 = Delta_m = {u in R_+^m | sum(u) = 1}
# p.447にu_0の定義があり、これはprox-center,
# u_0 = argmin_{u in Q2} d_2(u)
#     = argmin_{u in Q2} {ln m + \sum_{j=1}^m u(j) ln u(j)}
#     = (1/m, ..., 1/m)
u0 = np.ones(m) / m
assert np.isclose(d2(u0), 0.0)


# p.447 Denote by u_{μ2}(x) the optimal solution of this problem.
# This problem: max_{u \in Q2} {<Ax, u>_E2 - \phi^(u) - μ2 d_2(u)}
def u_mu2(x, mu2):
    # return np.argmax([np.dot(A @ x, u) - phi_hat(u) - mu2 * d2(u) for u in Q2])
    # p.459
    s = np.array([f_vals[j] + np.dot(g_list[j], x - x_list[j]) for j in range(m)])
    ret = np.exp(s / mu2)
    return ret / np.sum(ret)


# p.447 μ2 が smoothing parameter で f(x)の平滑化に対応
# f_{μ2}(x) = f^(x) + max_{u \in Q2} {<Ax, u>_E2 - \phi^(u) - μ2 d_2(u)}
def f_mu2(x, mu2):
    u_star = u_mu2(x, mu2)
    return f_hat(x) + np.dot(A @ x, u_star) - phi_hat(u_star) - mu2 * d2(u_star)


# p.448
# \nabla f_{μ2}(x) = \nabla f^(x) + A^T u_{μ2}(x)
#                  = x + A^T u_{μ2}(x)
def nabla_f_mu2(x, mu2):
    return x + A.T @ u_mu2(x, mu2)


# p.448
# L_1(f^) は f^ のリプシッツ定数 つまり、1
L_1_f_hat = 1.0


################

# 次にphi(u)のsmoothingを考える


# p.448
# Q1 = R^n
def d1(x):  # 恐らくこの例では任意に決めてよいので、最も簡単な以下のものを選ぶ
    return 0.5 * np.linalg.norm(x) ** 2


# D_1 = \max_{x in Q1} d_1(x)
# ここでは適当に4としておく そうしないとLemma 6.2.3が成り立たない
D1 = 4.0

# p.448
# the prox-center x_0 with d_1(x_0) = 0
x0_prox_center = np.zeros(n)
assert d1(x0_prox_center) == 0.0


# p.448
def x_mu1(u, mu1):
    # x_{μ1}(u) = argmin_{x in Q1} {<Ax, u>_E2 + f^(x) + μ1 d1(x)}
    # return np.argmin([np.dot(A @ x, u) + f_hat(x) + mu1 * d1(x) for x in Q1])
    # p.460 2を基に考える 微分すると、A.T@u+x+mu1x
    return -(1 / (1 + mu1)) * (A.T @ u)


# p.448 mu1が smoothing parameter で phi(u)の平滑化に対応
# φ_{μ1}(u) = -φ^(u) + min_{x in Q1} {<Ax, u>_E2 + f^(x) + μ1 d1(x)}
def phi_mu1(u, mu1):
    # return -phi_hat(u) + np.min([np.dot(A @ x, u) + f_hat(x) + mu1 * d1(x) for x in Q1])
    x_star = x_mu1(u, mu1)
    return -phi_hat(u) + np.dot(A @ x_star, u) + f_hat(x_star) + mu1 * d1(x_star)


# p.449以降などで登場 平滑化しない場合の最適解
def x_0(u):
    return x_mu1(u, 0.0)


################

# まず、6.2.2にあるExcessive gap conditionを確認する

# p.426に定義がある
# a linear operator A: E1 -> E2^*
# ||A||_{1,2} = max_{x,u} {<A x, u>_E2 | ||x||_E1 = 1, ||u||_E2 = 1}
# p.459
# ||A||_{1,2} = max_{1<=j<=m} ||g_j||_E1^*
#             = max_{1<=j<=m} ||g_j||_2
norm_A_12 = np.max([np.linalg.norm(g_list[j]) for j in range(m)])


# p.447のDanskin's theoremあたりの話より
# L_1(f_mu2) は f_mu2 のリプシッツ定数
# L_1(f_mu2) = L_1(f^) + 1/mu_2 ||A||_{1,2}^2
def L_1_f_mu2(mu2):
    return L_1_f_hat + 1 / mu2 * norm_A_12**2


# 前提として、p.453において、
# \alpha_{-1} = 2, \alpha_0 = 1, \alpha_1 = 2/3
# \lambda_{1,0} = 2, \lambda_{2,0} = 1
# \mu_{1,0} = \lambda_{1,0} ||A||_{1,2} \sqrt{D2/D1}
# \mu_{2,0} = \lambda_{2,0} ||A||_{1,2} \sqrt{D1/D2}

lambda_10 = 2
lambda_20 = 1
mu10 = lambda_10 * norm_A_12 * np.sqrt(D2 / D1)
mu20 = lambda_20 * norm_A_12 * np.sqrt(D1 / D2)

# p.449 Lemma 6.2.3
# Let us choose an arbitrary μ2 > 0
mu2 = mu20
# and set \bar{x} = arg min_{x \in Q1}
# {〈∇f_μ2(x0), x − x0〉_E1 + L1(f_μ2) d1(x)},
# (x_0 means x_0_prox_center)
# xで微分して、x = -∇f_μ2(x0)/L1(f_μ2)
bar_x = -nabla_f_mu2(x0_prox_center, mu2) / L_1_f_mu2(mu2)
# \bar{u} = u μ2 (x0). (6.2.16)
bar_u = u_mu2(x0_prox_center, mu2)

mu1 = mu10
assert mu1 >= L_1_f_mu2(mu2), f"{mu1=} {L_1_f_mu2(mu2)=}"
print(f"{mu1=} {mu2=}")

# Then the excessive gap condition is satisfied for any μ1 ≥ L1(f_μ2).
lhs = f_mu2(bar_x, mu2)
rhs = phi_mu1(bar_u, mu1)
assert lhs <= rhs, f"{lhs=} {rhs=}"
print(f"Excessive gap condition: {lhs=} <= {rhs=}")

################

# 6.2.3 algorithmを実装する

# --- Main iterative scheme (Section 6.2.3 algorithm, cf. (6.2.26)) ---

N_iter = 10
sz = 100

fig, axes = plt.subplots(2, N_iter, figsize=(5 * N_iter, 5 * 2))

for k in range(N_iter):
    ax_1, ax_2 = axes[0, k], axes[1, k]
    ax_1.set_title(f"Iteration {k}")
    ax_2.set_title(f"Iteration {k}")
    # ax_1にはf_mu2(x, mu2)のプロット
    # ax_2にはphi_mu1(u, mu1)のプロット
    x = np.linspace(-2, 2, sz)
    y = np.linspace(-2, 2, sz)
    X, Y = np.meshgrid(x, y)
    Z1 = np.array([[f_mu2(np.array([x, y]), mu2) for x in x] for y in y])
    Z2 = np.array([[phi_mu1(np.array([x, y]), mu1) for x in x] for y in y])
    ax_1.contour(X, Y, Z1, levels=20)
    ax_1.scatter(bar_x[0], bar_x[1], color="red")
    ax_2.contour(X, Y, Z2, levels=20)
    ax_2.scatter(bar_u[0], bar_u[1], color="red")

    # τₖ = 2/(k+3) では、6.2.18が不成立に
    # p.452でL1(f^)=0としているが、これを満たさない
    tau = 2 / (k + 3)
    # 満たすまで調整する
    for _ in range(10):
        if tau**2 / (1 - tau) <= mu1 / L_1_f_mu2(mu2):
            break
        tau *= 0.9
    else:
        raise ValueError("tau is too large")

    if k % 2 == 0:
        # 6.2.17
        lhs = f_mu2(bar_x, mu2)
        rhs = phi_mu1(bar_u, mu1)
        assert lhs <= rhs, f"{lhs=} {rhs=}"
        # 6.2.18
        assert tau**2 / (1 - tau) <= mu1 / L_1_f_mu2(mu2)

        mu1_plus = (1 - tau) * mu1
        x_hat = (1 - tau) * bar_x + tau * x_mu1(bar_u, mu1)
        bar_u_plus = (1 - tau) * bar_u + tau * u_mu2(x_hat, mu2)
        bar_x_plus = (1 - tau) * bar_x + tau * x_mu1(bar_u_plus, mu1_plus)

        lhs = f_mu2(bar_x_plus, mu2)
        rhs = phi_mu1(bar_u_plus, mu1_plus)
        assert lhs <= rhs, f"{lhs=} {rhs=}"
        print(f"Excessive gap: {rhs - lhs=}")

        bar_x, bar_u, mu1, mu2 = bar_x_plus, bar_u_plus, mu1_plus, mu2
    else:
        # symmetric dual variant of 6.2.17
        lhs = f_mu2(bar_x, mu2)
        rhs = phi_mu1(bar_u, mu1)
        assert lhs <= rhs, f"{lhs=} {rhs=}"

        mu2_plus = (1 - tau) * mu2
        u_hat = (1 - tau) * bar_u + tau * u_mu2(bar_x, mu2)
        bar_x_plus = (1 - tau) * bar_x + tau * x_mu1(u_hat, mu1)
        bar_u_plus = (1 - tau) * bar_u + tau * u_mu2(bar_x_plus, mu2_plus)

        lhs = f_mu2(bar_x_plus, mu2_plus)
        rhs = phi_mu1(bar_u_plus, mu1)
        assert lhs <= rhs, f"{lhs=} {rhs=}"
        print(f"Excessive gap: {rhs - lhs=}")

        bar_x, bar_u, mu1, mu2 = bar_x_plus, bar_u_plus, mu1, mu2_plus


plt.tight_layout()
plt.savefig("20250303/6.2.3.png")
# plt.show()
