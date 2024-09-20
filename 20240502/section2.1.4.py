import os
import matplotlib.pyplot as plt
import numpy as np

mu = 1
L = 100
Qf = L / mu


def bestSolution(n, k):
    q = (np.sqrt(Qf) - 1) / (np.sqrt(Qf) + 1)
    x = np.zeros(n)
    for i in range(k):
        x[i] = q ** (i + 1)
    return x


def main():
    n = 12
    answers = np.zeros((n + 1, n))
    for k in range(n + 1):
        answers[k] = bestSolution(n, k)
    fig = plt.figure(figsize=(9, 6))
    ax = fig.add_subplot(111)
    plt.imshow(answers.T)
    plt.colorbar()
    plt.xticks(np.arange(0, n, 1))
    plt.yticks(np.arange(0, n, 1))
    plt.tick_params(
        axis="both",
        which="major",
        labelsize=10,
        bottom=False,
        top=False,
        labeltop=True,
        labelbottom=False,
    )
    secax = ax.secondary_xaxis("top")
    secax.set_xlabel("$k$-th iteration", fontsize=20)
    plt.ylabel("index $i$", fontsize=20)
    plt.title(
        "Possible upper bound for $x_k \in \mathbb{R}^{k,\infty}$",
        fontsize=20,
    )
    plt.tight_layout()
    # plt.show()
    plt.savefig(os.path.basename(__file__).replace(".py", ".png"))


if __name__ == "__main__":
    main()
