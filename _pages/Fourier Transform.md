---
title: Fourier Transform
author: Ofir David
category: Fourier Analysis
layout: post
---
Course: [[Fourier Course Information]]

Up until now we talked about functions on $[-\pi,\pi]$, or equivalently $2\pi$ periodic functions. We now shift our focus to general function on $\RR$.
# Inner products

The first issue we encounter with these general functions, is that the corresponding inner products is on an infinite segment :
$$\angles{f,g}:=\frac{1}{2\pi}\int_{-\infty}^{\infty}f(x)\overline{g(x)}\dx.$$
This integral can diverge even for very nice functions, and in particular $\angles{1,1}=\infty$. To solve this problem we consider a subfamily of function, which is large enough to contain most of the functions that we work on.

>[!def] Definition: Norms on functions on $\RR$
> For a function $f:\RR \to \CC$ we define:
> 
> $$\begin{align} \norm f_1 & = \int_{-\infty}^{\infty} \abs{f(x)} \dx \\ \norm f_2 & = \frac{1}{2\pi} \left(\int_{-\infty}^{\infty} \abs{f(x)}^2  dx\right)^{1/2} \\ \norm f_\infty & = \sup_x \abs{f(x)}. \end{align}$$
> 
> For $p=1,2,\infty$ we denote by 
> 
> $$E^p(\RR) = \{f:\RR \to \CC \;\mid\; f \text{ piecewise continuous}, \norm f_p < \infty\}.$$

In the $[-\pi,\pi]$ finite case, we have that $\norm f_1 \leq \norm f_2 \leq \norm f_\infty$  (maybe up to a scalar normalization). This is no longer true in the infinite case, for example $f\equiv 1$ has $\norm f_2 = \norm f_1 =\infty$ while $\norm f_\infty =1$. Actually, you can show that:

>[!exc] Excercise:
> For each $p\in\{1,2,\infty\}$ find a function $f$ such that $\norm f_p <\infty$, while the other two norms are infinity.

We already saw that the inner product is not well defined for just bounded functions in $L^\infty (\RR)$, but it is well defined for function in $L^2(\RR)$.

>[!lem] Lemma: Inner product on $E^2(\RR)$
> The map $\angles{f,g}$ defined above is an inner product on $L^2(\RR)$.

>[!proof]- Proof:
> The Cauchy-Shwarz inequality on finite segments show that 
> 
> $$\abs{ \int_a^b f(x)\overline{g(x)}\dx }^2 \leq  \int_a^b \abs{f(x)}^2 \dx \cdot \int_a^b \abs{g(x)}^2 \dx \leq  \int_{-\infty}^{\infty} \abs{f(x)}^2 \dx \cdot \int_{-\infty}^{\infty} \abs{g(x)}^2 \dx. $$
> 
> Taking the limit of $a\to -\infty$ and $b\to \infty$ on the left hand side, gives us the infinite Cauchy-Shawrz analogue, and in particular :
> 
> $$\abs{\angles{f,g}} \leq \norm f_2 \norm g_2,$$ 
> 
> so if both $f,g\in L^2(\RR)$, then their inner product is finite (and actually converges in absolute value).

We can now look for an orthonormal basis and do a similar process as with the Fourier series. However, our main goal is to study functions through their periodicity (namely translation to the left and right), and the only periodic function which is in $E^2(\RR)$ is the zero function. Instead, we will just "extend" what we saw in the finite segment case to all of $\RR$.

# The Fourier Transform in $E^1(\RR)$

>[!def] Definition: The Fourier transform
> For a function $f:\RR \to \CC$ and $\omega \in \RR$ we write:
> 
> $$\hat f(\omega) := \frac{1}{2\pi} \int_{-\infty}^{\infty} f(x)e^{-i\omega x}dx = \angles{f,e^{i\omega x}}.$$
> 
> If this limit exists for every $\omega \in \RR$, we call $\hat{f}:\RR \to \CC$ the **Fourier transform** of $f$.
> We sometimes denote this transform by $\hat{f} = \mathcal{F}[f]$.

We will soon see that this transform is well defined for our functions in $E^1(\RR)$, but first, let's see some examples.

> [!example]- Example: The function $\chi_{[a,b]}$.
> For $a < b $ define the characteristic function:
> 
> $$f(x)=\chi_{[a,b]}(x)=\cases{1&x\in[a,b]\\0&else}.$$
> 
> Computing its Fourier transform, we have:
> 
> $$2\pi \hat{f}(w)= \int_{-\infty}^{\infty} \chi_{[a,b]}(x)e^{-i\omega x}dx = \int_{a}^{b} e^{-i\omega x}dx =\frac{1}{\omega} ie^{-i\omega x}\mid_a^b = \frac{e^{-i\omega a}-e^{-i\omega b}}{\omega i}.  $$
> 
> Note that the computation above is invalid when $\omega=0$ for which we have:
> 
> $$\hat{f}(0)=\frac{1}{2\pi} \int_{-\infty}^{\infty} \chi_{[a,b]}(x)dx=\frac {b-a}{2\pi}. $$
> 
> The function $\hat f(\omega)$ is easily seen to be continuous for $\omega \neq 0$, but you can also check that it is continuous at $\omega = 0$ as well. Also, since $e^{i\omega x}$ is bounded, as $\omega \to \infty$ we see that $\hat{f}(\omega)\to 0$
> 
> More over, when $a=-b$ is symmetric, the expression above is the real function:
> 
> $$\hat{f}(\omega)=\cases{\frac{\sin(\omega b)}{\omega \pi} & \omega \neq 0 \\ \frac{b}{\pi} & \omega = 0.}$$
> 
> <iframe scrolling="no" title="fourier transform characteristic" src="https://www.geogebra.org/material/iframe/id/htkvjguk/width/600/height/274/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="600px" height="274px" style="border:0px;"> </iframe>

>[!example]- Example: The function $e^{-a|x|}$, for $a>0$.
> First we note that $f(x):=e^{-a\abs{x}}\in E^1(\RR)$. Next, we have that
> $$\begin{align}  2\pi \cdot \hat f(\omega) & = \int_{-\infty}^{\infty} e^{-a\abs{x}} e^{-i\omega x}\dx = \int_{-\infty}^{0} e^{(a-i\omega) x}\dx + \int_{0}^{\infty}  e^{(-a-i\omega) x}\dx \\ & = \int_{0}^{\infty}\left(e^{-(a-i\omega)x}+e^{(-a-i\omega)x}\right)\dx=\left[\frac{e^{-ax}e^{i\omega x}}{i\omega-a}-\frac{e^{-ax}e^{-i\omega x}}{i\omega+a}\right]_{0}^{\infty}. \end{align}$$
> 
> Since $e^{i\omega x}$ is bounded by 1, and $e^{-ax}\to 0$ as $x\to\infty$, we conclude that 
> 
> $$2\pi \cdot \hat f(\omega) = \frac{1}{i\omega+a}-\frac{1}{i\omega-a} = \frac{2a}{\omega^2+a^2}. $$

## Basic properties

Before proving some basic results about the Fourier transform, we need to actually show that it is well defined for our functions, namely that $\angles{f,e^{i\omega x}}$ is finite when $f\in E^1(\RR)$. 

>[!lem] Lemma:
> If $f\in E^1(\RR)$, then $\hat{f}(\omega)$ is well defined for all $\omega$ and $\norm {\hat{f}}_\infty \leq \norm f_1$.

>[!proof]- Proof:
> This is a simple upper bound computation:
>    $$\abs{\hat{f}(\omega)}=\abs{\frac{1}{2\pi} \int_{-\infty}^{\infty} f(x)e^{-i\omega x}dx} \leq \frac{1}{2\pi} \int_{-\infty}^{\infty} \abs{f(x)}\abs{e^{-i\omega x}}dx=\frac{1}{2\pi} \norm f_1.$$

>[!remark]- Remark: Generalized inner products
> As we mentioned before, the "inner product" $\angles{f,e^{i\omega x}}$ is no longer a standard an inner product, however there is some method to this madness. This is is a product between a function in $L^1(\RR)$ and $L^\infty(\RR)$, where it is usually between two functions in $L^2(\RR)$. These two pairs of numbers satisfy the simple "equation" $\frac{1}{1}+\frac{1}{\infty} = \frac{1}{2} + \frac{1}{2} = 1$, and as it turns out, this is enough for the "inner product" to be defined. For more details, you should read about [Holder inequality](https://en.wikipedia.org/wiki/H%C3%B6lder's_inequality).

In the Fourier series section, we used $\sin(nx), \cos(nx)$ as our basis. Using the complex exponents is much easier (once we know how to work with them) and we almost get automatically the following results.

>[!claim] Claim: Arithmetic operations
> Let $f\in E^1(\RR)$. Then:
> 1. The Fourier transform is linear, namely $\mathcal{F}(\alpha f + g) = \alpha \mathcal{F}(f)+\mathcal{F}(g)$.
> 2. **Translation->Rotation**: Setting $f_\alpha(x) := f(x+\alpha)$, we have $$\hat{f}_\alpha (\omega) = e^{i\alpha\omega}\hat{f}(\omega).$$
> 3. **Multiplication**: If $\lambda \neq 0$, then setting $g(x)=f(\lambda x)$ we have
>    $$\hat g (\omega) = \frac {\hat{f}(\omega/\lambda)}{\abs{\lambda}}.$$
> 4. **Conjugation**:  $\overline{\cf \left[f\right] (\omega)}=\cf\left[\bar{f}\right] (-\omega)$.

>[!proof]- Proof:
> 1. Follows from the fact that integrals are linear.
> 2. (and 3) Both claims follow from change of parameters:
>    $$\hat{f_\alpha}(\omega) = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(x+\alpha)e^{-i\omega x}dx = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(x)e^{-i\omega (x-\alpha)}dx = e^{i\omega\alpha}\hat f(\omega).$$
> 3. For $\lambda>0$ we have:
> 
>    $$\hat{g}(\omega) = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(\lambda x)e^{-i\omega x}dx = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(x)e^{-i(\omega/\lambda) x}\frac{1}{\lambda}dx = \frac{1}{\lambda}\hat f(\frac{\omega}{\lambda}).$$
> 
>    For $\lambda<0$, the proof is similar.
> 4. $$2\pi \overline{\hat{f}(\omega)} = \overline{\int_{-\infty}^{\infty} f(x) e^{-i\omega x}\dx} = \int_{-\infty}^{\infty} \overline{f(x)} e^{i\omega x}\dx = 2\pi \hat{\overline{f}}(-\omega)$$

If $f\in L^1(\RR)$ and we multiply it by some bounded function $g\in L^\infty(\RR)$ then it is easy to check that $f(x)\cdot g(x)\in L^1(\RR)$, and actually $\norm {f\cdot g}_1 \leq \norm {f}_1 \norm{g}_\infty$ . In this case, we can ask what is the Fourier transform of $f\cdot g$. Probably the most important bounded function we work with is $e^{ix}$ which not only appear in the computation of the Fourier transform, but we also saw it in the claim above where a translation became a rotation. As it turns out the other direction works as well.

>[!claim] Claim: Rotation->translation.
> Let $f\in E^1(\RR)$ and for $c\in \RR$ let $h_c(x):=e^{icx}f(x)$. Then 
> 
> $$\hat{h_c}(\omega)=\hat{f}(\omega-c).$$
> 
> In the sine and cosine notations, we have:
> 
> $$\align{ \cf[f(x)\sin(x)]&=\frac{\cf[f](\omega-c)-\cf[f](\omega+c)}{2i} \\ \cf[f(x)\cos(x)]&=\frac{\cf[f](\omega-c)+\cf[f](\omega+c)}{2} }$$

>[!proof]- Proof:
> This is again a simple computation:
> $$\hat{h_c}(\omega) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{icx}f(x)e^{-i\omega x}dx = \frac{1}{2\pi}\int_{-\infty}^{\infty} f(x)e^{-i(\omega-c)x}dx = \hat f(\omega-c).$$

There is already an interesting phenomenon suggested by these results. When we translated $f$ it transformed into a rotation of $\hat{f}$ and when we rotated $f$ it transformed into a translation in $\hat{f}$. Something similar happened with the multiplication (and conjugation), but more "stable" - multiplication transformed into multiplication (same with conjugation). This duality is very important and we will see that more as we progress. 

Lets see a couple more examples. 

>[!cor] Corollary:
> If $f$ is even (resp. odd) then $\cf[f]$ is even (resp. odd).
> If $f$ is real (resp. pure imaginary), then $\overline{\cf[f](\omega)}=\cf[f](-\omega)$ (resp. $=-\cf[f](-\omega)$).
> In particular, if $f$ is real and even (e.g. cosine functions), then $\hat{f}$ is real and even, and if $f$ is real and odd, then $\hat{f}$ is pure imaginary and odd.

>[!proof]- Proof:
> Take the multiplication identity with $\lambda = -1$, so that $g(x)=f(-x)$. In this case we get that $\hat{g}(\omega)=\hat{f}(-\omega)$. If $f$ is symmetric, then $g=f$, so that $\hat{f}(\omega)=\hat{f}(-\omega)$ is symmetric, and if $f$ is odd, then $g(x)=-f(x)$ in which case 
> 
> $$\hat{f}(-\omega)=\widehat{g}(\omega)=\widehat{-f}(\omega)=-\widehat{f}(\omega)$$
> 
> is odd.
> The second part is proved similarly from the conjugation identity.


## Continuity and derivatives

Our next step is to show some properties on the function $\hat {f}$ itself, and we start by showing that it is continuous.

>[!claim] Claim: The Fourier transform is continuous
> If $f\in E^1(\RR)$, then:
> 1. The function $\hat{f}$ is continuous.
> 2. (The Riemann-Lebesgue lemma): $\limfi{\abs{\omega}} \hat{f}(\omega) = 0$.

>[!proof]- Proof:
> 1. For the second claim, let's consider the following example with $f(x)=e^{-\abs{x}/10}$
>   ![[continuity of Fourier transform.png]]
>  The function itself is drawn in green, and we also draw $f(x)\cdot \sin(10x)$ and $f(x)\cdot \sin(10.2 x)$ in blue and red, where we use sine function instead of complex exponents, just so we can draw them. The transform should be thought of as the integrals over these function.
>   In this example we want to show that since $10$ and $10.2$ are close, their integrals over $f(x)\cdot \sin(10x)$ and $f(x)\cdot \sin(10.2 x)$ are also close. The idea is that (1) if we are near the center the functions themselves are very close so their integrals are close and (2) if we are far away from the center, while this no longer holds, the total area beneath $f(x)$ is very small, so even when multiplying by some sine functions it remains small. Thus, together they will be small.
>   More formally, fix some $M>0$ which "measures" how far we are from the center, then:
>   
>    $$\align{  2\pi\abs{\hat{f}(\omega+h)-\hat{f}(\omega)} & \leq \int_{-\infty}^\infty\abs{e^{-i(\omega+h)x}-e^{-i\omega x}}\abs{f(x)}\dx = \int_{-\infty}^\infty\abs{e^{-ihx}-1}\abs{f(x)}\dx \\  & = \int_{\abs{x}\leq M}\abs{e^{-ihx}-1}\abs{f(x)}\dx + \int_{\abs{x}> M}\abs{e^{-ihx}-1}\abs{f(x)}\dx \\  & \leq \sup_{\abs{x}\leq M}\abs{e^{-ihx}-1} \cdot \int_{\abs{x}\leq M}\abs{f(x)}\dx + 2\int_{\abs{x}> M}\abs{f(x)}\dx \\  & \leq \sup_{\abs{x}\leq M}\abs{e^{-ihx}-1} \cdot \norm f_1 + 2\int_{\abs{x}> M}\abs{f(x)}\dx.}$$
>  
>    Choose your favorite $\varepsilon>0$. Since $\norm f_1 <\infty$, we can choose $M$ big enough so that 
>  
>    $$2\int_{\abs{x}> M}\abs{f(x)}\dx < \frac {\varepsilon}{2}$$
>  
>    Next, for $\abs{x}\leq M$, for all $\abs{h}$ small enough, using the continuity of $e^{-ihx}$ we can make sure that 
>    $$\sup_{\abs{x}\leq M}\abs{e^{-ihx}-1} \cdot \norm f_1<\frac{\varepsilon}{2}.$$
>    Together we see that as $h\to 0$ we have that $\hat{f}(\omega+h)\to \hat{f}(\omega)$, or in other words $\hat{f}$ is continuous.
> 2. The Riemann Lebesgue lemma is proved in a similar fashion. 
>    ![[Riemann Lebesgue.png]]
>    When computing the integral in $f(\omega)$, when we are far away from the center the integral will be very small, regardless of $\omega$. When we are close to the center, we can approximate our function by a step function. For each such step, when $\omega$ is very large, we should expect very high frequency fluctuations so every "positive area" will more or less cancel out with a "negative area".
>    More formally, for any choice of $M>0$ we get a simple upper bound:
>    
>    $$\align{  2\pi\abs{\hat{f}(\omega)} & = \abs{\int_{-\infty}^\infty e^{-i\omega x}f(x)\dx} \leq \abs{\int_{\abs{x}\leq M} e^{-i\omega x}f(x)\dx} + \int_{\abs{x}>M} \abs{f(x)}\dx.}$$
>    
>    As before, for any $\varepsilon>0$, we can choose $M$ big enough so that the second summand is as small as we want :
>    $$\int_{\abs{x}>M} \abs{f(x)}\dx < \frac{\varepsilon}{2}.$$
>    Since our function $f$ is Riemann integrable, we can approximate it by a step function $h$, namely $h(x)=\sum_1^n \lambda_i \chi_{[a_i,b_i]}$ is a finite combination of steps, and $\int_{\abs{x}\leq M}\abs{h(x)-f(x)}\dx < \frac{\varepsilon}{4}$. We can use it to upper bound the first summand:
>    $$\align{ \abs{\int_{\abs{x}\leq M} e^{-i\omega x}f(x)\dx}&=\abs{\int_{\abs{x}\leq M} e^{-i\omega x}\left(f(x)-h(x)\right)\dx + \int_{\abs{x}\leq M} e^{-i\omega x}h(x)\dx} \\ & \leq \int_{\abs{x}\leq M} \abs{f(x)-h(x)}\dx + \abs{\sum_{i=1}^n\lambda_i \int_{\abs{x}\leq M} e^{-i\omega x}\chi_{[a_i,b_i]}(x)\dx} \\ & \leq \frac{\varepsilon}{4}+\sum_{i=1}^n\abs{\lambda_i}\hat{\chi}_{[a_i,b_i]}(\omega). }$$
> We already saw that $\hat{\chi}_{[a_i,b_i]}(\omega)=\frac{e^{-i\omega a}-e^{-i\omega b}}{\omega i}\to0$ as $\omega \to \infty$, and since there are only finitely many such summands ($n$ now is fixed), for all $\omega$ large enough this sum is at most $\frac{\varepsilon}{2}$.
> Putting everything together, we get that for all $\varepsilon>0$ and for all $\omega$ large enough, we have that $\abs{\hat{f}(\omega)}<\varepsilon$, or in other words $\hat{f}(\omega)\to 0$.

Next we turn to derivatives, which also contain an interesting duality.

>[!claim] Claim: Fourier transform and derivatives
> Suppose that both $f\in E^1(\RR)$, and $f'\in E^1 (\RR)$. Then
> $$\cf[f'](\omega)=i\omega \cf[f](\omega).$$
> Similarly, if $xf(x)\in E^1 (\RR)$, then $\hat{f}$ is differentiable and 
> $$\cf[-ixf(x)] = \cf[f]'(\omega).$$

>[!remark] Remark:
> Before we give a proper proof, note that if we are allowed to change the order of derivation and integration, then the second part is almost automatic. However, we don't know that we can do this, and we basically prove it here.


>[!proof] Proof:
> For the first part, we use integration by parts
> 
> $$\align{ 2\pi \widehat{f'}(\omega)&=\int_{-\infty}^{\infty} f'(x)e^{-i\omega x}\dx=f(x)e^{-i\omega x}\mid_{-\infty}^{\infty}+i\omega\int_{-\infty}^{\infty} f(x)e^{-i\omega x}\dx. }$$
> 
> Using the fact that $f(x)=f(0)+\int_0^x f'(t)\dt$ and $\norm {f'}_1<\infty$ is finite, we see that $\limfi{x} f(x)$ exists. Since we also know that $\norm{f}_1<\infty$ is finite, this limit must be zero. Similarly, we get that $\displaystyle{\lim_{x\to -\infty}}f(x)=0$, and since $e^{-i\omega x}$ is bounded, we conclude that 
> 
> $$f(x)e^{-i\omega x}\mid_{-\infty}^{\infty} = 0. $$
> 
> The other summand is simply $2\pi i \omega \hat{f}(\omega)$ which completes the first part of claim.
> 
> For the second part, by definition we have that 
> 
> $$\align{ 2\pi\left(\cf[f]'(\omega) -\cf[-ixf(x)] \right) & =\lim_{h\to 0}\int_{-\infty}^{\infty}f(x)\frac{e^{-i(\omega+h)x}-e^{-i\omega x}}{h}\dx + i\int_{-\infty}^{\infty}xf(x) e^{-i\omega x}\dx \\ & = \lim_{h\to 0}\int_{-\infty}^{\infty}f(x)e^{-i\omega x}\left( \frac{e^{-ihx}-(1-ihx)}{hx}x \right)\dx. }$$
> 
> As $e^z$ is analytic, we can find some constant $C$ such that 
> 
> $\abs{\frac{e^{-ihx}-(1-ihx)}{hx}} < C\abs{hx}^2$ 
> $\abs{\frac{e^{-ihx}-(1-ihx)}{hx}} <C\abs{hx}^2$ 
> $\abs{\frac{e^{-ihx}-(1-ihx)}{hx}}< C\abs{hx}^2$ 
> $\abs{\frac{e^{-ihx}-(1-ihx)}{hx}}<C\abs{hx}^2$ 
> 
> for $\abs{hx}<1$. If $\abs{hx}>1$, then $\abs{\frac{e^{-ihx}-(1-ihx)}{hx}}<3$. Using the fact that $\norm {xf(x)}_1 <\infty$, the same ideas from before show that the limit is zero.


>[!example] Example: Fourier transform of the Gaussian
> Letting $f(x)=e^{-x^2}$, its Fourier transform is 
> 
> $$\frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-x^2}e^{-i\omega x}\dx,$$
> 
> which doesn't seem to simple to compute.
> Instead, let us use the fact that we can take the derivative beneath the sign of the integral to get that :
> 
> $$ 2\pi \hat{f}'(\omega)= \int_{-\infty}^{\infty} e^{-x^2}(-ix)e^{-i\omega x}\dx = \frac{i}{2} \int_{-\infty}^{\infty} (-2x)e^{-x^2}e^{-i\omega x}\dx.$$
> 
> Taking $u(x)=e^{-x^2}$ , and $v(x)=e^{-i\omega x}$, our integral is $u'(x)v(x)$ so we can do integration by parts. It follows that 
> 
> $$ 2\pi \widehat{f}'(\omega)= \frac{i}{2} e^{-x^2}e^{-i\omega x}\mid_{-\infty}^{\infty} - \frac{1}{2}\omega \int_{-\infty}^{\infty} e^{-x^2}e^{-i\omega x}=\pi\omega \hat{f}(\omega).$$
> 
> The solution to the differential equation $\hat{f}'(\omega)=\frac{\omega}{2}\hat{f}(\omega)$ is $ae^{-\omega^2/4}$. Finally, since
> 
> $$a = \hat{f}(0)=\frac {1}{2\pi} \int_{-\infty}^{\infty} e^{-x^2}\cdot 1 \dx = \frac{1}{2\sqrt{\pi}},$$
> 
> we conclude that 
> 
> $$\hat{f}(\omega) = \frac{1}{2\sqrt{\pi}} e^{-\omega^2/4}.$$


<- [[Fourier Series|Previous: Fourier Series]]    ,    [[Fourier Course Information#Table of contents|Back to table of contents]]    ,   ??? ->









