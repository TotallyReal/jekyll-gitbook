---
title: Fourier Analysis - Motivation
author: Ofir David
category: Fourier Analysis
layout: post
---
Course: [[Fourier Course Information]]
# What do we analyze?

The "**Fourier Analysis**" is one of the most useful tool when we try to study real (and complex) functions, which naturally appear in many places, for example:
 - **Physics**: represent position, speed, force, temperature, etc. ,
 - **Digital representations**: like pixels in images, sound in audio file, or movement in animation
 - **"Abstract" quantities**: stock market prices, or even measuring "popularity" in social media sites.

These "real functions" come in several flavors, according to their domains, and the most common types are:
1. Functions on the real line:  $f:\RR \to \RR$, 
2. Periodic functions, namely $f:\RR \to \RR$, with some period $T>0$, so that $f(x+T)=f(x)$,
3. Finite and discrete domain $f:\{1,...,n\} \to \RR$, or 
4. Infinite and discrete domain $f: \ZZ \to \RR$ , or as we usually call them sequences. 

Having so many "real functions" types, which represent so many objects in our world, it is very important to find mathematical structures and tools to study them. We already learned some of them in basic courses in calculus and algebra:
1. First, we need to choose the **type of functions**: Bounded, Continuous, differentiable, piecewise continuous, integrable etc.
2. **Linear algebra**: Usually this chosen family forms a vector space, allowing us to use all the tools from linear algebra.
3. **Calculus**: Using the real line's structure, we can look at continuity, derivative, integral, etc.
4. **Geometry**: We can also measure the "size", namely the norm, of a function in several ways. For example, the maximum distanance from zero $\norm{f}_\infty = \sup|f(x)|$, or measure the area beneath the graph of the function (in absolute value):    
   >[!figure]- Figure:
   >
   > ![[area.jpg|400]]
   
    These norms satisfy the well known triangle inequality $\norm{f+g} \leq \norm f + \norm g$, which let us construct a **geometry** on our space, since we can measure distances, e.g. 
    
    $$dist(f,g):=\norm{f-g}.$$
    
5. **Angles**: More generally, we can think of "angles" between vectors, and draw intuition from the standard Euclidean spaces (e.g. the Pythagoras theorem). More formally, we add an inner product structure (as we shall see [[Inner product spaces - a reminder|soon]]).	

The main idea in Fourier analysis, is that we add one more very interesting structure:

5. **Symmetry**: These families usually have very nice "symmetries". Usually we think of symmetries like reflections - we have the original object, we take its reflection though a mirror, and somehow get the "same" object (or at the very least it looks the same). Something similar happens with our real functions - for example, functions on the real line are "symmetric" to left and right translations: we can "move" functions to the left and right to get another function in the family :
   >[!figure] Figure:
   >
   >![[translation.jpg|600]]
   >
   > $$ f(x) \mapsto f(x+c) $$
    
   We can think of this as advancing in position or time (depending on what our functions represent).

This "symmetry" structure seems simple at first, however it leads to very interesting questions. Are there interesting "patterns" that our functions exhibit under this symmetries? For example, the function "repeats" itself when we move to the left or right? Are there "basic" patterns that we should look for when given such a function? This "pattern" search question is the main goal of our course, and in a sense the "Fourier analysis" can be thought of as pattern investigation of these functions.

> [!Remark]- Remark:
> In our course we will mainly be interested in the periodic functions, and functions on the real line. In this study, we will naturally also see the space of infinite sequences.
> The finite discrete Fourier transforms are also very important, but will not be part of this course. However, they appear frequently in the theoretical side of computer science, if you wish to study more about them.

---
# "Real life" problems:

Let see some examples for this pattern search in real life problems.

## Image compression

In our modern day life, we take images and videos of almost everything that happens to us. More over, as our technology improves, we can save more and more information in each image. However, the problem with this approach is that this information takes a lot of space. One solution is to keep buying new space, whether it is a new hard drive or extra cloud space. Another solution is to try compressing the information instead. There are many compression algorithms and some of which (for example, the JPEG image compression) use ideas based on Fourier transforms.
### Pixelwise compression:

Suppose we have a grayscale image file, where the color of each pixel is represented by an integer in $[0,255]$ going from black at $0$ all the way to white at $255$. One very simple way to compress the image, is to change the pixel value from 255 options to something smaller, for example 16 or 8. This already gives us some compressions, and for some images it will be hard to notice the changes.

![[Euler pixel compressions.png|600]]

 However, as the number of pixel values decreases, we start to see jumps in colors. This is not too surprising, because we are trying to approximate our image by step (piecewise constant) functions. So even though two nearby pixels can have nearby color values originally, we can still have a jump in the color. This is because our compression looks at each pixel separately. To improve our compressions, we can try to exploit "patterns" in the image. For example, if there is a gradient section, namely the color changes linearly from one place to another, then we would only need two parameters to describe it (e.g. to write $ax+b$). 
### Pattern compression:

This idea of looking for patterns is measured in a sense in the Fourier transform coefficients. The Fourier transform "decomposes" the full image (and not each pixel separately) into sine and cosine wave patterns with weights which determines how "strong" that pattern is in the picture. 

For example, in a $10\times10$ pixels image, there are $10\cdot 10=100$ possible patterns, which you can see on the figure below on the left. Given any such image, we can for example keep only the "first" $[1,i]\times [1,j]$ patterns, and plot it on the $(i,j)$ position as we see on the right with the cat picture. Note for example that the picture at the $(7,7)$ position only has $7\cdot 7=49$ out of the $100$  patterns from the original picture (less than half!) and is already quite similar to the final image.

| ![[Fourier patterns.png]]   | ![[cat patterns.png]]   |
|---|---|
|   |   |

As in turns out, most weights in this pattern decomposition are quite small, and removing their corresponding patterns completely doesn't change the image too much. Thus, in general we can throw away all the information about this small weight waves, and get a compression without losing too many details:

![[Euler  FFT compressions.png|600]]

For more details and some actual python code which runs the compressions above: [Python image compression](https://colab.research.google.com/drive/1y2M0qtu4bkMG5eILY_LVRvEEK61UD3OS?usp=sharing)

Some interesting YouTube videos about image compressions:
- [Youtube: JPEG compression - By Computerfile](https://www.youtube.com/watch?v=Q2aEzeMDHMA)
- [Youtube: FFT image compression - By Steve Brunton](https://www.youtube.com/watch?v=gGEBUdM0PVc&list=PLMrJAkhIeNNT_Xh3Oy0Y4LTj0Oxo8GqsC)

To summarize, one way (of many) to think about Fourier transform is as extracting patterns from our data and the a weight for each pattern. If the data has nice "wavy" data, then the Fourier transform can help understanding it.

## Music and noise reduction

When playing music on a piano (and many other instruments as well), we usually play different notes that sound "harmonious" together. For example, the chord `C` on the piano is a combination of the notes `C,E,G`. Each of these notes correspond to a "pure" sine sound wave with a given frequency, and when they are all played together, these waves sum up as can be seen in the image below.

| ![[piano keyboard.png\|314]]   | ![[piano notes.png\|500]]   |
|---|---|
|   |   |

Suppose now that we can hear this combination of notes together. Can we find out what are the notes being played? For example, can we extract from the `C+E+G` orange wave in the image, the `C,E,G` red, green and blue waves? This is one type of "pattern" search that Fourier transformation allows us to do.
More over, when we are listening to the chord, there is probably a lot of background white noise, which we should think of as something "without any pattern". Is it possible to extract from the "noisy" chord the original notes as well? This too can be done using Fourier transformation.

See for example:
- [Youtube: Denoising data with Fourier transformation - By Steve Brunton](https://www.youtube.com/watch?v=s2K1JfNR7Sc)
- [Youtube: Extract Musical Notes from Audio in Python with FFT - By Jeff Heaton](https://www.youtube.com/watch?v=rj9NOiFLxWA)
- [Openprocessing: Visualizing Fourier transformation of audio](https://openprocessing.org/sketch/1051721)

## Channel separation

When opening a website online, usually our computer sends a request to our internet provider to send us exactly the information needed to view the website. However, when we watch television, or listen to the radio, our television and radio (usually) don't send any requests, and instead get all the possible channels that we paid for, in a single stream of information. So the question is, how do they separate this single stream into the different channels?

%% add some image with radio waves %%

Here too, one of the ways of extracting these different channels is by in a sense coding them on different "Fourier patterns". Once we find these patterns from the signal that we get, we can use it to reconstruct the original information sent over it.


---
# The tools of our craft

What type of tools and ideas are we going to use?

## Divide and conquer - the orthonormal basis
One of our main tools, is to decompose our large space of functions into smaller sections (=patterns), where we can understand each section separately, and once we do, combine them back together to understand our original function.
You already learned about this idea back in your first course in linear algebra, which had the mysterious name of eigenvalues and eigenvectors. This was further expanded in the second course, about inner product spaces, where you saw the importance of geometry and working with orthonormal basis of eigenvalues.
Here, we would take this idea to the next stage - the infinite dimensional space of functions - where our building blocks orthonormal basis would consist of the sine and cosine functions.

## Sine and cosine and the complex plane
As mention several times, the sine and cosine functions are going to be our building blocks for the Fourier transform. At first glance, it is not clear why it happens and why they are so important, and in particular each one of one them on its own. However, they become quite interesting once combined - they are just two parts ($x$ and $y$ coordinates) of the same very simple and very important process: **Moving at constant speed on a circle**. This clues us as to why these trigonometric functions arise so naturally - a lot of natural phenomena have natural "rotational" behavior, and when we see the sine or cosines function, it is usually just because we don't see the "whole 2 dimensional picture".

>[!figure]- Figure:
> ![[pendulum.png|209]]                    ![[solar system.jpg#right|500]]

More over, this is also why many of the computations that will be done with sines and cosines in our course can be much more natural in the 2-dimensional complex plane.
Recall (or learn in a few weeks) that by definition we have that 
$$e^{i\theta} := \cos(\theta) + i\sin(\theta),$$
namely the sine and cosine functions are the imaginary and real parts of the nice (complex) exponential function. While complex functions seem a bit more complicated than real functions, they are in many ways much simpler, and in particular the exponential function is quite easy to work with. For example, it satisfies the well known exponential property of $e^{z+w}=e^z\cdot e^w$. While we won't necessarily use this during the course, since complex functions are not a prerequisite, once you feel more at ease with the complex exponential function, you should go over the material and translate it to its complex notation.

However, as a small taste for why this rotational behavior is so important, consider the following spring:

![[The Fourier spring.gif|500]]

Is the string moving to the right (which is our space's "symmetry" action) or is it rotating around its axis?

The rainbow colors might help to answer this question, but without them it would be impossible to decide. Indeed, the exponential property basically says that translation to the right and left $\theta \mapsto \theta + \phi$ is exactly the same as rotating since $e^{i(\theta+\phi)}=e^{i\theta} \cdot e^{i\phi}$ (as an exercise, think what it means in the language of eigenvalues and eigenvectors). This transformation between left and right translation, and the simpler rotation is what stands at the mathematical heart of the Fourier transform.

# Some mathematical applications

## Differential equations

Another important property that the sines and cosines (and even better, the exponential function) have, is that it is easy to differentiate them. More specifically $\sin'(x)=\cos(x)$ and $\cos'(x)=-\sin(x)$. Such relations make it much simpler to solve differential equations where the functions are combinations of these sine and cosine functions. Luckily for us, the Fourier transform shows that most of the interesting functions can be written as such combinations, and this is quite useful for solving general differential equations.

## Number and group theory

These Fourier transforms, and in particular it discrete finite versions, appear frequently in number theory when studying finite groups and fields. For example, they appear when studying Diophantine equations, namely integer solution for integral equations (e.g. solutions to $x^2 + y^2 = n$ for some integer $n$). In this area the "Fourier transforms" are usually called group representations.

%%## Probability%%

%%add here%%


[[Fourier Course Information#Table of contents|Back to table of contents]]    ,    [[Inner product spaces - a reminder| Next: Inner product spaces]]-> 

