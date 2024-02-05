---
title: Orthogonal basis - a reminder
author: Ofir David
category: Fourier Analysis
layout: post
---

# Orthonormal sets
Once we have a vector space, usually the next step is finding a nice basis. In the finite dimensional case, we had the standard basis, denoted by $\{e_1,...,e_n\}$ where

$$e_i= (0,...,0,\overbrace{1}^i,0,...,0).$$

This is a simple yet powerful basis and it arises naturally and used in many places. One of the main reasons for its usefulness is that it also has nice "geometric" properties, and many ways it gives a "direction" to the space. 

<center><img src="../../images/orthogonality/standard_basis2.jpg" width="500"  /> </center>

Trying to understand and generalize this properties, led us to the definition of orthonormal bases.
> #### Definition: Orthogonal and orthonormal bases
> Let $V$ be an inner product space and let $\Omega \subseteq V$ be a subset. The set is called:
> 1. **Orthogonal**: if $0 \not \in \Omega$  and any distinct pair of vectors $v\neq u$ in $\Omega$ are perpendicular, namely $\angles uv =0$.
> 2. **Orthonormal**: if in addition $\norm v = 1$ for all $v\in \Omega.$ 
{: .definition }

We can also write the orthonormality condition it in a more "compact" way. For any $u,v\in \Omega$: 

$$\angles {u,v}=\begin{cases}1 & u = v \\0 & u\neq v\end{cases}.$$

The main advantage of this orthogonality definition, is that it lets us take our intuition from the standard Euclidean geometry to general spaces. In particular we have the following:

> #### Theorem: Orthonormal coefficients
> Suppose that $\{v_1,...,v_n\}\subseteq V$ is an orthogonal set. Then:
> 1. **Pythagoras**: $\norm {\sum_1^n v_i}^2 = \sum_1^n \norm {v_i}^2$.
> 2. **Coefficients**: If  $v\in span \\{ v_1, ..., v_n \\} $, namely $v=\sum_1^n \alpha_i v_i$, then $\alpha_i = \frac{\angles {v,v_i}}{\norm {v_i}^2}$. 
>    
>    In particular for an orthonormal set we get
>    
> $$v = \sum_1^n \angles {v,v_i} v_i \; , \text{ and } \; \norm{v}^2 = \sum_1^n |\angles {v,v_i}|^2.$$
> 
{: .theorem }

> #### Proof:
> 1. Under the assumption that $\angles {v_i,v_j} = 0$ for $i\neq j$, we get that 
>    
>    $$\norm{\sum_1^n v_i}^2 = \angles {\sum_{i=1}^n v_i, \sum_{j=1}^n v_j}=\sum_{i,j=1}^n \angles{v_i,v_j}=\sum_{i=1}^n \angles{v_i,v_i}=\sum_1^n \norm {v_i}^2.$$
>2. This is a straight forward computation:
>   
>   $$\angles {v,v_j}= \angles{\sum_{i=1}^n \alpha_i v_i, v_j} = \sum_{i=1}^n \alpha_i \angles{v_i,v_j} = \alpha_i \norm {v_i}^2$$
{: .proof }

As a simple example you should have in mind, in the standard Euclidean space, for a vector $\bar{x}=(x_1,...,x_n)$ the i'th coordinate, namely the i'th coefficient in the standard basis, is just $x_i = \angles{\bar{x}, e_i}$.


The last theorem already suggests that having a basis of orthonormal vectors can be quite helpful, since it is very easy to find the coefficients (both theoretically, and if needed numerically). Moreover, whenever we have an orthogonal set, it is already have of its way to being a basis:

> #### Lemma:
> Any orthogonal set is linearly independent.
> In particular, in an inner product space of dimension $n$, an orthogonal set of size $n$ is a basis.
{: .lemma }

> #### Proof:
> Let $\Omega$ be an orthogonal set, and suppose that we can write zero as linear combination of its elements (which by definition is a finite combination). This means that 
> 
> $$ 0 = \sum_1^n \alpha_i \omega_i $$
> 
> for some elements $\omega_i \in \Omega$. However, since the set is orthogonal, we know that $\alpha_i=\frac{\angles {0,\omega_i}}{\norm {\omega_i}^2}=0$, so that this combination is trivial, and we conclude that $\Omega$ is linearly independent.
{: .proof }

In an infinite dimensional space, life is much more interesting, and the definition of a spanning set, and therefore of a basis is slightly different, though it has the same intuition (???).

For now, let see a couple of interesting examples in this infinite dimensional case with the inner product $\angles{f,g}=\int_0^1 f(x)g(x)\dx$.

> #### Example: Orthogonal step functions {#ex:step}
> Consider the following set of functions which contains the constant 1 function, and for each integer $0\leq p$, and integer $0\leq n \leq 2^p - 1$ the function
> 
> $$s_{p,i} = \cases{
> -1 & \frac{n}{2^p}<x<\frac{n+0.5}{2^p} \\
> 1  & \frac{n+0.5}{2^p} < x < \frac{n+1}{2^p} \\
> 0  & else }.$$
> 
>  In words: each such function chooses a section of length $1/2^p$ and has $-1$ on half of it and $+1$ on the second half. It should not be very hard to convince yourselves that these functions form an orthogonal set (prove it!).
>  
>  What would you change to make it an orthonormal set?
> 
> <center><iframe scrolling="no" title="Orthogonal step functions" src="https://www.geogebra.org/material/iframe/id/vumxbcp7/width/627/height/300/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/false/ctl/false" width="627px" height="300px" style="border:0px;"> </iframe></center>
{: .example}

The second, and our main, example, is the smooth version of the previous one.

>#### Example:
> Consider the inner product on functions on $[-\pi,\pi]$ defined by
> $$\frac {1}{\pi}\int_{-\pi}^\pi f(x)\overline{g(x)}\dx .$$
> The set of functions 
> $$\Omega=\{\cos(kx) : k\geq 0\} \cup \{\sin(kx) : k\geq 1\}$$ 
> is (almost) orthonormal - the only exception is that $cos(0x)\equiv 1$ has norm $2$ instead of $1$.
{: .example}


>#### Excercise: Prove the claim above.
>There are several ways of solving this exercise:
> 1. **Complex integration**: If you know some complex integration, this is a very simple exercise using exponentials. For example, writing $\cos(nx)=\frac{e^{inx}+e^{-inx}}{2}$, we get that
>    $$\align{\angles {\cos(mx),\cos(nx)} & =\angles {\frac{e^{imx}+e^{-imx}}{2},\frac{e^{inx}+e^{-inx}}{2}} \\ 
>    & =\frac {1}{4}(\angles {e^{imx},e^{inx}} + \angles {e^{imx},e^{-inx}} + \angles {e^{-imx},e^{inx}} + \angles {e^{-imx},e^{-inx}})}.$$
>    These expressions are easy to compute:
>    
>    $$\angles {e^{inx},e^{imx}} = \frac{1}{\pi} \int_{-\pi}^\pi e^{i(m-n)x}dx.$$
>    
>    If $m=n$, then the integrand is simply $1$, so the integral is $\frac{2\pi}{\pi} = 2$. Otherwise, when $m-n\neq 0$ we get that
>    
>    $$\angles {e^{inx},e^{imx}} = \frac{1}{\pi} \frac{1}{i(m-n)}e^{i(m-n)x} \mid_{-\pi}^\pi = 0.$$ 
> 2. **Trigonometric identities**: Ignoring the complex integration, we can use directly the trigonometric equalities. Recall that the product of two cosine satisfies:
>    
>    $$\cos(\theta)\cos(\varphi) = \frac {\cos(\theta-\varphi)+\cos(\theta+\varphi)}{2}.$$
>    
>    Using this equality, we obtain that for $m,n\geq 0$ we have that
>    
>    $$\align{
>   \angles {\cos(mx),\cos(nx)} & =\frac {1}{\pi}\int_{-\pi}^\pi \cos(mx)\overline{\cos(nx)} \dx \\
>   & =\frac {1}{\pi}\int_{-\pi}^\pi \frac{\cos((m-n)x)+\overline{\cos((m+n)x)}}{2} \dx = \begin{cases} 2&m=n=0\\ 1&m=n\geq 1 \\ 0 & m\neq n \end{cases}.}$$
>    
>    A similar computation can be done for the rest of the inner products.
> 3. **Integration tricks**: Finally, one more way is by using some basic integral operations in an interesting way. The integral above for $m=n=0$ is trivial, and in general it is symmetric, so let's assume that $m\neq 0$. Using integration by parts, with the idea that integrating\differentiating $\cos(x)$ twice we return to the same place, we obtain the following: 
>    
>    $$\begin{align}\frac {1}{\pi}\int_{-\pi}^\pi \cos(mx)\overline{\cos(nx)} \dx & = \overbrace{\frac{1}{m\pi}\sin(mx)\cos(nx)\mid _{-\pi}^\pi}^{=0} + \frac {n}{m\pi}\int_{-\pi}^\pi \sin(mx)\sin(nx) \dx\\& = -\overbrace{\frac {n}{m^2\pi} \cos(mx)\sin(nx)\mid_{-\pi}^\pi} +\frac {n^2}{m^2\pi} \int_{-\pi}^\pi  \cos(mx)\cos(nx) \dx\end{align}.$$
>    
>    It then follows that 
>    
>    $$\left(1-\frac{n^2}{m^2}\right)\frac {1}{\pi}\int_{-\pi}^\pi \cos(mx)\overline{\cos(nx)} \dx = 0,$$
>    
>    so unless $m=n$, the integral must be $0$. As for the $m=n\geq 1$ case, namely integrating $\cos^2(nx)$, you should first convince yourself that $\int_{-\pi}^\pi \cos^2(nx) \dx = \int_{-\pi}^\pi \sin^2(nx) \dx$ (why?). Given that, we obtain that
>    
>    $$2\int_{-\pi}^\pi \cos^2(nx) \dx = \int_{-\pi}^\pi \cos^2(nx) \dx+\int_{-\pi}^\pi \sin^2(nx) \dx =\int_{-\pi}^\pi 1 \dx = 2\pi,$$
>    
>    so we conclude that for $n\geq 1$ we have
>    
>    $$ \angles {\cos(nx),\overline{\cos(nx)}} = 1.$$
{: .exercise }

The importance of orthogonal, and in particular orthonormal bases, is that it is very easy to find the coefficients in these bases.


# Orthogonal projection 

At this point we already have one very interesting property of orthogonal (and better yet) orthonormal sets - it is very easy to find the coefficients for orthogonal bases. However, these sets have more interesting properties, and one of them is related to a very interesting problem that rises up naturally in many places:
>#### Problem:
> Given a point $v\in V$ and a set $W\subseteq V$, find the distance from $v$ to $W$, and if possible find the closest point to $v$.
{: .problem}

It is not hard to see why this sort of problem appear in many places, since it basically looks for the shortest way from one point to get to some set. Just to make it even more interesting, sometimes this problem is hidden in other problems as well. For example, the famous problem of given a collection of points on the plane, and looking for the best linear approximation, is not only the same problem as above, but with the extra detail that $W$ is a subspace:

<center><figure>
<img src="../../images/orthogonality/linear_approximation.jpg" width="400"  /> 
<figcaption>Approximating the blue points data with the red line.</figcaption>
</figure>
</center>


When $W$ is a subspace, the solution in general is simple, where the main idea is what we expect to see in the standard Euclidean plane:
<center><figure>
<img src="../../images/orthogonality/orthogonal projection.png" width="500"  /> 
<figcaption>orthogonal projection</figcaption>
</figure>
</center>

As the image suggests, the point $w\in W$ closest to $v$ is its orthogonal (perpendicular) projection on $W$. Finally, the most important part, is that this orthogonal projection is very easy to compute:

>#### Theorem: Orthogonal projection
>
> Let $W\leq V$ be a finite dimensional subspace, and let $\{w_1,...,w_k\}$ be an orthonormal basis for $W$. The **orthogonal projection** to $W$ is defined by
> $$P_W(v):=\sum_1^k \angles {v,w_i}w_i.$$
> This orthogonal projection of $v$ is the closest point to $v$ in $W$.
{: .theorem}

# Examples

> #### Example: Orthogonal step function approximation
> Let's try to approximate the function $f(x)=x$ using the [orthogonal step functions](#ex:step) we defined previously, and we shall use only the first four such functions, namely :
> 
> %% image %%
> 
> These four function form an orthogonal set, and in order to use the theorem we need to normalize them, namely $\hat{f}_i := \frac{f_i}{\norm {f_i}}$, so that
> 
>  $$ \hat{f}_1 = f_1, \;\; \hat{f}_2 = f_2, \;\; \hat{f}_3 = \sqrt{2}f_3, \;\; \hat{f}_4 = \sqrt{2}f_4.$$
>  
>  The coefficients are then going to be 
>  
>  $$\angles{x,\hat{f}_1}=\frac{1}{2}, \;\; \angles{x, \hat{f}_2}=\frac{1}{4}, \;\; \angles{x, \hat{f}_3} = \angles{x, \hat{f}_4} =\frac{1}{16}. $$
>  
>  This means that we get the approximation:
>  
>  $$ x \sim \frac{1}{2}\cdot f_1 + \frac{1}{4}\cdot f_2 + \frac{1}{16} \cdot 2 \cdot (f_3+f_4).$$
>  
>  And finally, unsurprisingly, we get the approximation:
>  <center><figure><img src="../../images/orthogonality/approx_step_functions.jpg" width="500"  /> <figcaption>Approximation with step functions</figcaption></figure></center>

> #### Exercise:
> Compute $\angles{x, f_i}$ for any of the step function in the orthogonal basis. Do it one time directly using the integral, and one time "geometrically". Try to conjecture how the approximation will look like, when taking all the functions with $p\leq P$ for some positive integer $P$, and then prove it. Try to do the same for other function (e.g. $f(x)=x^2$) - can you say in general how the approximation will look like?
> 
> Note that in the example above we had $P=2$ since the corresponding segments of our functions were of length $1=1/2^0$, $1/2$ and $1/2^2$.
{: .exercise}


> #### Example: Approximation with sine waves.
> Similar to the previous example, we can try to approximate $f(x)=x$ using sine waves (explain why we don't need cosines).
> Add some explanations...
> <iframe scrolling="no" title="Approximate with sine functions" src="https://www.geogebra.org/material/iframe/id/pa3rfcj3/width/800/height/450/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/false/ctl/false" width="700px" height="393px" style="border:0px;"> </iframe>
{: .example}

There was a very interesting phenomenon with the last approximation: The "distance" between the approximation and our original $f(x)=x$ function goes to zero. In our case this means that the integral 
 
$$\int_{-\pi}^\pi (f(x)-2\sum_1^N (-1)^{k+1} \frac{\sin(kx)}{k})^2 \dx \to 0.$$
 
In other words, the area (more or less, up to the square in the integrand) between the function goes to zero. It does not mean that there is a pointwise convergence! For example, in all of our approximations, the values in both $x=\pm \pi$ remains zero, while the value of the original function is $\pm \pi$. However, we do have pointwise convergence in ALL the other points. This leads to a very interesting question, which we will later try to solve:

> #### Question:
> When does the norm convergence imply also pointwise convergence? And if there isn't pointwise convergence, then what can we say?


> #### Exercise:
> To get some intuition about the last question, try to approximate some other "nice" function and try to guess the answer for this question for those functions. Try it on a range of families of functions like: constant, linear, polynomial, exponential, unbounded function, noncontinuous, etc.







