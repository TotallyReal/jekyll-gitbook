---
layout: post
---
# What is linear regression

In the land of machine learning, one of the most basic problems with an interesting solution is the one called linear regression.

## Moving cars and measurements errors

To understand it, consider this simple problem where we have a video of a car driving at constant speed, and you want to find out what is that speed. Luckily for us, at each frame of the video you can find the timestamp, namely how many seconds passed from the beginning of the video. Furthermore, there are markings on the road, so we can also measure how much distance the car passed.

To find the speed, is now a simple matter of dividing the distance the car passed by how many time it took. For example, if in 10 seconds it moved 222 meters, then its speed is 22 meters per second (or equivalently 79.2 kilometers per hour).

However, there is one big issue with this process - we don't know how accurate are our measurements. For example, if the marking on the road are every 5 meters, then you might only know that the car moved between 220 to 225 meters, and you approximated that it is near the 222 mark. Same problem with the timing. Changing our reading slightly to 225 meters in 9.5 seconds means that the car drove at speed approximately 85 kilometers per hour rather than just 79.

So how do we fix this, and get a "better" approximation to the speed? One way, is instead of one such measurement, we take several measurements and find the "best" approximation for such data. More formally, our data are pairs $(x_i, t_i),\;i=1,...,m$ of  distance and time, and approximating them with constant speed growth means that they are close to being on the line
$$x = a_0 + v\cdot t.$$
This means that at time $t=0$ the car is at position $a_0$ and it drive at speed $v$. Geometrically, this means that we are trying to approximate the blue dots below with a red line:

IMAGE

## How good is the approximation?

We now have an interesting experiment. We have 
1. **The original process**, namely the moving car, which can be described by a straight line,
2. **The data points**, which were supposed to be on the line, but the measurement errors moved them out a little bit.
3. **The approximation**, where we try to find back the line which is the best approximation.

While both step (1) and (2) are straight forward, what does it mean to look for the best approximation? To answer it we must determine to our self first how do we measure how good an approximation is, and only then a "best" approximation has a meaning. For example, at time $t_i$ we measured the distance $x_i$ while in truth it should have been $\tilde{x}_i:=a_0+v\cdot t_i$, so we want $|x_i-\tilde{x}_i|$ to be as small as possible. However, can we make it small for all $i$ simultaneously, or in other words the "size" of the vector $(x_1-\tilde{x}_1,...,x_m-\tilde{x}_m)$? Consider two ways of measuring this:
1. $\ell^\infty$ distance: We want $\max_i|x_i-\tilde{x}_i|$ to be as small as possible.
2. $\ell^1$ distance:  We want $\sum_i|x_i-\tilde{x}_i|$ to be as small as possible.

In the first case, we want the worst possible error to be as small as possible. This seems reasonable, but what happens if there was a huge error in just one of our data points? trying to fit it will cause our model to be bad.
In the second case, if one data point is bad, but the rest are very small, it can still be a very good approximation. 

Whether you prefer good approximations using $\max_i|x_i-\tilde{x}_i|$ or alternatively $\sum_i|x_i-\tilde{x}_i|$ depends on the model that you choose. There are many more such functions (usually called **norms**), and there is one more important in the middle between those two, the $\ell^2$ distance:
$$\sum |x_i-\tilde{x}_i|^2.$$
Here too we take the sum and not the maximum, so several "big" errors might not hurt too much like in the $\ell^\infty$ distance, but on the other hand since we take the square, when ever an error $|x_i-\tilde{x}_i|$ is big, it square is larger (with respect to squares of small errors), so we are less forgiving than the $\ell^1$ distance.

The interesting part about this new distance, is not only that it is a "compromise" between the two distances defined above, but it has also connection to an algebraic structure making it much easier to study.

## The inner product