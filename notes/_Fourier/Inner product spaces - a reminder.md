---
title: Inner product spaces - a reminder
author: Ofir David
category: Fourier Analysis
layout: post
---
## The Euclidean prototype
We start by recalling some elements from the theory of inner products, which are our ways to give standard vector spaces a new geometric structure. The prototype of this structure is the standard Euclidean dot product on $\RR^3$ defined by 

$$\angles {(x_1, x_2, x_3),(y_1,y_2,y_3)}=x_1y_1+x_2y_2+x_3y_2.$$

This dot product measures two very important quantities. First is the length of a vector:

$$\norm {(x_1,x_2,x_3)} := \sqrt{\angles {(x_1,x_2,x_3),(x_1,x_2,x_3)}} = \sqrt{x_1^2+x_2^2+x_3^2}.$$

The second are angles between vectors - if $\theta$ is the angle between two vectors $u,v$, then

$$\cos(\theta)=\frac{\angles {u,v}}{\norm{u}\norm{v}}.$$

![[cosine between vectors.png|400]] 

In particular, two vectors are perpendicular, namely $\theta = \frac{\pi}{2}$ if
$$u\perp v \iff \angles {u,v} = 0.$$
This structure stands at the heart of the standard Euclidean geometry that we live in, and can be used to describe many of the interesting properties that our world has. In particular, one of the first theorems that most of us learn about, and is essential to many of the results in geometry: 

**The Pythagorean theorem**": If $u \perp v$ are perpendicular, then $\norm{u+v}^2 = \norm u^2 + \norm v^2$

![[pythagoras.jpg|400]]
## The inner product

With this geometric intuition, let us recall its generalization as "[[Inner product|inner products]]". In the following, our field will always be one of $\FF = \RR,\CC$.

>[!def] Definition: Inner Products
>Let $V$ be a vector space. An **inner product** on $V$ is a function $$\angles{\cdot,\cdot}:V\times V \to \FF$$
> such that 
> 1. **Positive**: For any $v\in V$ we have $\angles {v,v} \geq 0$ with equality if and only if $v=0.$
> 2. **Hermitian**: For any $u,v\in V$ we have that $\angles {u,v} = \overline{\angles {v,u}}$.
> 3. **Linear in first coordinate**: For any $u,v,w\in V$ and $\alpha \in \FF$ we have 
>    $$\angles {u+\alpha v,w} = \angles {u,w} + \alpha \angles {v,w}.$$

Let's recall some interesting examples for inner product spaces:
>[!example]- Examples:
> 1. **Standard inner product**:
>     Over $\FF^n$ we have the standard inner product defined by:
>    $$\angles {(x_1,...,x_n),(y_1,...,y_n)} = \sum_1^n x_i\overline{y_i}.$$
> 2. **Integrals**: For continuous functions in $[0,1]$ we have the inner product:
>    $$\angles {f,g} =\int_0^1 f(x)\overline{g(x)}\dx$$
> 3. **Weighted integral**: For a nonnegative function $w:[0,1]\to[0,\infty)$ we define:
>    $$\angles {f,g}_w:=\int_0^1f(x)\overline{g(x)}w(x)\dx$$

The last two examples are for infinite dimensional inner products spaces (where the second example is a specific case of the third one). If we extend our space of continuous functions even a little bit to piecewise continuous functions, we suddenly have two interesting problems that need to be solved:
- **The zero function**: Consider the function:
  ![[discontinuity.jpg|300]]
  This is clearly a piecewise continuous function with one discontinuity at $x=1$. While it is not the zero function, it does satisfy $\angles{f,f}=0$, so that the function $\angles{\cdot,\cdot}$ is no longer an inner product. However, this is the only problem with the definition, which can be fixed easily by "increasing" the zero function to contain such functions. 
  More formally, we will say that two functions are equivalent $f_1\sim f_2$ if $f_1-f_2$ is almost zero, in the sense that $\angles{f_1-f_2, f_1-f_2}=0$. The inner product is well defined modulo this equivalence, namely if $f_1 \sim f_2$ and $g_1 \sim g_2$, then $\angles{f_1,g_1}=\angles{f_2,g_2}$. This should not be two surprising because for piecewise continuous function $f_1 \sim f_2$ just means that $f_1(x)=f_2(x)$ except for finitely many points.
- **Infinite integrals**: Consider the function $f:[0,1]\to\RR$ defined by $f(x)=\cases{\frac{1}{x} & x>0 \\ 0 & x=0}.$ This too is a piecewise continuous function with only one discontinuity at $x=0$. However this time $\angles{f,f}=\int_0^1\frac{1}{x^2}\dx = \infty$ , so our inner product doesn't necessarily return finite numbers.
  This problem can be solved by restricting our space of functions to "small" enough functions, namely just $f$ which satisfy
  $$\int_0^\infty |f(x)|^2\dx < \infty.$$
  If we have two such functions $f,g$ , then 
  $$\abs{f(x)\overline{g(x)}} \leq \max\{\abs{f(x)}^2,\abs{g(x)}^2\}\leq \abs{f(x)}^2 + \abs{g(x)}^2.$$
  It follows that the integral in the inner product
  $$\angles {f,g} =\int_0^1 f(x)\overline{g(x)}\dx$$
  converges in absolute value (and is at most $\int_0^1 \abs{f(x)}^2 dx + \int_0^1\abs{g(x)}^2\dx$), and therefore converges.

> [!def] Definition: The space of piecewise continuous functions.
> For a segment $I\subseteq \RR$ we define:
> $$E^2(I)=\{f:I\to \CC\;\mid\;f\text{ piecewise continuous, }\int_I\abs{f(x)}^2\dx < \infty\}.$$
> We sometimes also denote it by $E(I)$.


 > [!remark] Remark: $\mathcal{L}^2$v-functions.
 > This space can (and should be) extended a little bit, and instead of piecewise continuous function, we can talk about integrable functions, and then it is denoted by $\mathcal{L}^2$. However, for simplicity we will continue to work with the piecewise continuous functions.

## The norm

Once we have the inner product (which "corresponds" to angles), we also have the norm (which is the "length" of a vector):

>[!def] Definition: Norms
> Let $V$ be a vector space. A **norm** on $V$ is a function
> $$\norm {\cdot} : V \to \RR$$
> such that:
> 1. **Positive**: For any $v \in V$ we have that $\norm v\geq 0$ with equality if and only if $v=0$.
> 2. **Absolute homogeneous**: For any $v\in V$ and $\alpha \in \FF$ we have $$\norm {\alpha v} = |\alpha|\cdot \norm v.$$
> 3. **Triangle inequality**: For any $u,v\in V$ we have $$\norm {u+v} \leq \norm u + \norm v.$$

There are many examples of interesting norms, but probably one of the most useful one for us is the induced norm:
>[!theorem] Theorem: The induced norm.
> If $V$ is an inner product space, then $\norm v := \sqrt {\angles {v,v}}$ is a norm function.

In particular, in the Euclidean geometry, this norm is the standard 
$\norm {x_1,...,x_n} = \sqrt{\sum_1^n |x_i|^2}$, and in our new and improved integral inner product on functions, we get:

$$ \norm f = \sqrt{\int_0^1 |f(x)|^2\dx }. $$

The importance of the norm functions, is that we use them to measure the size of vectors, and more over we can talk about distances between vector, by defining

$$\mathrm{dist}(u,v):=\norm{u-v}.$$

Different norms define different distances, which have all sorts of relations between them. The norms above are usually called the $\mathcal {L}^2$ norms (since we take the square and then square root), and denoted by $\norm {\cdot}_2$. A couple more interesting norms that we will encounter later on are the $\mathcal{L}^1$ and $\mathcal {L}^\infty$ norms, both in the continues and discrete cases, defined respectively by:


$$\begin{align} \norm f_1 & := \int_0^1 |f(x)|\dx & \norm {(x_1,...,x_n)}_1 & := \sum_1^n |x_i| \\ \norm f_\infty & := \sup|f(x)| & \norm {(x_1,...,x_n)}_\infty & := \max_i |x_i| \end{align}.$$

Actually, these are part of a family of norms called $\mathcal{L}^p$ norms for $1\leq p\leq \infty$ defined by:

$$\begin{align} \norm f_p & := \left(\int_0^1 |f(x)|^p\dx\right)^{1/p} & \norm {(x_1,...,x_n)}_p & := \left(\sum_1^n |x_i|^p\right)^{1/p} \end{align}.$$

For $p=1,2$ we get the $\mathcal{L}^1$ and $\mathcal{L}^2$ norms, and in the limit $p\to\infty$ we obtain the $\mathcal{L}^\infty$ norm.

While there are similarities between the discrete and continuous case, the discrete finite dimensional norms are much more well behaved than their infinite dimensional analogues. We will later discuss more in depth about these infinite dimensional norms, but for now let's get a little bit of visual intuition about the finite dimensional case, by simply drawing the unit circle $\norm{(x,y)}_p=1$ in the plane.
<center><iframe scrolling="no" title="L_p norms in the plane" src="https://www.geogebra.org/material/iframe/id/tqp6ewcv/width/700/height/333/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/false/ctl/false" width="700px" height="333px" style="border:0px; "> </iframe></center>

As you can see, the standard unit circle for $p=2$ is an actual circle, while for $p=1$ we get a diamond, and as $p\to \infty$ it approaches (and in the limit is) a square lined up to the X and Y axes. Also, for $p<1$ the formula defined above is not a norm, and we can "see" it, since the interior of the unit circle is not convex.