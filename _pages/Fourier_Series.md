---
title: Fourier Series
author: Ofir David
category: Fourier Analysis
layout: post
---
# The Fourier series

After reminding ourselves the notations and results from inner product spaces, and combining it with the norm convergence in our new infinite dimensional vector spaces, we are ready to study the Fourier transforms on periodic function.

In the following sections we would like to study the inner product space $E[-\pi,\pi]$ of piecewise continuous function on $[-\pi,\pi]$ (or equivalently $2\pi$ periodic functions on $\RR$) with the inner product

$$\angles{f,g}=\frac{1}{\pi} \int_{-\pi}^\pi f(x)\overline{g(x)}\dx.$$

Our orthonormal basis will consist of 

$$\{\frac{1}{\sqrt{2}}, \sin(x), \cos(x), \sin(2x), \cos(2x),...\}.$$

> [!remark]- Remark: Equality between functions
> Recall that in our space $E[-\pi,\pi]$ we identify between two function $f,g$ if $f-g$ is zero almost everywhere (namely $f\equiv g$ for all but finitely many points).
> In particular, if both $f$ and $g$ have the same Fourier series, then $f\sim g$ are the same in $E[-\pi, \pi]$ (both equivalent to the same Fourier series) and therefore are equal almost everywhere.


> [!def] Definition: Fourier coefficients
> The Fourier coefficients of $f\in E[-\pi,\pi]$ are $\angles{f,\frac{1}{\sqrt{2}}}$ , $\angles{f,\sin(nx)}$, and $\angles{f,\cos(nx)}$ for all $n\geq 1$. In particular we have the classic Fourier series expansion:
> 
> $$f \sim \sum \angles{f,\frac{1}{\sqrt{2}}}\frac{1}{\sqrt{2}} + \sum_{n=1}^\infty \left( \angles{f,\cos(nx)}\cos(nx) + \angles{f,\sin(nx)}\sin(nx)\right).$$

When there is no ambiguity, we will use the notation:

$$\align{a_0&:=\angles{f,\cos(0x)}=\sqrt{2}\angles{f,\frac{1}{\sqrt{2}}} \\a_n&:=\angles{f,\cos(nx)} \; , \text{for } n\geq 1\\b_n&:=\angles{f,\sin(nx)} \; , \text{for } n\geq 1,}$$

for which the Fourier series looks like:

$$f \sim \frac{a_0}{2} + \sum_{n=1}^\infty \left(a_n\cos(nx) + b_n\sin(nx)\right).$$

Before you look at the examples below (which are $f(x)=x,\;|x|,\;\chi_{[-\pi,0]}-\chi_{[0,\pi]}$), try to compute some Fourier series for simple and nice functions (and in particular for these examples). 
To visualize these result, you can use the following Desmos program:
1. Enter the $a_0$ in the simple $a_0$ cell.
2. The syntax for the $a_n$ (and similarly $b_n$) should be 
   ```
   a = a_n for n=[1,...,k]
   ```
	   
3. To plot steps functions like $f(x)=\chi_{[-\pi,0]}-\chi_{[0,\pi]}$ use the notation 
   ```
   f={-pi<x<0:-1 , 0<=x<pi:1}
   ```
	or more generally 
	```
	{condition1: value1, condition2: value2, ...}
	```

   
Once you finish putting in the coefficients and choosing your function $f(x)$, you can close the menu and choose the approximation level using the $k=?$ slider below the graph.
You can also go directly to the Desmos site [here](https://www.desmos.com/calculator/bmne2o5ycg).

<iframe src="https://www.desmos.com/calculator/bmne2o5ycg" width="700" height="400" style="border: 1px solid #ccc" frameborder=0></iframe>


>[!example]- Examples: Fourier series
> 1. $f(x)=x$: In this case, we already saw that $b_n=2\frac{(-1)^{n+1}}{n}$ and $a_n=0$ for all $n$ (since $x\cos(nx)$ is an odd function).
> 2. $f(x)=\chi_{[0,\pi]}-\chi_{[-\pi,0]}$: This is also an odd function, so that $a_n=0$ for all $n$. As for the $b_n$, the product $f(x)\sin(nx)$ is even, so we have that 
>    
>    $$\align{b_n & = \angles{\chi_{[0,\pi]}-\chi_{[-\pi,0]},\sin(nx)} = \frac{1}{\pi} \int_0^\pi \sin(nx) \dx  - \frac{1}{\pi} \int_{-\pi}^0 \sin(nx) \dx \\ & = \frac{2}{\pi} \int_0^\pi \sin(nx) \dx = \frac{2}{n\pi} \cos(nx)\mid_0^\pi=\frac{2}{n\pi}\left((-1)^n-1\right).}$$
>    
>    It follows that $b_{2n}=0$ while $b_{2n+1}=\frac{4}{(2n+1)\pi}$. All in all, we get that
>    
>    $$\chi_{[0,\pi]}-\chi_{[-\pi,0]}\sim\sum_0^\infty \frac{4}{(2n+1)\pi} \sin((2n+1)x).$$
>    
>    <iframe scrolling="no" title="approximate step function with sin(kx)" src="https://www.geogebra.org/material/iframe/id/zjz8avxw/width/600/height/320/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="600px" height="320px" style="border:0px;"> </iframe>
> 3. $f(x)=\abs{x}$ : Now we have an even function, so that $b_n=0$ for all $n$. Similarly, since $f(x)\cos(nx)$ is even we get:
>    
>    $$\align{a_n&=\angles{|x|,\cos(nx)}=\frac{2}{\pi} \int_0^\pi x\cos(nx)\dx \\ &= \frac{2}{n\pi}  \left( x\sin(nx)\mid_0^\pi+ \int_0^\pi \sin(nx)\dx\right)=\frac{2}{n^2\pi}\left((-1)^n-1\right)}.$$
>    
>    It follows that $a_{2n}=0$ while $a_{2n+1}=\frac{-4}{(2n+1)^2\pi}$.
>    However, if $n=0$ then the computation above is not well defined as we divided by zero! So for this case we need a separate computation, we produces
> 
>    $$\angles{|x|,1}=\frac{1}{\pi}\int_{-\pi}^{\pi}|x|\dx = \pi.$$
> 
>    Finally, we get that 
> 
>    $$|x|\sim \frac{\pi}{2} - \sum_1^\infty \frac{4}{(2n+1)^2\pi} \cos((2n+1)x).$$
>    
> 4. $f(x)=\sin^2(x)$: While we can compute all the coefficients using the integrals, here we can use another method. Recall that $\sin(x)=Im(e^{ix})=\frac{e^{ix}-e^{-ix}}{2i}$. Using this identity, we see that
>    
>    $$\align{\sin^2(x) &= \left(\frac{e^{ix}-e^{-ix}}{2i}\right)^2 = \frac{e^{2ix}-2+e^{-2ix}}{-4} \\ & = \frac{\cos(2x)-1}{-2}= \frac{1}{2}-\frac{\cos(2x)}{2}.}$$
>    
>    This is already Fourier series expression of $f(x)$, and since there is always a unique such combination, this is the Fourier series of $f(x)$.


# Pointwise convergence

In our Fourier series $f \sim \frac{a_0}{2} + \sum_{n=1}^\infty \left(a_n\cos(nx) + b_n\sin(nx)\right)$ , the limit on the right is the norm convergence, and we have already seen that it doesn't imply pointwise convergence. However, as can be seen in the Fourier series in the step function $\chi_{[0,\pi]}-\chi_{[-\pi,0]}$ above, in most of the points we do have pointwise convergence. Moreover, the only points where it doesn't seem to have pointwise convergence are the two edge points at $\pm \pi$ and in $0$. These are exactly the "problematic" points where the function is not continuous. 

Leaving the edges aside for now, where does the Fourier series converges at the point  $x=0$? This is actually quite simple to find, since

$$\sum_0^\infty \frac{4}{(2n+1)\pi} \overbrace{\sin((2n+1)0)}^{=0}=0.$$

![400](step%20function%20approx.png)
More over, the intuition is that the approximation seems to converge to $-1$ just to the left of $x=0$ and to $+1$ just to the right of $x=0$ , and more or less go straight from $-1$ to $+1$ in the middle. In other words, the value at $x=0$ is exactly the average of the two values to its left and to its right! 

We actually see something similar at the edge points $\pm \pi$. If we think of $f$ as a periodic function, then as it passes through the point $x=\pi$ it jumps from $+1$ to $-1$ , which again has average $0$ which is where our blue approximation function is at.

These observation are true in a more generalized setting where the functions are "smooth enough". However, since we don't even assume that our functions are continuous, we need a slightly different definition than just saying differentiable functions.


>[!def] Definition: Half derivative
> Let $f\in E[-\pi,\pi]$ and denote the right limit at a point by $f(a^+)=\displaystyle{\lim_{x\to a^+}}f(x)$
> We define the right half derivative as the limit, if it exists, of
> 
> $$\displaystyle{\lim_{x\to a^+}}\frac{f(x)-f(a^+)}{x-a}.$$
> 
> Similarly we define the left half derivative.
> 
> For simplicity of notation, we identify between the edge points $\pm \pi$ and consider its left and right half derivatives as the left half derivative at $\pi$ and right half derivative at $-\pi$.
> 
> We denote by $E'[-\pi,\pi]\subseteq E[-\pi,\pi]$ all the piecewise continuous function on $[-\pi,\pi]$ that have left and right half derivative at every point in $[-\pi,\pi]$

We this new definition of "differentiable" function, we have the following:

>[!theorem] Theorem: Dirichlet's theorem for pointwise convergence
> Let $f\in E'[-\pi,\pi]$. Then at a given point $\lambda \in(-\pi,\pi)$ the Fourier series converges pointwise to the average of the left and right limits, namely
> 
> $$\frac{f(\lambda^+)+f(\lambda^-)}{2} = \frac{a_0}{2} + \sum_{n=1}^\infty \left(a_n\cos(n\lambda) + b_n\sin(n\lambda)\right).$$
> 
> At the edge points $\lambda =\pm \pi$, it converges to $\frac{f(-\pi^+)+f(\pi^-)}{2}$.
> 
> In particular, the series converges pointwise at each point where $f$ is continuous.

>[!remark]- Remark: Gluing the edges.
> As the last theorem suggest, we should actually think about the edge points $\pm \pi$ as a single point.

>[!example] Example:
> 1. We already saw that this theorem holds for the discontinuities of $f=\chi_{[0,\pi]}-\chi_{[-\pi,0]}$, namely the pointwise convergence there are to the average of the left and right limits.
>    Let's consider the pointwise convergence at $x=\frac{\pi}{2}$. Since $f(x)$ is continuous there and $f(\frac{\pi}{2})=1$, this is going to be the limit. Writing the pointwise convergence of the Fourier series, we get:
>    
>    $$1=\sum_0^\infty \frac{4}{(2n+1)\pi} \sin((2n+1)\frac{\pi}{2})=\frac{4}{\pi}\sum_0^\infty \frac{(-1)^n}{2n+1} .$$
>    
>    Try to prove this using other methods (clue: $\arctan(1)=\frac{\pi}{4}$).
>    
> 2. As another example, recall that the approximation for $f(x)=x$ looks like:
>    ![600](Pasted%20image%2020240131120746.png)
>    Here the function is "continuous" except for the edges, where it jumps from $f(\pi^-)=\pi$ to $f(-\pi^+)=-\pi$. The average is of course $\frac{f(-\pi^+)+f(\pi^-)}{2}=0$, and the pointwise convergence at these points are
>    
>    $$2\sum_{k=1}^{\infty}\left(-1\right)^{k+1}\overbrace{\frac{\sin\left(\pm k\pi\right)}{k}}^{=0}=0.$$ 
> 

>[!exc] Excercise:
> Compute the Fourier series for $f(x)=\chi_{[0,\pi]}$. Where are its discontinuity points, and what should be the pointwise convergence there for the Fourier series?

# Uniform convergence

We have now seen that for a "smooth" enough function $f(x)$, our Fourier series not only converges in norm but also pointwise (more or less). Can we strengthen this to a uniform convergence? In general, the answer is no. Our Fourier approximations are continuous (combination of sine and cosine functions), and the uniform limit of continuous functions is again continuous. So unless $f(x)$ by itself is continuous, this is false.

However, if $f(x)$ is continuous and "smooth" enough, then we do actually have uniform convergence. Before stating the theorem and proving it, recall one of the main tools to prove uniform convergence:

>[!theorem] Theorem: Weierstrass theorem for uniform convergence
> Let $f_n:I\to \CC$ be a sequence of functions. If $\sum_1^\infty M_n<\infty$ for some sequence of numbers satisfying  $\sup_x |f_n(x)|\leq M_n$, then $\sum_1^\infty f_n(x)$  converges uniformly and in absolute value.

In our case, we are dealing with sums of the form 

$$\frac{a_0}{2} + \sum_{n=1}^\infty \left(a_n\cos(nx) + b_n\sin(nx)\right).$$

Since the sine and cosine functions are bounded by $1$, using Weierstrass' theorem, if 

$$\sum_1^\infty \left(|a_n|+|b_n|\right)<\infty,$$

then the Fourier series will converge uniformly.

We already know that this sum is "not too large", since Bessel inequality implies that 

$$\sum_1^\infty \left(|a_n|^2+|b_n|^2\right)\leq \norm{f}^2,$$

however, this is not enough in general to show that the sum without the square is finite (for example, if $a_n=b_n=\frac{1}{n}$). It turns our that the "smoother" $f$ is, the faster both $a_n$ and $b_n$ converge to zero, and the better the chance for the series above to converge.

In particular, we have the following result for "smooth" functions.

>[!theorem] Theorem: Term by term derivatives
> Suppose that $f\in C[-\pi, \pi]$ is continuous and $f(\pi)=f(-\pi)$ and that $f'(x)\in E[-\pi,\pi]$ (and in particular $f'(x)$ exists except for finitely many points).
> 
> Then writing the Fourier series of $f$ as:
> 
> $$f(x)\sim \frac{a_0}{2} + \sum_1^\infty (a_n \cos(nx)+ b_n\sin(nx)),$$ 
> 
> we have that the Fourier series of $f'$ is the element wise derivative:
> 
> $$f'(x)\sim \sum_1^\infty (-na_n \sin(nx)+ nb_n\cos(nx)).$$


Note that going the other way around, given the $n$-th Fourier coefficients of $f'$, we can obtain the $n$-th Fourier coefficients of $f$ by dividing by $n$, so they converge to zero very fast. In particular we have the following:

>[!cor] Corollary: Uniform convergence
> Under the conditions of the Theorem above, the Fourier series of $f$ converges uniformly to $f$.


>[!proof]- Proof:
> Denote by $a_n,b_n$, and $\tilde{a}_n,\tilde{b}_n$ the Fourier coefficients of $f(x)$ and $f'(x)$ respectively. By the theorem we know that $\abs{a_n}=\frac{\abs{\tilde{n}_n}}{n}, \abs{b_n}=\frac{\abs{\tilde{a}_n}}{n}$ for $n\geq 1$. Using this fact and the Cauchy Shwarz inequality, we get
> 
> $$\sum_1^N (\abs{a_n}+\abs{b_n})=\sum_1^N \frac{1}{n}(\abs{\tilde{a}_n}+|\tilde{b}_n|)\leq \sqrt{\sum_1^N \frac{2}{n^2}}\sqrt{\sum_1^N\left( |\tilde{a}_n|^2+|\tilde{b}_n|^2\right)}.$$
> 
> If we can show that the last expression is bounded (and therefore converge) we could use Weierstrass theorem to prove uniform convergence. We already know that  $\sum_1^\infty \frac{1}{n^2}$ is finite (and even know how to compute it), and for the other term we can use Bessel's inequality to obtain:
> 
> $$\sum_1^N \left(|\tilde{a}_n^2| + |\tilde{b}_n^2|\right) \leq \norm{f'},$$
> 
> which completes the proof.


>[!example]- Example: $f(x)=|x|$
> This function is periodic continuous, and its derivative is $f'=\chi_{[0,\pi]}-\chi_{[-\pi,0]}$ which is in $E[-\pi,\pi]$ so we can apply the last lemma. We already computed its Fourier series:
> 
> $$|x|\sim \frac{\pi}{2} - \sum_1^\infty \frac{4}{(2n+1)^2\pi} \cos((2n+1)x).$$
> 
> Since 
> 
> $$\sum_1^\infty\sup_x|\frac{4}{(2n+1)^2\pi} \cos((2n+1)x)|\leq \sum_1^\infty \frac{4}{(2n+1)^2\pi}<\infty,$$
> 
> we can use Weierstrass' theorem to conclude that its convergence is indeed uniform.
> Furthermore, taking the term by term derivatives, we obtain another Fourier series that we already saw, namely:
> 
> $$\chi_{[0,\pi]}-\chi_{[-\pi,0]} \sim \sum_1^\infty \frac{4}{(2n+1)\pi} \sin((2n+1)x).$$
> 
> Note that the Fourier coefficients of $\chi_{[0,\pi]}-\chi_{[-\pi,0]}$ (which is not continuous) behave like $\frac{1}{n}$ while the coefficients of the continuous $|x|$ behave like $\frac{1}{n^2}$.


>[!proof]- Proof of term by term derivatives: 
> The main idea of the proof is to move between the Fourier coefficients of $f$ and $f'$ via integration by parts. More specifically, write the Fourier series of both $f$ and $f'$:
> 
> $$\align{f(x)& \sim \frac{a_0}{2} + \sum_1^\infty (a_n \cos(nx)+ b_n\sin(nx))\\ f'(x) &\sim \frac{\tilde{a}_0}{2} + \sum_1^\infty (\tilde{a}_n \cos(nx)+ \tilde{b}_n\sin(nx))}$$
> 
> Using integration by parts we have that 
> 
> $$\align{\tilde{a}_n &= \angles{f',\cos(nx)}=\frac{1}{\pi}\int_{-\pi}^{\pi}f'(x)\cos(x)\dx\\ &=\frac{1}{\pi}\left(f(x)\cos(nx)\mid_{-\pi}^{\pi} - \int_{-\pi}^{\pi}nf(x)\sin(nx)\dx \right)\\&=\overbrace{(f(\pi)-f(-\pi))}^{=0}(-1)^n+n\angles{f,\sin(nx)} = nb_n.}$$
> 
> A similar computation shows that $\tilde{b}_n = -na_n$. This shows that we can take the derivative element wise.
> 

>[!exc] Excercise:
> Suppose that we are given $f$ as in the theorem, however, we don't know if $f(\pi)=f(-\pi)$. Find the Fourier coefficients of $f'(x)$.
> Try to use the last theorem, instead of reproving it.

We saw that we can take the derivative term by term. Similarly, we can also take the integral element wise in the Fourier series.

>[!remark]- Remark: Integrals vs Derivative
> We usually study derivatives before integrals, and we sometimes get the feeling that they are easier. While this is usually true when trying to actually compute these functions, when speaking about the results, the integral, namely the antiderivative of a function is usually much "better" than the derivative of a function. Indeed, if we measure a function by how smooth it is, namely how many derivatives it has, then we always get that the anti derivative has at least (!) one derivative.


>[!theorem] Theorem: Term by term integrals
>Suppose that $f\in E[-\pi, \pi]$ and denote its Fourier series by
>
>$$f(x)\sim \frac{a_0}{2} + \sum_1^\infty (a_n \cos(nx)+ b_n\sin(nx)).$$
> 
>Then for any $[c,d]\subseteq [-\pi,\pi]$ we have the term by term integral:
>
>$$\int_c^d f(t)\dt = \frac{a_0(d-c)}{2} + \sum_1^\infty (\frac{a_n}{n} (\sin(nd)-\sin(nc)) - \frac{b_n}{n}(\cos(nd)-\cos(nc)).$$

>[!proof]+ Proof:
>
>The main step here is to note that we can write
>
>$$\align{\int_c^d f(t) \dt &= \frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\pi\chi_{[c,d]}\dt = \angles{f,\pi\chi_{[c,d]}} \\ & =\angles{\frac{a_0}{2} + \sum_1^\infty (a_n \cos(nx)+ b_n\sin(nx)),\pi\chi_{[c,d]}}.}$$
>
>Using the fact that the inner product is continuous (with respect to the $\norm{\cdot}_2$ norm), we can take the summation outside the integral to obtain:
>
>$$\align{\int_c^d f(t) \dt &=\angles{\frac{a_0}{2}, \pi\chi_{[c,d]}} + \sum_1^\infty\angles{a_n \cos(nx)+ b_n\sin(nx),\pi\chi_{[c,d]}} \\ & = \int_c^d\frac{a_0}{2} \dt + \sum_1^\infty\int_c^d(a_n \cos(nx)+ b_n\sin(nx))\dt \\ & = \frac{a_0(d-c)}{2} \dt + \sum_1^\infty(\frac{a_n}{n} (\sin(nd)-\sin(bc))- \frac{b_n}{n}(\cos(nd)-\cos(nc))\dt.}$$

> [!exc] Is the indefinite integral differentiable?
> Let $f(x)=|x|$ which is continuous, and define 
> 
> $$F(x)=\int_{-\pi}^{x} f(t)\dt-\frac{\pi^2}{2},$$ 
> 
> so that $F'(x)=f(x)$. 
> What can you say about the convergence of the Fourier series of $F(x)$? What is it $\cl_2$ , $\cl_\infty$ and pointwise limit? Check to see if your guess is correct.
> 

>[!proof]- Proof:
> It is not hard to show that 
> 
> $$F(x)=\cases{-\frac{x^2}{2}&x\leq 0\\ \frac{x^2}{2} & x\geq 0}.$$
> 
> Write it Fourier series as 
> 
> $$F(x) \sim \frac{a_0}{2} + \sum_1^\infty (a_n \cos(nx)+ b_n\sin(nx)).$$
> 
> Since $F(x)$ is an odd function, we immediately get that $a_n=0$ for all $n$. As for $b_n$, using symmetry and integration by parts we get 
> 
> $$\align{b_n&=\angles{F(x),\sin(nx)}=\frac{2}{\pi}\int_0^\pi \frac{x^2}{2} \sin(nx) \dx \\ & = -\frac{2}{\pi n} \left[ \frac{x^2\cos(nx)}{2}\mid_0^\pi -\int_0^\pi x\cos(nx)\dx  \right] = -\frac{2}{\pi n} \left[ \frac{\pi^2(-1)^n}{2} - \int_0^\pi x\cos(nx)\dx  \right].}$$
> 
> A second integration by parts gives:
> 
> $$\int_0^\pi x\cos(nx)\dx =  x\frac{\sin(nx)}{n}\mid_0^\pi - \int_0^\pi \frac{\sin(nx)}{n}\dx=\frac{\cos(nx)}{n^2}\mid_0^\pi=\frac{(-1)^n-1}{n^2}.$$
> 
> All together we have that $b_n=-\frac{2}{\pi n} \left[ \frac{\pi^2(-1)^n}{2} + \frac{(-1)^n-1}{n^2}  \right]$. 
> 
> Considering the converge of the Fourier series, since $F\in E[-\pi, \pi]$ we automatically get the $\cl_2$-norm convergence. Also, the function is continuous "everywhere" (except the edge points) and has half derivatives, so Dirichlet's theorem applies and we have pointwise convergence in $(-\pi,\pi)$. On the edges, the pointwise convergence is to the average:
> 
> $$\frac{\displaystyle{\lim_{x\to-\pi+}F(x)+\lim_{x\to\pi-}F(x)}}{2}=\frac{\pi^2/2-\pi^2/2}{2}=0.$$
> 
> The function $F(x)$ is not continuous at the edges, since $F(-\pi)\neq F(\pi)$ so we can't use the theorem about uniform convergence. In general the fact that the conditions of the theorem don't hold doesn't mean that its result doesn't hold. However, in this case it is true, since if there is uniform convergence in $[-\pi,\pi]$, then considering the functions as $2\pi$ periodic there will be uniform convergence everywhere, so the limit (of continuous function) is going to be continuous. As this is not true for $F$, the convergence is not uniform.

The last exercise shows that taking the integral of a continuous function doesn't necessarily gives us a smooth function, since there can be issues with the edge points. However, we can fix these problems in a way.

>[!exc] Excercise:
> Let $f_0(x)=sign(x)$ which is not continuous. Show that there are $f_1(x),f_2(x)$ such that $f_2'(x)=f_1(x)$ and $f_1'(x)=f_0(x)$ in almost every $x$ and both $f_1,f_2$ are continuous (including edge points).

>[!proof]- Proof:
> The main idea is to start with $\abs{x}$ as before, and to change it by a scalar to $f_1(x)=|x|+c$. This keeps $f_1(x)$ as a continuous function with $f_1'(x)=f_0(x)$. Let $F$ be as in the previous exercise, and define
> 
> $$F_C(x)=\int_{-\pi}^{x} (f_1(t)+C)\dt-\frac{\pi^2}{2} = F(x)+Cx.$$ 
> 
> The function $F_C(x)$ is still continuous in $(-\pi,\pi)$ and $F_C'(x)=f_1(x)$. Also, it limit at the edge points are
> 
> $$\lim_{x\to-\pi^+}F_C(x)=-\frac{\pi^2}{2}-C\pi\;\;;\;\;\lim_{x\to\pi^-}F_C(x)=\frac{\pi^2}{2}+C\pi.$$
> 
> Choosing $C=-\frac{\pi}{2}$ will cause them to be equal and therefore make $F_C(x)$ continuous.

>[!example] Example: Fourier in differential \\ integral equations
> Let's try to find continuous $f$ solving the equation
> 
> $$ \int_0^x f(t)\dt = x - f'(x) .$$
> 
> If the equation above holds, then in particular $f'(x)$ is by itself defined and continuous. Let's write the Fourier expansion of $f$ as
> 
>$$f(x)\sim \frac{a_0}{2} + \sum_1^\infty (a_n \cos(nx)+ b_n\sin(nx)).$$
>
>We would like to take the term by term derivative, but not all the conditions of the theorem hold - we don't know that $f(-\pi)=f(\pi)$. However, we can assume that it is true and continue on, but we need to check that our final solution does satisfy this condition (or alternatively, it satisfies the equation we started with). Under this assumption, we can write:
>
>$$f'(x)\sim \sum_1^\infty (-n a_n \sin(nx)+ n b_n\cos(nx)).$$
>
>For any function in $E[-\pi,\pi]$ we can do term by term integration, so putting everything together we obtain the equation:
>
>$$\frac{a_0x}{2} + \sum_1^\infty (\frac{a_n}{n} \sin(nx)- \frac{b_n}{n}(\cos(nx)-1)) = x - \sum_1^\infty (-n a_n \sin(nx)+ n b_n\cos(nx)).$$
>
>Moving everything to the same side, we get 
>
>$$\left(\frac{a_0}{2}-1\right)x + \sum_1^\infty \frac{b_n}{n} + \sum_2^\infty \left( a_n(\frac{1}{n}-n) \sin(nx) - b_n(\frac{1}{n}-n\right)\cos(nx))=0.$$
>
>If all the "coefficients" are zero, then of course it solves the equation. However, note that the last equation is not a Fourier expansion (namely, it is not a linear combination of a basis), so we don't know automatically that this is the only solution.
>In any case, one way to make all the coefficient zero is by taking:
>
>$$a_0=2,\; a_n =0\; \forall n\geq 2,\; b_n =0 \; \forall n\geq 1.$$
>
>We are now left with $f(x)=1+a_1\cdot\cos(x)$, and note that the functions in this family do satisfy $f(-\pi)=f(\pi)$. Finally, just to be on the safe side, let's see that they do satisfy our original equation:
>
>$$\align{\int_0^x f(t)\dx & = \int_0^x (1+a_1\cos(t))\dx = x + a_1 \sin(t)\mid_0^x = x+a_1\sin(x)\\ x-f'(x) & = x-(1+a_1\cos(x))' = x + a_1\sin(x)}.$$

# Convergence summarization

Let's summarize our convergence results in the space $E[-\pi,\pi]$:
1. Norm and pointwise convergence implications for sequence $f_n$ of functions:
   
   $$\align{\norm{\cdot}_\infty & \Rightarrow \norm{\cdot}_2 \Rightarrow \norm{\cdot}_1 \\ \norm{\cdot}_\infty&\Rightarrow \text{pointwise}.}$$
2. Neither the pointwise of $\norm\cdot_2$ convergence imply one another.
3. For any $f\in E[-\pi,\pi]$ there is $\norm\cdot_2$ convergence of the Fourier series: 
   $$f(x)\sim \frac{a_0}{2} + \sum_1^\infty (a_n \cos(nx)+ b_n\sin(nx)).$$
   
   The coefficients are determined uniquely by $f$, and if two functions $f,g$ have the same Fourier coefficients, then they are the same in $E[-\pi,\pi]$, namely $f(x)=g(x)$ except for finitely many points.
4. If $f$ has half derivatives at every point, then the Fourier series converges point wise to the averages:
   $$\frac{f(x^+)+f(x^-)}{2}.$$
   
   In particular, if $f$ is continuous at $x$, then the Fourier series converges pointwise to $f(x)$.
 5. For any $f\in E[-\pi,\pi]$ we can do term by term integration of the Fourier series.
 6. If $f$ is continuous (including edge points) and $f'\in E[-\pi,\pi]$, then we can also take derivatives term by term.
 
   


---

<-[Previous: Orthonormal basis](Infinite%20Orthonormal%20basis)    ,    [](Fourier%20Course%20Information#Table%20of%20contents|Back%20to%20table%20of%20contents)    ,   ??? -> 
