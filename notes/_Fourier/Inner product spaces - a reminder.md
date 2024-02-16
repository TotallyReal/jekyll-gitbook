---
title: Inner product spaces - a reminder
author: Ofir David
category: Fourier Analysis
layout: post
---
Course: [[Fourier Course Information]]
# The Euclidean prototype
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
# The inner product

With this geometric intuition, let us recall its generalization as "[[Inner product|inner products]]". In the following, our field will always be one of $\FF = \RR,\CC$.

![[Inner product#^9bddd8]]

Let's recall some interesting examples for inner product spaces:
>[!example]- Examples:
> 1. **Standard inner product**:
>     Over $\FF^n$ we have the standard inner product defined by:
>    $$\angles {(x_1,...,x_n),(y_1,...,y_n)} = \sum_1^n x_i\overline{y_i}.$$
> 2. **Integrals**: For continuous functions in $[0,1]$ we have the inner product:
>    $$\angles {f,g} =\int_0^1 f(x)\overline{g(x)}\dx$$
> 3. **Weighted integral**: For a nonnegative function $w:[0,1]\to[0,\infty)$ we define:
>    $$\angles {f,g}_w:=\int_0^1f(x)\overline{g(x)}w(x)\dx$$

The last two examples are for infinite dimensional inner products spaces (where the second example is a specific case of the third one). They can be further extended in two interesting ways:
- **Infinite domains**: Instead of integrating over $[0,1]$ we can of course integrate over any closed and bounded segment $[a,b]$. More over, we can integrate over unbounded segments, e.g. $[0,\infty)$, but then the inner product is not always well defined. For example, the constant 1 function $\bar{1}(x)$ is continuous on $[0,\infty)$, while 
  
  $$\angles {\bar{1},\bar{1}}_{[0,\infty)}=\int_0^\infty 1\cdot 1\cdot \dx = \infty.$$
  
  We can "solve" this problem by only considering functions which satisfy 
  
  $$\int_0^\infty |f(x)|^2\dx < \infty.$$
  
  The space of these function is call the [[L2 functions]] and denoted by $\mathcal{L}^2$.
- **Piecewise continuous function**: We can increase the set of functions we work with, and instead of just continuous functions, we can look at functions which are piecewise continuous. As in the previous case, this is again not an inner product space, though for a different reason. The "inner product" satisfies all the conditions except for $\angles {v,v} = 0$ if and only if $v=0$. For example, the function:
  ![[discontinuity.jpg|300]]

# The norm

Once we have the inner product (which "corresponds" to angles), we also have the norm (which is the "length" of a vector):

![[Norm#^5a49a3]]

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

---

<-[[Fourier/Motivation|Previous: Motivation]]    ,    [[Fourier Course Information|Back to table of contents]]    ,    [[Orthogonal sets - a reminder|Next: Orthogonal sets]]-> 
