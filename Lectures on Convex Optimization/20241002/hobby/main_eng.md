# The Pitfall of the Statement "A Convex Function is Continuous"

A convex function defined on an **open interval** is **continuous**. In this sense, it can be said that "a convex function is continuous."

![open_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/974d791b-2602-3bee-a2b1-680437cdea8a.png)

However, a convex function defined on a **closed interval** is **not necessarily continuous at the endpoints** of the interval.
![closed_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/265dac7d-f42c-aee4-1313-4a5d4ca3b223.png)

If you assume that the function is continuous as long as it is not discontinuous at the endpoints, you may fall into a trap, as illustrated by the following example:

![psi](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/f63d6516-7d34-f04e-8cd3-90091c0d2c05.png)

## Definitions of Terms

To ensure a rigorous discussion, we will first provide definitions.
While other definitions may exist, this article generally follows the textbook.

### Convex Function

A set $Q$ is **convex** if it satisfies the following condition (Textbook, Definition 2.1.1):

$$
\alpha x + (1 - \alpha) y \in Q \quad (\forall x, y \in Q, ~ \forall \alpha \in [0, 1])
$$

| Convex Set | Non-convex Set |
| :---: | :---: |
| ![convex](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/3b35d51e-3099-9339-cdec-493933834844.png) | ![non_convex](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/4206d582-2506-f89d-e23e-ff8b9179a9f2.png) |

(Quoted from Wikipedia's "[Convex Set](https://ja.wikipedia.org/wiki/%E5%87%B8%E9%9B%86%E5%90%88)" / [CheCheDaWaff](https://commons.wikimedia.org/wiki/File:Convex_polygon_illustration1.svg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0&gt), via Wikimedia Commons)

Additionally, for a function $f$ taking values in the extended reals $\mathbb{R} \cup \{ \pm\infty \}$, the **domain** of $f$ is defined as:

$$
\mathrm{dom} ~ f = \{ x \in \mathbb{R}^n \mid \lvert f(x) \rvert < \infty \}
$$

For simplicity, the textbook assumes $\mathrm{dom} ~ f \neq \emptyset$, but note that the definition of a [proper convex function](https://ja.wikipedia.org/wiki/%E7%9C%9F%E5%87%B8%E5%87%BD%E6%95%B0) includes both $\mathrm{dom} ~ f \neq \emptyset$ and $f(x) \neq -\infty$.

A function $f$ is **convex** if the following holds (Textbook, Definition 3.1.1):

$$
f(\alpha x + (1 - \alpha) y) \leq \alpha f(x) + (1 - \alpha) f(y) \\\\
(\forall x, y \in \mathrm{dom} ~ f : \text{convex}, ~ \forall \alpha \in [0, 1])
$$

Another important term in this article is "closed convex." A function $f$ is **closed convex** if the following set is a closed set (Textbook, Definition 3.1.2):

$$
\mathrm{epi} ~ f = \{ (x, t) \in \mathbb{R}^{n+1} \mid x \in \mathrm{dom} ~ f, ~ f(x) \leq t \}
$$

The following example, shown earlier, is not a closed convex function. This is because the boundary of $\mathrm{epi} ~ f$ does not include the left and right endpoints of $x$.

![open_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/974d791b-2602-3bee-a2b1-680437cdea8a.png)

The next example is also not a closed convex function, as the dotted portion at the left endpoint is not included in the boundary of $\mathrm{epi} ~ f$.

![closed_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/265dac7d-f42c-aee4-1313-4a5d4ca3b223.png)

On the other hand, the following example is a closed convex function, as it includes the endpoints.

![closed_interval_closed_convex](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/122d0d6e-fbaa-ba51-3ba0-e9379121f381.png)

In fact, the following is also a closed convex function. However, the domain of $f$ is $\{ x \in \mathbb{R} \mid x > 0 \}$, which is an **open interval**.

![closed_interval_inf](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/552c5e59-274b-4a43-8ec7-0727826659c6.png)

Please compare these examples with the definitions provided.

### Continuity

Though it may not be explicitly described in textbooks, continuity can generally be defined as follows without any issues. For further details, please refer to sources like [this one](https://old.math.jp/wiki/%E4%BD%8D%E7%9B%B8%E7%A9%BA%E9%96%93%E8%AB%965%EF%BC%9A%E9%80%A3%E7%B6%9A%E5%86%99%E5%83%8F#.E5.91.BD.E9.A1.8C_5.18_.28.E7.82.B9.E5.88.97.E3.82.92.E7.94.A8.E3.81.84.E3.81.9F.E7.82.B9.E3.81.AB.E3.81.8A.E3.81.91.E3.82.8B.E9.80.A3.E7.B6.9A.E6.80.A7.E3.81.AE.E7.89.B9.E5.BE.B4.E3.81.A5.E3.81.91.29).

The fact that a function $f$ is continuous on $\mathrm{dom} ~ f$ is equivalent to $f$ being continuous at any $\overline{x} \in \mathrm{dom} ~ f$.

For a specific $\overline{x} \in \mathrm{dom} ~ f$, this is defined as follows:

For any sequence $\{ x_k \} \subseteq \mathrm{dom} ~ f$ converging to $\overline{x}$, the sequence $\{ f(x_k) \}$ converges to $f(\overline{x})$.

## Convex functions on closed intervals are not necessarily continuous

First, as a trivial example, we will show by a counterexample that a convex function defined on a closed interval is not necessarily continuous at the endpoints of the interval. Here is a counterexample, which was also used as an example of a non-closed convex function:

![closed_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/265dac7d-f42c-aee4-1313-4a5d4ca3b223.png)

That this is a convex function can be confirmed using the definition of a convex function:

$$
f(\alpha x + (1 - \alpha) y) \leq \alpha f(x) + (1 - \alpha) f(y) \\\\
(\forall x, y \in \mathrm{dom} ~ f : \text{convex}, ~ \forall \alpha \in [0, 1])
$$

It may be slightly non-trivial when $x$ or $y$ is at the left end of the interval, but considering that the function would satisfy this definition if it were continuous (i.e., if the function had a value at the left end as an open circle instead of a filled one), we can see that the definition holds.

As a side note, the following example is discontinuous but is not a convex function in the first place. It might be interesting to think about why the previous example is convex and this one is not, in terms of the definition:

![closed_interval_non_convex](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/dd1f9e47-2179-3637-6790-a2f0158b6667.png)

Returning to the main point, the previous example is a convex function, and its discontinuity is evident.

Thus, **a convex function defined on a closed interval is not necessarily continuous at the endpoints of the interval**.

However, this counterexample is a somewhat trivial exception, as the function is **not a closed convex function**.

When the condition of being a **closed convex function** is imposed, the question of whether discontinuous examples exist becomes a much less trivial question, in my opinion. The main topic of this article is that such examples **do exist**.

## Example of a closed convex function that is not continuous

Now, let us move to the main point.

(p.152)

Here, I present an example of a non-trivial discontinuous convex function, as mentioned at the beginning.

For $g \in \mathbb{R}^n$ and $\gamma \in \mathbb{R}$, define the following:

```math
\begin{align}
\phi(y,g,\gamma) &:= \langle g, y \rangle - \frac{\gamma}{2} \| y \|_2^2 \\\\
\psi(g,\gamma) &:= \sup_{y \in \mathbb{R}^n} \phi(y,g,\gamma)
\end{align}
```

where $\langle \cdot, \cdot \rangle$ is the inner product and $\| \cdot \|_2$ is the Euclidean norm.

I will omit the proof that this is a convex function. For those interested, please refer to textbooks.

Next, let us investigate the behavior of $\psi(g,\gamma)$ based on different values of $\gamma$.

- When $\gamma<0$:

In the case of $g=0$, it is obvious that $\psi(g,\gamma)=\infty$.

In the case of $g\neq 0$, let $y_\alpha = \alpha g$. Then,

```math
\begin{align}
\phi(y_\alpha,g,\gamma) &= \langle g, \alpha g \rangle - \frac{\gamma}{2} \| \alpha g \|_2^2 \\
&= \alpha \| g \|_2^2 - \frac{\gamma}{2} \alpha^2 \| g \|_2^2 \\
&\to \infty \quad (\alpha \to \infty)
\end{align}
```

Thus, $\psi(g,\gamma)=\infty$.

- When $\gamma=0$:

```math
\phi(y,g,0) = \langle g, y \rangle = \begin{cases}
0 & g = 0\\
\infty & g \neq 0
\end{cases}
```

Therefore,

```math
\psi(g,0) = \begin{cases}
0 & g = 0\\
\infty & g \neq 0
\end{cases}
```

- For the case where $\gamma>0$:

```math
\begin{aligned}
\psi(g,\gamma) &= \sup_{y \in \mathbb{R}^n} \left( \langle g, y \rangle - \frac{\gamma}{2} \| y \|_2^2 \right) \\
&= \sup_{y \in \mathbb{R}^n} \left( -\frac{\gamma}{2} \left\| y - \frac{g}{\gamma} \right\|_2^2 + \frac{\| g \|_2^2}{2\gamma} \right) \\
&= \frac{\| g \|_2^2}{2\gamma}
\end{aligned}
```

### Summary of Cases and Visualization

As a result, $\psi(g,\gamma)$ is expressed as follows:

```math
\psi(g,\gamma) = \begin{cases}
0 & g=0, \gamma=0\\
\frac{\| g \|_2^2}{2\gamma} & \gamma > 0\\
\infty & \text{otherwise}
\end{cases}
```

When illustrated for the case of $n=1$, the graph is as shown below, as indicated at the beginning.

![psi](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/f63d6516-7d34-f04e-8cd3-90091c0d2c05.png)

Since the graph becomes difficult to interpret when $\gamma$ is too close to 0, the lower limit of $\gamma$ is adjusted gradually. In short, while the value is 0 at $(g,\gamma)=(0,0)$, it diverges to infinity as $\gamma$ approaches 0 nearby.

Here, the red dotted sequence represents the following:

$$
\psi(\sqrt{\gamma}g,\gamma) = \frac{1}{2} \|\| g \|\|_2^2
$$

Using this, for some $\beta>0$:

$$
\lim_{k \to \infty} \psi(g_k,\gamma_k) = \beta\\\\
\lim_{k \to \infty} (g_k,\gamma_k) = (0,0)
$$

This clearly shows that $\psi$ is discontinuous.

An interesting point is that $\mathrm{dom} ~ \psi = (\mathbb{R} \times \{ \gamma > 0 \}) \cup \{ (0,0) \}$ is **neither closed nor open**, but $\psi$ is a **closed convex function**.

Below is the one-dimensional case again, so please think about why this is a closed convex function. I found it somewhat non-trivial since the open set $\{ \gamma > 0 \}$ appears, yet it remains a closed convex function.

| Not closed convex | Not closed convex |
| :---: | :---: |
| ![open_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/974d791b-2602-3bee-a2b1-680437cdea8a.png) | ![closed_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/265dac7d-f42c-aee4-1313-4a5d4ca3b223.png) |

| Closed convex | Closed convex |
| :---: | :---: |
| ![closed_interval_closed_convex](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/122d0d6e-fbaa-ba51-3ba0-e9379121f381.png) | ![closed_interval_inf](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/552c5e59-274b-4a43-8ec7-0727826659c6.png)<br>($\mathrm{dom} ~ f$ is an open interval) |

In summary for this section, the following point should be emphasized:

**A closed convex function in two or more variables is not necessarily continuous on $\mathrm{dom} ~ f$.**

## A Closed Convex Function is Lower Semicontinuous

In the counterexample above, we demonstrated that a **closed convex function is not necessarily continuous**.

However, the weaker assertion that a **closed convex function is always lower semicontinuous** holds (see textbook Theorem 3.1.4.1).

(Note that although omitted in this article, the necessary and sufficient condition for a function to be a strictly convex and closed convex function is that it is lower semicontinuous. Also, the example in the second figure of this article is a convex function but neither closed convex nor lower semicontinuous.)

In this section, I will present the definition of lower semicontinuity and then show that a closed convex function is lower semicontinuous.

### Definition of Lower Semicontinuity

Lower semicontinuity, like continuity, can be defined as follows:

For any sequence $\{ x_k \} \subseteq \mathrm{dom} ~ f$ converging to $\overline{x}$, $\liminf_{k \to \infty} f(x_k) \geq f(\overline{x})$.

Indeed, in the previous example, the sequence of red points converging to $(\overline{g},\overline{\gamma})=(0,0)$ also shows that the function value $\psi$ converges to some $\beta>0$, satisfying $\liminf_{k \to \infty} \psi(g_k,\gamma_k) = \beta > \psi(0,0) = 0$.

Please also refer to the figure below.

![lower_semi_continuous](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/b11fe54c-a7ae-7843-df80-402b9d6cf6f5.png)

(Quoted from Wikipedia “[Semicontinuity](https://en.wikipedia.org/wiki/Semicontinuity)” / [Mktyscn](https://commons.wikimedia.org/wiki/File:Lower_semi.svg), Public domain, via Wikimedia Commons)

### Proof that "A Closed Convex Function is Lower Semicontinuous"

We will show that if $f$ is a closed convex function, then it is lower semicontinuous.

Consider any sequence $\{ x_k \} \subseteq \mathrm{dom} ~ f$ converging to $\overline{x}$, and examine the sequence $\{ (x_k, f(x_k)) \} \subseteq \mathrm{epi} ~ f$.

We aim to show that
$$
\liminf_{k \to \infty} f(x_k) \geq f(\overline{x}).
$$

We will divide the proof based on the value of $\overline{f} := \liminf_{k \to \infty} f(x_k)$. Note that $\overline{f}$ always exists within the extended real numbers $\mathbb{R} \cup \{ \pm\infty \}$. For those unfamiliar with the concept of $\liminf$, please refer to [this page](https://mathlandscape.com/limsup-liminf/#toc1).

- Case 1: $\overline{f} \in \mathbb{R}$

By the [property of liminf](https://mathlandscape.com/limsup-liminf/#toc4), there exists a subsequence $\{ f(x_{k_j}) \}$ converging to $\overline{f}$. By the [convergence property of subsequences](https://www.nomuramath.com/lroj6ogu/), $x_{k_j} \to \overline{x}$ for any choice of subsequence. Thus, the sequence $\{ (x_{k_j}, f(x_{k_j})) \}$ converges to $(\overline{x}, \overline{f})$.

Since $\mathrm{epi} ~ f$ is closed by the definition of a closed convex function, any sequence within $\mathrm{epi} ~ f$ whose subsequence has a limit must also have that limit inside $\mathrm{epi} ~ f$.

Therefore, since the sequence $\{ (x_{k_j}, f(x_{k_j})) \}$ has the limit $ (\overline{x}, \overline{f})$ with $\overline{f} \in \mathbb{R}$, we conclude that
$$
(\overline{x}, \overline{f}) \in \mathrm{epi} ~ f
\implies
\liminf_{k \to \infty} f(x_k) = \overline{f} \geq f(\overline{x}),
$$
proving the claim.

- Case 2: $\overline{f} = -\infty$

Since $\overline{x} \in \mathrm{dom} ~ f$, we know $f(\overline{x}) > -\infty$. Furthermore, because $\overline{f} = \liminf_{k \to \infty} f(x_k) = -\infty$, for sufficiently large $ k$, we have $f(x_k) \leq f(\overline{x}) - 1$. This implies that $\{ (x_k, f(\overline{x}) - 1) \} \subseteq \mathrm{epi} ~ f$.

However, since $f(\overline{x}) - 1$ is constant and does not depend on $k$, the sequence converges to $(\overline{x}, f(\overline{x}) - 1)$.

By a similar closedness argument as before, this leads to $(\overline{x}, f(\overline{x}) - 1) \in \mathrm{epi} ~ f$. However, this implies $f(\overline{x}) \leq f(\overline{x}) - 1 \iff 0 \leq -1$, which is a contradiction.

Thus, the original assumption must be incorrect.

- Case 3: $\overline{f} = \infty$

In this case,
$$
\liminf_{k \to \infty} f(x_k) = \infty \geq f(\overline{x}),
$$
which is trivially true.

#### Summary of Cases

From the above cases, we conclude that
$$
\liminf_{k \to \infty} f(x_k) \geq f(\overline{x}),
$$
which proves that $f$ is lower semicontinuous at $\overline{x}$.

Thus, we have shown that $f$ is lower semicontinuous, and in particular, a closed convex function is lower semicontinuous.

## Convex Functions on Open Intervals are Continuous

Next, we will show that convex functions defined on open intervals are continuous. This fact can be proven quite simply and elementarily, but we will omit such a proof in this section. Please refer to [another source](https://mathlandscape.com/convex-func/#toc7) for details.

More precisely, in this section, we will prove the following proposition (Textbook Lemma 3.1.4):

**A closed convex function of one variable is continuous on $\mathrm{dom} ~ f$.**

This proposition complements the previously proven fact that

**A closed convex function of two or more variables is not necessarily continuous on $\mathrm{dom} ~ f$.**

This proposition establishes the continuity of convex functions without discontinuities on closed intervals, and as a corollary, the continuity of convex functions on open intervals immediately follows.

Thus, the following is continuous:

![open_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/974d791b-2602-3bee-a2b1-680437cdea8a.png)

Even as one endpoint approaches infinity, the function remains continuous.

![open_interval_inf](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/2d8bebe7-57d5-52f4-30a6-d761b4472d5a.png)

We will now demonstrate that a closed convex function of one variable is continuous on $\mathrm{dom} ~ f$.

We focus on the question of **why, in dimensions higher than one, we can only claim lower semicontinuity, whereas in one dimension, we can claim continuity**, as we proceed with the proof.

### Proof of "A closed convex function of one variable is continuous on dom f"

Since it was mentioned earlier that $f$ is lower semicontinuous, this fact will be omitted here.

Let $\{x_k\} \subseteq \mathrm{dom} ~ f$ be a sequence converging to a point $\overline{x} \in \mathrm{dom} ~ f \subseteq \mathbb{R}$. To show that
$$
\limsup_{k \to \infty} f(x_k) \leq f(\overline{x}),
$$
it suffices to prove that the upper and lower limits coincide, thus ensuring that the limit is equal to $f(\overline{x})$. This would demonstrate that $f$ is continuous at $\overline{x}$.

Let's prove this.

It is crucial to note that, in the case of a single variable, i.e., on the real line, the domain of a convex function **must be an interval**. Additionally, it was assumed at the beginning of this discussion that $\mathrm{dom} ~ f \neq \emptyset$.

Thus, since $x_k \to \overline{x}$, for sufficiently large $k$, any $x_k$ can be represented using at most two fixed points $\overline{y}_1, \overline{y}_2 \in \mathrm{dom} ~ f$ as
$$
x_k \in \{(1-\alpha_k) \overline{x} + \alpha_k \overline{y}_1, (1-\alpha_k) \overline{x} + \alpha_k \overline{y}_2\} \quad (\alpha_k \in [0, 1]).
$$

For example, in the figure below, the red points represent $\{x_k\}$, and it can be seen that points sufficiently close to $\overline{x}$ can be expressed in this manner.

![why_interval_1](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/9f6b27df-fcaf-4518-03ad-ad47c4ed8b39.png)

By the definition of a convex function, we have:

```math
\begin{align}
f(x_k) &\leq (1-\alpha_k) f(\overline{x}) + \alpha_k f(\overline{y}_1), \\
f(x_k) &\leq (1-\alpha_k) f(\overline{x}) + \alpha_k f(\overline{y}_2).
\end{align}
```

Since $x_k \to \overline{x}$, it follows that $\alpha_k \to 0$. Substituting $\alpha_k \to 0$ into the above inequalities, we obtain
$$
\limsup_{k \to \infty} f(x_k) \leq f(\overline{x}).
$$
This shows that $f$ is upper semicontinuous at $\overline{x}$.

Thus, $f$ is continuous at $\overline{x}$, and in particular, $f$ is continuous on $\mathrm{dom} ~ f$.

### Why the proof does not work in the case of two variables

As a supplement, let’s briefly consider why the above proof does not hold when dealing with more than one variable.

For the function $\psi$, which is a closed convex function but not continuous, its domain is $\mathrm{dom} ~ \psi = (\mathbb{R} \times \{ \gamma > 0 \}) \cup \{ (0,0) \}$. The red sequence used to show that the function is lower semicontinuous but not continuous is plotted on the two-dimensional plane formed by the domain, as shown below.

![why_interval_2](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/9e681295-3cad-6e42-cbd9-21e8beafc543.png)

In this case, an infinite number of points analogous to $\overline{y}_1, \overline{y}_2$ would be needed. As a result, even if $x_k \to \overline{x}$, it would not necessarily follow that $\alpha_k \to 0$, which is why the previous proof does not apply.

This highlights a fundamental difference between the one-variable case and the case of more than one variable.

## Sufficient condition for "convex functions are continuous"

To conclude this article, I will present a sufficient condition under which convex functions are continuous, a topic that is somewhat outside the scope of standard textbooks. However, the essence of this condition can be found in articles such as [this one](https://math.stackexchange.com/questions/2961783/is-a-convex-function-always-continuous).

The following proposition holds:

**A convex function $f: \mathbb{R}^n \to \mathbb{R}$ is continuous.**

You may wonder, "Wasn't the statement 'convex functions are continuous' proven false earlier in this article?" However, **this proposition is true**.

The key difference lies in the fact that this convex function takes values **only in the real numbers, not extended real numbers**. In previous discussions, the convex function $f$ took values in the extended real number system, i.e., $f: \mathbb{R}^n \to \mathbb{R} \cup \{ \pm\infty \}$. In other words, the following proposition is equivalent:

**A convex function defined over the entire real domain is continuous.**

This assumption prevents counterexamples like $\mathrm{dom} ~ \psi = (\mathbb{R} \times \{\gamma > 0\}) \cup \{ (0,0) \}$ from arising.

Note that functions such as $f(x) = x^2$, where $\sup f(x) = \infty$, still satisfy the conditions of this proposition. Conditions such as "boundedness of $f$" are not required.

However, it is important to note that well-known convex functions such as $1/x$ and $-\log x$ do **not** satisfy the condition that "$\mathrm{dom} ~ f$ is the entire real line."

The pitfall of the statement "convex functions are continuous" remains, and a proper understanding of the assumptions under which a proposition holds is crucial.

The proof of this proposition is provided below.

### Proof of "Convex functions with a domain equal to the entire real space are continuous"

When $\mathrm{dom} ~ f = \mathbb{R}^n$, the following inequality holds for any $\beta > 0$ (e.g., Theorem 3.1.1 from a textbook):

```math
\begin{align}
  f\left(\frac{\beta}{\beta+1} \left(\overline{x} + \frac{\overline{x}-x}{\beta}\right) + \frac{1}{\beta+1} x \right) &\leq \frac{\beta}{\beta+1} f\left(\overline{x} + \frac{\overline{x}-x}{\beta}\right) + \frac{1}{\beta+1} f(x),\\
  f(\overline{x}) &\leq \frac{\beta}{\beta+1} f\left(\overline{x} + \frac{\overline{x}-x}{\beta}\right) + \frac{1}{\beta+1} f(x),\\
  f(\overline{x}) - f(x) &\leq \beta \left(f\left(\overline{x} + \frac{\overline{x}-x}{\beta}\right) - f(\overline{x})\right).
\end{align}
```

By considering the general argument with $\beta = r$, we obtain the following inequality:

```math
\begin{align}
-r \left(f\left( \overline{x} - \frac{\overline{x}-x}{r} \right) - f(\overline{x})\right) &\leq f(\overline{x}) - f(x) \leq r \left(f\left( \overline{x} + \frac{\overline{x}-x}{r} \right) - f(\overline{x})\right)\\
-r \left(f(\overline{y}_1) - f(\overline{x})\right) &\leq f(\overline{x}) - f(x) \leq r \left(f(\overline{y}_2) - f(\overline{x})\right)\\
-r M &\leq f(\overline{x}) - f(x) \leq r M
\end{align}
```

Since $r$ was arbitrary, by letting $r \to 0$, we obtain $f(x) \to f(\overline{x})$.

From the above, it is shown that $f$ is continuous at $\overline{x}$.

Therefore, $f$ is continuous, and it has been demonstrated that a convex function whose domain $\mathrm{dom}~f$ is the entire real number space is continuous.

## Summary

- When $\mathrm{dom}~f$ is the empty set:
  - Not subject to discussion (e.g., constant value mapping to $-\infty$).
- When $\mathrm{dom}~f$ is not the entire space $\mathbb{R}^n$ $(f: \mathbb{R}^n \to \mathbb{R} \cup \{\pm\infty\})$:
  - **Not closed convex**:
    - In some cases, $f$ is not even lower semicontinuous on $\mathrm{dom}~f$ (e.g., functions with discontinuities at the boundary of a closed interval).
    - In other cases, $f$ is continuous on $\mathrm{dom}~f$ (see [example of improper convex functions](https://math.stackexchange.com/questions/1105842/improper-convex-function)).
  - **Closed convex**:
    - For single-variable functions, $f$ is **continuous** on $\mathrm{dom}~f$ (e.g., $1/x, -\log x (x>0)$).
    - For multivariable functions, $f$ is **lower semicontinuous** on $\mathrm{dom}~f$ (e.g., the function $\psi$ in this article is an example that is **not continuous**).
- When $\mathrm{dom}~f$ is the entire space $\mathbb{R}^n$ $(f: \mathbb{R}^n \to \mathbb{R})$:
  - **Continuous** (e.g., $ax+b, x^2, |x|, e^x$).
