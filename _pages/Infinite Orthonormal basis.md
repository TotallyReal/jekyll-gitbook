---
title: Infinite Orthonormal basis
author: Ofir David
category: Fourier Analysis
layout: post
---

Course: [[Fourier Course Information]]

# Orthonormal basis - from finite to infinite

The concept of a basis is fundamental in linear algebra (and generally in mathematics). Its formal definition is just a set of linearly independent vectors which span the given vector space. The other equivalent definition, was that $\{v_1,...,v_n\}$ is a basis for $V$, if and only if any vector $v\in V$ has a unique presentation as a linear combination
$$v = \sum_1^n \alpha_i v_i.$$
This allowed us to identify between the abstract vector $v$ and the coordinate vector $(\alpha_1,...,\alpha_n)$ (Though remember that different bases produce different coordinate vectors).
Moreover, when our vector space can be spanned by finitely many vectors, we have seen that not only there exists a finite basis to the space, but all of the bases have the same size, which we call **the dimension** of the vector space. This has led to all sorts of interesting results, for example a linearly independent set which is the size of the dimension of the space, is also spanning, and therefore a basis.

When dealing with "non finite dimensional" vector spaces, we need to reconsider the definition of a basis. Suddenly finite sums might not be enough to describe the whole space. For simplicity, consider a countable infinite set $S=\{v_i \mid i\in \NN\}$, for which we ask whether it is spanning or linearly independent. There are two main approaches:
1. **The algebraic approach**: Here we only know how to add finitely many vectors, so the set $S$ is spanning, if every vector is a **finite** linear combination of finitely many vectors in $S$, and it is linearly independent if any **finite** subset of $S$ is linearly independent.
2. **The analytic approach**: In special and interesting cases, we might be able to define infinite sums, namely  $\sum_1^\infty \alpha_i v_i$ , and then the definition is the analogue to what we have for finite sets. As the spaces we deal with are special and interesting, this will be our next step.

# Convergence in norm

As usually, before talking about the limit of infinite sums, we need to define what are limits.

>[!def] Definition: Convergence in norm
 > Let $V$ be a normed vector space. We say that a sequence of vectors $v_n$ converges in norm to $v$ in $V$ if $\norm{v_n - v}\to 0$ and we denote it by $v_n \overset{\norm{\cdot}}{\longrightarrow} v$, or just $v_n \to v$ if there is no ambiguity.
 
>[!remark] Remark:
 > Note that we have defined convergence with convergence, namely:
 > $$v_n \normto v \iff \norm{v_n -v}\to 0.$$
 > This is not a cyclic definition, since the new norm convergence on the left is defined by the old known convergence of real numbers on the right.
 
 Before we go over a few examples to get some intuition, recall our three "main" norms on function spaces (say on $[0,1]$):
 
 $$\align{\norm{f}_1& = \int_0^1|f(x)|\dx \\ \norm{f}_2& = \sqrt{\int_0^1|f(x)|^2\dx} \\ \norm{f}_\infty& = \sup_{0\leq x\leq 1} |f(x)|. } $$

The $\mathcal{L}^2$ norm is the induced norm from the standard inner product, and comes with all the benefits of such a norm. Unless said otherwise, the "norm" convergences will mean that norm. While the $\cl^1$ and $\cl^\infty$ are not induced norm, they have nice geometric intuition:
1. The norm $\norm{f}_1$ measures the area between $f$ and the $x$-axis in absolute value. In particular two functions are close in this norm is the area between them is small.
2. The norm $\norm{f}_\infty$ measures the "maximal" (supremum) distance of $f$ from the $x$-axis. In particular, a function $f$ is close to $g$ in the infinity norm if it is in a small strip around $g$

(Add images)

>[!example]- Example 1: The functions $f_n(x) = \frac{x}{n}$
> ![[x divided by n.png|400]]
> Looking at the picture, we guess that the functions should converge to the zero function, and this is indeed the case for all of the norms above. Indeed, we have that:
> 
> $$\align{\norm{f_n}_1&=\frac{1}{2n} \to 0 \\ \norm{f_n}_2&=\frac{1}{\sqrt{3n^2}} \to 0 \\ \norm{f_n}_\infty &=\frac{1}{n} \to 0 .}$$

>[!example]- Example 2: The functions $f_n(x) = x^n$
> ![[x power n.png|400]]
> This time, the functions look a bit more complicated, but still "seem" to be converging to the zero function. Let's check if this is true:
> 
> $$\align{\norm{f_n}_1&=\frac{1}{n+1} \to 0 \\ \norm{f_n}_2&=\frac{1}{\sqrt{2n+1}} \to 0 \\ \norm{f_n}_\infty &=1 \not\to 0 .}$$
> 
> This time, unlike the previous example, the sequence converge to zero both in the $\mathcal{L}^1$ and $\mathcal{L}^2$ but not in $\mathcal{L}^\infty$.

>[!exc]- Excercise:
> Show that in the space $C[0,1]$ of continuous functions with the $\cl^\infty$ norm, the sequence $x^n$ of functions does not converge. 

>[!cor] Corollary:
> Different norm can have different convergence of the same sequence.

>[!exc] Excercise:
> Show that for any $f\in C[0,1]$ we have that $\norm{f}_1 \leq \norm{f}_2 \leq \norm{f}_\infty$.
> Conclude that if $f_n$ converges in $\cl^\infty$, then it converges in both $\cl^1$ and $\cl^2$, and similarly if $f_n$ converges in $\cl^2$, then it converges in $\cl^1$.
> So intuitively, the infinity norm is the "strongest norm": convergence there implies convergence "everywhere".

## Pointwise convergence 

One more important type of convergence for functions which we learned about in calculus, which is not a norm convergence (why?) is the pointwise convergence:

>[!def] Definition: Pointwise convergence of functions
> We say that a sequence of functions $f_n$ converges pointwise in a set $X$, if $f_n(x)$ is a convergent sequence for any $x\in X$.

>[!lem] Lemma:
> If $f_n \to f$ in $\cl^\infty$ (unifrom convergence) then $f_n \to f$ pointwise.

The last lemma is an interesting one, and helped quite a lot in calculus. It meant that whenever we want to look for uniform convergence, the only candidate was the pointwise limit (if exists) which is usually much easier to find. 
Unfortunately, there is no such connection with the induced norm.

>[!example]- Example: Pointwise convergence doesn't imply $\norm{\cdot}_2$ convergence 
> Consider the functions $f_n(x)=\cases{n& x\in(0,\frac{1}{n}) \\ 0 & else}$.
> Then this sequence converges pointwise to the zero function (check!) however 
> 
> $$\norm {f_n - 0}_2^2 = \int_0^{1/n} n^2 \dx =n \not \to 0 . $$


>[!example]- Example: $\norm{\cdot}_2$ convergence doesn't imply pointwise convergence
> The idea is to build functions which are (1) have very small area, and (2) this area "shifts" around. Then (1) will imply norm convergence, and (2) will mean that no one point will actually converge.
> More specifically, our functions will be characteristic (step) functions which are 1 on segment of size $\frac{1}{2^n}$ and zero otherwise, and we move around this segment. Formally, the first few functions are:
> 
> $$\align{f_1(x) \equiv 1=\chi_{[0,1]} \\ f_2(x)=\chi_{[0,1/2]} \; &, \; f_3(x) = \chi_{[1/2,1]} \\ f_4 = \chi_{[0,1/4]} &, \; f_5=\chi_{[1/4,2/4]}\;,\; f_6=\chi_{[2/4,3/4]}\;,\; f_6=\chi_{[3/4,1]}}$$
> 
> <iframe scrolling="no" title="no pointwise covnergence" src="https://www.geogebra.org/material/iframe/id/msyqgctt/width/600/height/299/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="600px" height="299px" style="border:0px;"> </iframe>
> 
> Since our step functions always have height 1, then the normed squared equals to the area, which in turn equals to the width $\frac{1}{2^n}\to 0$. On the other hand, this sequence doesn't converge point wise to any point!

# Continuous functions

Given an inner product space $V$ with the inner product $\angles{\cdot,\cdot}$, we now know how to generate a norm $\norm{v}:=\sqrt{\angles{v,v}}$, and from the previous section use this norm to define limits. Of course, once we have "limits" we can ask whether given functions are continuous, and fortunately our standard arithmetic functions are continuous.

>[!theorem] Theorem: Inner products are continuous
> Let $V$ be an inner product space and suppose that $v_n \normto v$ and $u_n \normto u$. In addition, let $\alpha_n \to \alpha$ in the field. Then the following functions are continuous:
> 1. **Addition**: $v_n + u_n \normto v + u$.
> 2. **Negation**: $-v_n \normto -v$.
> 3. **Scalar multiplication**: $\alpha_n v_n \to \alpha v$.
> 4. **Inner product**: $\angles{v_n , u_n} \to \angles{v,u}$.
> 5. **Norm**: $\norm {v_n} \to \norm {v}$.

>[!proof]- Proof:
> All of the proofs are similar to the standard continuity proofs in $\RR$. Let's prove as example only parts (4) and (5). Indeed, for part (4) we have
> $$\align{|\angles{v_n, u_n}-\angles{v, u}| & \leq |\angles{v_n, u_n}-\angles{v_n, u}| + |\angles{v_n, u}-\angles{v, u}| \\ &= |\angles{v_n, u_n - u}| + |\angles{v_n - v, u}| \leq \norm{v_n}\norm{u_n-u} + \norm{v_n-v}\norm{u} = (*) ,}  $$
> where the last inequality is the Cauchy-Shwartz inequality.
> By assumption, we have that  $\norm{u_n-u} , \norm{v_n-v} \to 0$. Since $\norm{u}$ is constant and $\norm{v_n} \leq \norm{v_n-v} + \norm{v}$ is bounded, we conclude that $(*)$ converges to zero, which is exactly what we wanted to show.
> Part (5) now follows by taking $u_n=v_n$, together with the fact that the square root function is continuous. $\square$

# Infinite sums and complete orthonormal bases

Now that we have the definition of limits in our normed space, we can define infinite sums $\sum_1^\infty v_k$ as the limit (if exists) of the partial sums $\sum_1^N v_k$. 

>[!remark] Remark: Some notations issues
> Since we work with convergence of functions, where norm convergence and pointwise convergence are different, we will use $\sum_1^\infty \angles{v,e_k}e_k \sim v$ to indicate norm convergence and $\sum_1^\infty \angles{v,e_k}e_k = v$ for pointwise convergence. Later we will see that they coincide in many cases.

With this new infinite sum definition and the continuity we saw above, many of the results from finite dimensional spaces carry on naturally to infinite dimensional spaces. For example:

>[!lem] Lemma: Coefficients of orthonormal sets
> Suppose that $\{e_k|k\in\NN\}$ is an orthonormal set, and $v=\sum_1^\infty \alpha_k v_k$. Then $\alpha_n = \angles{v, e_n}$.

>[!proof]- Proof:
> We have that 
> 
> $$\align{ \angles{v, e_n} & = \angles{\sum_1^\infty \alpha_k e_k, e_n} = \angles{\limfi{N} \sum_1^N \alpha_k e_k, e_n} \\ &= \limfi{N} \angles{ \sum_1^N \alpha_k e_k, e_n}},$$
> 
> where in the last equality we used the continuity of inner products. Since $\angles{ \sum_1^N \alpha_k e_k, e_n}=\alpha_n$ for any $N\geq n$, we see that the limit is $\alpha_n$ and we are done.

With this in mind, we can define our new infinite orthonormal basis.

>[!def] Definition: An orthonormal basis
> Let $V$ be an inner product space, and $\{e_k\}$ an orthonormal set. We say that it is a orthonormal basis if every $v\in V$ is the limit $\sum_1^n\angles{v, e_k}e_k \normto v$.

Note that by the definition of a complete orthonormal basis each vector has a presentation $v\sim\sum_1^\infty \alpha_k e_k$, and by the lemma above it is unique, namely $\alpha_k=\angles{v, e_k}$, or in other words we again have a unique presentation for every vector, just like for finite dimensional vector spaces and their bases.

We can now define the main orthonormal basis that we work with.

>[!theorem] Theorem: The Fourier system $E[-\pi, \pi]$
> Let $V=E[-\pi,\pi]$ be the vector space of piecewise continuous functions on $[-\pi,\pi]$, with the inner product $\angles{f,g}:=\frac{1}{\pi}\int_{-\pi}^{\pi} f(x)\overline{g(x)} \dx$. Then the functions
> $$\{\frac {1}{2}\}\cup\{\cos(nx) \mid n\geq 1\} \cup \{\sin(nx) \mid n\geq 1\}$$
> form a complete orthonormal basis.

>[!proof]- Proof:
> We already know that this system is orthonormal. The proof that it is "spanning" is more complicated and we will not prove in this course. However, for those interested, you should read about the [Stone-Weierstrass](https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem) theorem.

We can now extend two of the results we know for finite dimensional inner product spaces to the infinite dimensional case:

>[!claim] Claim:
>Let $V$ be an inner product space with an orthonormal system $\{e_k \mid k\in\NN\}$.
> 1. **Bessel inequality**: For every $v\in V$ we have $\sum_1^\infty |\angles{v,e_k}|^2 \leq \norm{v}^2$.
> 2. **Parseval identity**: If the orthonormal system is a basis, then there is an equality $\sum_1^\infty |\angles{v,e_k}|^2 = \norm{v}^2$ for all $v$. On the other hand, if there is such an equality for all $v$, then the system is basis.
> 3. **Generalized Parseval identity**: If the orthonormal system is a bsis and $u,v$ are any two vectors, then:
>    $$\angles{u,v} = \sum_1^\infty \angles{u,e_i}\overline{\angles{v,e_i}}.$$

>[!proof]- Proof:
> The claim here is in a sense the limit of the analogue claim for finite dimensional spaces, indeed, the main object here is none other than
> 
> $$\sum_1^\infty |\angles{v,e_k}|=\limfi{N} \sum_1^N |\angles{v,e_k}| = \norm{\limfi{N} \sum_1^N \angles{v,e_k}e}.$$
> 
> Moreover, recall that these approximations are the orthogonal projections of $v$ to the spaces spanned by $\{e_1,..., e_N\}$, so that we additionally have that 
> 
> $$\sum_1^N \angles{v,e_k}e \perp (v-\sum_1^N \angles{v,e_k}e),$$
> 
> and therefore
> 
> $$\norm{v}^2 = \norm{\sum_1^N \angles{v,e_k}e}^2 + \norm{v-\sum_1^N \angles{v,e_k}e}^2 =(*).$$
> 
> 1. The orthogonal projection in $(*)$ implies the standard finite dimensional Bessel inequality $\sum_1^N |\angles{v,e_k}|^2 \leq \norm{v}^2$ for any $N$, and taking the limit produces the general Bessel inequality.
> 2. Using $(*)$ we see that $\norm{\sum_1^N \angles{v,e_k}e} \to \norm{v}$ if and only if $\norm{v-\sum_1^N \angles{v,e_k}e} \to 0$ or equivalently $\sum_1^N \angles{v,e_k}e \normto v$. Hence, Parsevel identity holds for all $v\in V$ if and only if the system is complete.
> 3. Finally, for an orthonormal basis, using the continuity of the inner product, we obtain that :
>    $$\align{\angles{u,v}&=\angles{\sum_{i=1}^\infty\angles{u,e_i}e_i,\sum_{j=1}^\infty\angles{v,e_j}e_j}\\&=\sum_{i,j=1}^\infty\angles{u,e_i}\overline{\angles{v,e_j}}\angles{e_i,e_j}=\sum_{i=1}^\infty\angles{u,e_i}\overline{\angles{v,e_i}}}$$

>[!example] Example: The function $f(x)=x$
> Recall that we have already seen that $\angles{x, \sin(nx)}=2\frac{(-1)^{n+1}}{n}$. On the other hand, 
> 
> $$\angles{x, \cos(nx)} = \frac{1}{\pi}\int_{-\pi}^{\pi} x\cos(x)\dx 0$$ 
> 
> for all $n$, since $x\cos(nx)$ is an odd function. Thus we conclude that $x \sim 2\sum_1^\infty \frac{(-1)^{n+1}}{n} \sin(nx)$. Computing the Parseval identity, we obtain that
> 
> $$\frac{2\pi^2}{3}=\frac{1}{\pi}\int_{-\pi}^{\pi} x^2\dx = \sum_1^\infty \frac{4}{n^2}.$$
> 
> So while we already knew from calculus that $\sum_1^\infty \frac{1}{n^2}$ converge, now we can also find out its limit $\frac{\pi^2}{6}$.
> <center><iframe scrolling="no" title="Approximate with sine functions" src="https://www.geogebra.org/material/iframe/id/pa3rfcj3/width/800/height/450/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/false/ctl/false" width="700px" height="393px" style="border:0px;"> </iframe></center>

>[!lem] Lemma: The Riemann Lebesgue Lemma
> For an orthonormal basis $\{e_k \mid k\in \NN \}$ and any vector $v$ we have that $\angles{v,e_k}\to 0$.

-Add intuition-

>[!proof]- Proof:
> We know that $\norm v = \sum_1^\infty |\angles{v,e_k}|^2$ so we must have that $\limfi{n} |\angles{v,e_k}| = 0$.




---

<-[[Orthogonal sets - a reminder|Previous: Orthogonal sets]]    ,    [[Fourier Course Information#Table of contents|Back to table of contents]]    ,   [[Fourier Series|Next: Fourier series]] -> 

