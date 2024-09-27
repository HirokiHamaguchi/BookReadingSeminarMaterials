# 「凸関数は連続である」という言説の落とし穴

**開区間**上で定義された凸関数は**連続**です。この意味で、「凸関数は連続である」と言えます。

![open_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/974d791b-2602-3bee-a2b1-680437cdea8a.png)

しかし、**閉区間**上で定義された凸関数は区間の端点で**連続であるとは限りません**。
![closed_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/265dac7d-f42c-aee4-1313-4a5d4ca3b223.png)

なるほど、じゃあ端で不連続じゃなければ連続なんですね、と分かった気でいると、こういう例が落とし穴になります。

![psi](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/f63d6516-7d34-f04e-8cd3-90091c0d2c05.png)

本記事の内容は、一部以下の書籍に準拠します。以下、教科書と表記します。

Yurii Nesterov. 2018. Lectures on Convex Optimization (2nd. ed.). Springer Publishing Company, Incorporated.

https://link.springer.com/book/10.1007/978-3-319-91578-4

## 目次

- [「凸関数は連続である」という言説の落とし穴](#凸関数は連続であるという言説の落とし穴)
  - [目次](#目次)
  - [用語の定義](#用語の定義)
    - [凸関数](#凸関数)
    - [連続](#連続)
  - [閉区間において凸関数は連続であるとは限らない](#閉区間において凸関数は連続であるとは限らない)
  - [閉凸関数だが連続でない例](#閉凸関数だが連続でない例)
    - [場合分けのまとめと図示](#場合分けのまとめと図示)
  - [閉凸関数ならば下半連続である](#閉凸関数ならば下半連続である)
    - [下半連続の定義](#下半連続の定義)
    - [「閉凸関数ならば下半連続である」の証明](#閉凸関数ならば下半連続であるの証明)
      - [場合分けのまとめ](#場合分けのまとめ)
  - [開区間において凸関数は連続である](#開区間において凸関数は連続である)
    - [「1変数の閉凸関数はdom fで連続である」の証明](#1変数の閉凸関数はdom-fで連続であるの証明)
    - [2変数の場合、何故証明が回らないのか](#2変数の場合何故証明が回らないのか)
  - [最後に](#最後に)

## 用語の定義

厳密な議論の為に、まず定義を示します。
他の定義方法もあるかと思いますが、本記事では概ね教科書に従います。

### 凸関数

集合 $Q$ が **凸(convex)** であることは、次の条件を満たすことと同値です(教科書 Definition 2.1.1)：

$$
\alpha x + (1 - \alpha) y \in Q \quad (\forall x, y \in Q, ~ \forall \alpha \in [0, 1])
$$

| 凸集合である | 凸集合でない |
| :---: | :---: |
| ![convex](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/3b35d51e-3099-9339-cdec-493933834844.png) | ![non_convex](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/4206d582-2506-f89d-e23e-ff8b9179a9f2.png) |

(Wikipedia「[凸集合](https://ja.wikipedia.org/wiki/%E5%87%B8%E9%9B%86%E5%90%88)」より引用 / [CheCheDaWaff](https://commons.wikimedia.org/wiki/File:Convex_polygon_illustration1.svg), [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0&gt), via Wikimedia Commons)

また、拡大実数$\mathbb{R} \cup \\{ \pm\infty \\}$に値を取る関数 $f$ の **domain** は次のように定義されます：

$$
\mathrm{dom} ~ f = \\{ x \in \mathbb{R}^n \mid \lvert f(x) \rvert < \infty \\}
$$

議論の簡単の為、教科書では$\mathrm{dom} ~ f \neq \emptyset$のみを仮定していますが、[真凸関数 (proper convex function)](https://ja.wikipedia.org/wiki/%E7%9C%9F%E5%87%B8%E5%87%BD%E6%95%B0)は$\mathrm{dom} ~ f \neq \emptyset$に加えて$f(x)\neq -\infty$も定義に入れていることには注意して下さい。

そして、関数 $f$ が **凸** であることは、次が成立することと同値です(教科書 Definition 3.1.1):

$$
\displaylines{
f(\alpha x + (1 - \alpha) y) \leq \alpha f(x) + (1 - \alpha) f(y) \\\\
(\forall x, y \in \mathrm{dom} ~ f : \text{convex}, ~ \forall \alpha \in [0, 1])}
$$

また、本記事で重要となるキーワードに閉凸というものがあります。
関数 $f$ が **閉凸** であることは、次の集合が閉集合であることと同値です(教科書 Definition 3.1.2)：

$$
\mathrm{epi} ~ f = \\{ (x, t) \in \mathbb{R}^{n+1} \mid x \in \mathrm{dom} ~ f, ~ f(x) \leq t \\}
$$

冒頭にも示した以下の例は閉凸関数ではありません。これは$x$の左端および右端において、$\mathrm{epi} ~ f$の境界が含まれない為です。

![open_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/974d791b-2602-3bee-a2b1-680437cdea8a.png)

次の例も閉凸関数ではありません。左端の点線の部分が$\mathrm{epi} ~ f$の境界に含まれません。

![closed_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/265dac7d-f42c-aee4-1313-4a5d4ca3b223.png)

一方で、以下の例は閉凸関数です。端点を含んでいます。

![closed_interval_closed_convex](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/122d0d6e-fbaa-ba51-3ba0-e9379121f381.png)

実は、以下も閉凸関数です。ただし、$\mathrm{dom} ~ f$は$\\{ x \in \mathbb{R} \mid x > 0 \\}$と**開区間**です。

![closed_interval_inf](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/552c5e59-274b-4a43-8ec7-0727826659c6.png)

定義と見比べて下さい。

### 連続

教科書で陽に記述されている訳ではないと思われますが、一般に連続性は以下のように定義して問題ないです。詳細は例えば[こちら](https://old.math.jp/wiki/%E4%BD%8D%E7%9B%B8%E7%A9%BA%E9%96%93%E8%AB%965%EF%BC%9A%E9%80%A3%E7%B6%9A%E5%86%99%E5%83%8F#.E5.91.BD.E9.A1.8C_5.18_.28.E7.82.B9.E5.88.97.E3.82.92.E7.94.A8.E3.81.84.E3.81.9F.E7.82.B9.E3.81.AB.E3.81.8A.E3.81.91.E3.82.8B.E9.80.A3.E7.B6.9A.E6.80.A7.E3.81.AE.E7.89.B9.E5.BE.B4.E3.81.A5.E3.81.91.29)などを参照して下さい。

関数 $f$ が$\mathrm{dom} ~ f$で連続であることは、任意の$\overline{x} \in \mathrm{dom} ~ f$において$f$が連続であることと同値です。

ある$\overline{x} \in \mathrm{dom} ~ f$に対して、これは次のように定義されます：

$\overline{x}$に収束する任意の点列$\\{ x_k \\} \subseteq \mathrm{dom} ~ f$に対して、$\\{ f(x_k) \\}$は$f(\overline{x})$に収束する。

## 閉区間において凸関数は連続であるとは限らない

まず自明な例として、閉区間上で定義された凸関数は、区間の端点で連続であるとは限らないことを反例により示します。閉凸関数でない例でも示した、以下が反例です。

![closed_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/265dac7d-f42c-aee4-1313-4a5d4ca3b223.png)

この関数が凸関数であることは、凸関数の定義

$$
\displaylines{
f(\alpha x + (1 - \alpha) y) \leq \alpha f(x) + (1 - \alpha) f(y) \\\\
(\forall x, y \in \mathrm{dom} ~ f : \text{convex}, ~ \forall \alpha \in [0, 1])}
$$

において、$x$または$y$が区間の左端である時のみやや非自明ですが、この関数が連続であった場合(つまり、左端で黒丸ではなく白丸に値を持つ場合)に凸関数であることを踏まえると、この定義を満たすことが分かります。

余談として、以下の例は不連続ですが、そもそも凸関数ではありません。なぜ上の例では凸で下の例では凸でないか、もっと言えば、なぜ下の例では凸でないのに上の例は凸であるか、ということを、定義に沿って考えてみると面白いかも知れません。

![closed_interval_non_convex](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/dd1f9e47-2179-3637-6790-a2f0158b6667.png)

本題に戻ると、先の例は凸関数であり、かつその不連続性は明らかです。

以上より、**閉区間上で定義された凸関数は、区間の端点で連続であるとは限りません**。

しかし、この反例は**閉凸関数ではない**という、ある種自明な例外によるものです。

**閉凸関数である**という条件を課した時、不連続な例が存在するのか否かは、実はかなり非自明な問いだと私は思っています。それが**実は存在する**、というのが本記事の主題です。

## 閉凸関数だが連続でない例

本題です。冒頭に示した、非自明な不連続凸関数の例を示します。

$g\in \mathbb{R}^n$ と $\gamma \in \mathbb{R}$ に対して、

```math
\begin{align}
\phi(y,g,\gamma) &:= \langle g, y \rangle - \frac{\gamma}{2} \| y \|_2^2 \\\\
\psi(g,\gamma) &:= \sup_{y \in \mathbb{R}^n} \phi(y,g,\gamma)
\end{align}
```

と定義します。$\langle \cdot, \cdot \rangle$ は内積、$\| \cdot \|_2$ はユークリッドノルムです。

これが凸関数であることの証明は省略します。気になる方は教科書を参照して下さい。

以下、$\psi(g,\gamma)$の挙動を$\gamma$で場合分けして調べます。

- $\gamma<0$の場合

$g=0$の場合は明らかに$\psi(g,\gamma)=\infty$です。

$g\neq 0$の場合も、$y_\alpha = \alpha g$ とすると、

```math
\begin{align}
\phi(y_\alpha,g,\gamma) &= \langle g, \alpha g \rangle - \frac{\gamma}{2} \| \alpha g \|_2^2 \\
&= \alpha \| g \|_2^2 - \frac{\gamma}{2} \alpha^2 \| g \|_2^2 \\
&\to \infty \quad (\alpha \to \infty)
\end{align}
```

より、$\psi(g,\gamma)=\infty$です。

以上より、$\psi(g,\gamma)=\infty$です。

- $\gamma=0$の場合

```math
\phi(y,g,0) = \langle g, y \rangle = \begin{cases}
0 & g = 0\\
\infty & g \neq 0
\end{cases}
```

である為、

```math
\psi(g,0) = \begin{cases}
0 & g = 0\\
\infty & g \neq 0
\end{cases}
```

です。

- $\gamma>0$の場合

```math
\begin{aligned}
\psi(g,\gamma) &= \sup_{y \in \mathbb{R}^n} \left( \langle g, y \rangle - \frac{\gamma}{2} \| y \|_2^2 \right) \\
&= \sup_{y \in \mathbb{R}^n} \left( -\frac{\gamma}{2} \left\| y - \frac{g}{\gamma} \right\|_2^2 + \frac{\| g \|_2^2}{2\gamma} \right) \\
&= \frac{\| g \|_2^2}{2\gamma}
\end{aligned}
```

です。

### 場合分けのまとめと図示

結果として、$\psi(g,\gamma)$ は以下のようになります。

```math
\psi(g,\gamma) = \begin{cases}
0 & g=0, \gamma=0\\
\frac{\| g \|_2^2}{2\gamma} & \gamma > 0\\
\infty & \text{otherwise}
\end{cases}
```

これを$n=1$の場合に図示すると、冒頭にも示したような以下のグラフになります。

![psi](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/f63d6516-7d34-f04e-8cd3-90091c0d2c05.png)

$\gamma$を0に近づけすぎると非常に見づらいグラフになってしまうので、$\gamma$の下限を少しずつ変えて示しています。
要は$(g,\gamma)=(0,0)$においてその値は0ですが、その周辺では$\gamma$が0に近づくと$\infty$へと発散していくということです。

ここで、赤の点列は、

$$
\psi(\sqrt{\gamma}g,\gamma) = \frac{1}{2}\| g \|_2^2
$$

であることを用いて、ある$\beta>0$に対し、

$$
\displaylines{
\lim_{k \to \infty} \psi(g_k,\gamma_k) = \beta\\\\
\lim_{k \to \infty} (g_k,\gamma_k) = (0,0)
}
$$

を満たすような点列を示しています。
これは明らかに$\psi$が不連続であることを示しています。

さらに面白い点として、$\mathrm{dom} ~ \psi = (\mathbb{R} \times \\{ \gamma > 0 \\}) \cup \\{ (0,0) \\}$は**閉でも開でもない**ですが、**閉凸関数**です。

以下に1次元の場合を再掲しておくので、何故閉凸関数であるか考えてみて下さい。$\\{ \gamma > 0 \\}$という開集合が出てくるのに、これが閉凸関数であることが、自分は少し非自明であると感じました。

| 閉凸でない | 閉凸でない |
| :---: | :---: |
| ![open_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/974d791b-2602-3bee-a2b1-680437cdea8a.png) | ![closed_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/265dac7d-f42c-aee4-1313-4a5d4ca3b223.png) |

| 閉凸 | 閉凸 |
| :---: | :---: |
| ![closed_interval_closed_convex](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/122d0d6e-fbaa-ba51-3ba0-e9379121f381.png) | ![closed_interval_inf](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/552c5e59-274b-4a43-8ec7-0727826659c6.png)<br>($\mathrm{dom} ~ f$は開区間) |

この節のまとめとして、以下のことを強調しておきます。

**2変数以上の閉凸関数$f$は$\mathrm{dom} ~ f$で連続であるとは限らない。**

## 閉凸関数ならば下半連続である

以上の反例では、**閉凸関数であっても連続であるとは限らない**ことを示しました。

一方で、**閉凸関数ならば下半連続である**という、それを弱めた主張は常に成り立つことが言えます(教科書 Theorem 3.1.4.1)。

（なお、本記事では省略しますが[真凸関数かつ閉凸関数であることの必要十分条件は、それが下半連続である](https://ja.wikipedia.org/wiki/%E9%96%89%E5%87%B8%E5%87%BD%E6%95%B0)ことです。また、本記事の最初から2番目の図の例は、凸関数ですが、閉凸関数でもなく、また下半連続でもありません。）

本節では、下半連続の定義を示し、その後に閉凸関数ならば下半連続であることを示します。

### 下半連続の定義

下半連続性は連続性と同様、以下のように定義出来ます:

$\overline{x}$に収束する任意の点列$\\{ x_k \\} \subseteq \mathrm{dom} ~ f$に対して、$\liminf_{k \to \infty} f(x_k) \geq f(\overline{x})$。

実際、前節の例で$(\overline{g},\overline{\gamma})=(0,0)$に収束する赤点で示した点列も、関数値$\psi$は$\beta>0$に収束し、$\liminf_{k \to \infty} \psi(g_k,\gamma_k) = \beta > \psi(0,0) = 0$を満たしています。

下図も参照して下さい。

![lower_semi_continuous](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/b11fe54c-a7ae-7843-df80-402b9d6cf6f5.png)

(Wikipedia「[半連続](https://ja.wikipedia.org/wiki/%E4%B8%8B%E5%8D%8A%E9%80%A3%E7%B6%9A)」より引用 / [Mktyscn](https://commons.wikimedia.org/wiki/File:Lower_semi.svg), Public domain, via Wikimedia Commons)

### 「閉凸関数ならば下半連続である」の証明

$f$が閉凸関数ならば下半連続であることを示します。

$\overline{x}$に収束する任意の点列$\\{ x_k \\} \subseteq \mathrm{dom} ~ f$に対して、点列$\\{ (x_k, f(x_k)) \\} \subseteq \mathrm{epi} ~ f$を考えます。

これに対し、
$$
\liminf_{k \to \infty} f(x_k) \geq f(\overline{x})
$$
を言えれば良いです。

$\overline{f} := \liminf_{k \to \infty} f(x_k)$の値に基づく場合分けを行います。なお、$\overline{f}$は常に拡大実数$\mathbb{R} \cup \\{ \pm\infty \\}$内に存在します。$\liminf$になじみがない方は、[こちら](https://mathlandscape.com/limsup-liminf/#toc1)も参考にして下さい。

- $\overline{f} \in \mathbb{R}$の場合

[$\liminf$の性質](https://mathlandscape.com/limsup-liminf/#toc4)より、ある部分列$\\{ f(x_{k_j}) \\}$が$\overline{f}$に収束します。
[収束部分列の性質](https://www.nomuramath.com/lroj6ogu/)として、部分列の取り方に依らず、$x_{k_j} \to \overline{x}$です。以上より、$\\{ (x_{k_j}, f(x_{k_j})) \\}$は$(\overline{x}, \overline{f})$に収束します。

ここで、閉凸関数の定義より$\mathrm{epi} ~ f$は閉集合である為、その内で定義される任意の点列は、その部分列が極限を持つならば、それは$\mathrm{epi} ~ f$内に存在します。

よって、$\\{ (x_{k_j}, f(x_{k_j})) \\}$という点列は、$\overline{f} \in \mathbb{R}$を用いた$(\overline{x}, \overline{f})$という極限を持つため、それは$\mathrm{epi} ~ f$内に存在します。つまり、
$$
(\overline{x}, \overline{f}) \in \mathrm{epi} ~ f
\implies
\liminf_{k \to \infty} f(x_k) = \overline{f} \geq f(\overline{x})
$$
が成り立ち、主張は成立します。

- $\overline{f} = -\infty$の場合

$\overline{x} \in \mathrm{dom} ~ f$であることから、$f(\overline{x}) > -\infty$です。また、$\overline{f} = \liminf_{k \to \infty} f(x_k) = -\infty$より、十分大きな$k$に対して、$f(x_k)$は十分小さな値を取り、特に、$f(x_k) \leq f(\overline{x})-1$が成り立ちます。これは、$\\{ (x_k, f(\overline{x})-1) \\} \subseteq \mathrm{epi} ~ f$を意味します。

しかし、この点列は、$f(\overline{x})-1$が$k$に依存しない単なる定数である為、$(\overline{x}, f(\overline{x})-1)$に収束してしまいます。

先程と同様の閉性に関する議論より、これは$(\overline{x}, f(\overline{x})-1) \in \mathrm{epi} ~ f$を導きます。しかし、これは$f(\overline{x}) \leq f(\overline{x})-1 \iff 0 \leq -1$を意味し、矛盾します。

なので、そもそもの仮定が誤りであると分かります。

- $\overline{f} = \infty$の場合

この場合、
$$
\liminf_{k \to \infty} f(x_k) = \infty \geq f(\overline{x})
$$
は自明です。

#### 場合分けのまとめ

以上より、
$$
\liminf_{k \to \infty} f(x_k) \geq f(\overline{x})
$$
が成り立ち、$f$は$\overline{x}$で下半連続であることが示されました。

よって、$f$は下半連続であり、特に、閉凸関数ならば下半連続であることが示されました。

## 開区間において凸関数は連続である

本記事の最後に、開区間上で定義された凸関数は連続であることを示します。なお、この事はかなり簡単かつ初等的に示せますが、そのような証明は本節では省略します。別のサイトなどを参照して下さい。

より正確に、本節では以下の命題を示します (教科書 Lemma 3.1.4):

**1変数の閉凸関数$f$は$\mathrm{dom} ~ f$で連続である。**

これは、以前に示した

**2変数以上の閉凸関数$f$は$\mathrm{dom} ~ f$で連続であるとは限らない。**

という命題と対をなすものです。

この命題は閉区間で定義された不連続点がない凸関数の連続性を示すので、系として開区間で定義された凸関数の連続性が直ちに従います。

つまり、以下が連続です。

![open_interval](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/974d791b-2602-3bee-a2b1-680437cdea8a.png)

一方の端点を無限に飛ばしても、これは連続です。

![open_interval_inf](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/2d8bebe7-57d5-52f4-30a6-d761b4472d5a.png)

では、1変数の閉凸関数$f$が$\mathrm{dom} ~ f$で連続であることを示します。

**何故、2変数以上では下半連続のみしか言えないはずなのに、1変数では連続まで言えるのか**、という点に着目して証明します。

### 「1変数の閉凸関数はdom fで連続である」の証明

$f$が下半連続であることは先述の通りの為、省略します。

ある点$\overline{x} \in \mathrm{dom} ~ f \subseteq \mathbb{R}$について、点列$\\{ x_k \\} \subseteq \mathrm{dom} ~ f$が$\overline{x}$に収束するとします。この時、
$$
\limsup_{k \to \infty} f(x_k) \leq f(\overline{x})
$$
であることを示せば、上極限と下極限が一致することから、その極限は$f(\overline{x})$に[一致](https://mathlandscape.com/limsup-liminf/#toc6)し、$f$が$\overline{x}$で連続であることが示されます。

そのことを示します。

非常に重要な事として、1変数、つまり、数直線上の凸関数のdomainは、**一つの区間の形以外にありえません**。また、$\mathrm{dom} ~ f \neq \emptyset$を記事冒頭で仮定していました。

つまり、$x_k \to \overline{x}$より、$k$が十分大きい任意の$x_k$は、高々2つの固定された$\overline{y}_1, \overline{y}_2\in \mathrm{dom} ~ f$を用いて、

$$
x_k \in \\{ (1-\alpha_k) \overline{x} + \alpha_k \overline{y}_1, (1-\alpha_k) \overline{x} + \alpha_k \overline{y}_2 \\} \quad (\alpha_k \in [0, 1])
$$

と表せます。例えば以下の図では、赤点が$\\{ x_k \\}$を示しますが、十分$\overline{x}$に近い点は、そのように表せることが分かります。

![why_interval_1](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/9f6b27df-fcaf-4518-03ad-ad47c4ed8b39.png)

また、凸関数の定義より、

```math
\begin{align}
f(x_k) &\leq (1-\alpha_k) f(\overline{x}) + \alpha_k f(\overline{y}_1) \\
f(x_k) &\leq (1-\alpha_k) f(\overline{x}) + \alpha_k f(\overline{y}_2)
\end{align}
```

が成立します。

ここで、$x_k \to \overline{x}$より、$\alpha_k \to 0$が導かれます。そして、上記不等式で$\alpha_k \to 0$とすると、
$$
\limsup_{k \to \infty} f(x_k) \leq f(\overline{x})
$$
が導かれます。
これは、$f$が$\overline{x}$で上半連続であることを示しています。

よって、$f$は$\overline{x}$で連続であり、特に、$f$は$\mathrm{dom} ~ f$で連続であることが示されました。

### 2変数の場合、何故証明が回らないのか

本記事の締めくくりとして、上の証明が何故2変数以上の場合に回らないのか、という点について考察します。

閉凸関数だが連続ではない関数$\psi$について、$\mathrm{dom} ~ \psi = (\mathbb{R} \times \\{ \gamma > 0 \\}) \cup \\{ (0,0) \\}$でした。
そして、下半連続であるが連続ではないことを示すのに用いた赤の点列をdomainがなす2次元平面上にプロットしたのが下図です。

![why_interval_2](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/905155/9e681295-3cad-6e42-cbd9-21e8beafc543.png)

このような点列では、先の証明で仮定した$\overline{y}_1, \overline{y}_2$に相当するものが無限個必要になってしまいます。
これでは$x_k \to \overline{x}$としても、$\alpha_k \to 0$とは限らないため、先の証明が回らないのです。

ここに1変数の場合と2変数以上の場合の決定的な違いがあると考えています。

## 最後に

本記事は所属研究室の輪読準備の一環として書かれました。
皆様の理解の一助になれば幸いです。
