---
layout: home
title: Fourier Analysis notes
permalink: /
---

# The Fourier Analysis notes - Jekyll Gitbook 

This code is used to generate the [Fourier Analysis notes website](https://totallyreal.github.io/Fourier_Notes/) that I created when I gave this course at the Technion (2023).
The main goal of this website was to enhance the usual notes using all the interactivity that our internet browsers provide us, starting from simple hyperlinks and table of contents, interactive text (e.g. show\hide sections), animations, interactive programs, etc.

This is still very much a work in progress, and there are several big issues that hopefully one day I will complete. As I am a mathematician and not a website developer, some of these might take much more time. 

The rest of this document is to remind myself what I need to do when I have the time and energy. If you want, I would appreciate the help, in particular in the more technical parts of the code behind the website.

You can contact me at [totallyRealField@gmail.com](mailto:totallyRealField@gmail.com).

---

## The mathematical notes:
Lets start with the simple problem.

The course was given to a Hebrew speaking (and listening) audience. However, as Hebrew goes against everything natural in the world, and more specifically, it goes from right to left, I could not use it when I first started to work on the website. Once I finally added the Hebrew support, I moved to Hebrew notes, so now the website is half English and half Hebrew.

Of course, I need to translate the two parts into the other language, and once this is done, separate the website into two (as while supporting Hebrew is hard enough, having both Hebrew and English together is even harder for our poor browsers to understand).

To write the notes locally, I use obsidian, so they are written in standard markdown + the Obsidian ["callout" environment](https://help.obsidian.md/Editing+and+formatting/Callouts), which I use for Theorems, Lemmas, Examples, etc. You can find these notes under the "notes" directory.

Other than that, if you happen to read the notes and have suggestions or ideas for improvement, I would be happy to hear about them.

---

## The website design:
Right now there is not too much of a "design" to the website. There is the standard design coming from the original [Jekyll-Gitbook repository](https://github.com/sighingnow/jekyll-gitbook) that I forked, plus some basic components that I created for the notes themselves. 

We all know how unappealing and daunting big blocks of text can appear, especially when learning a new subject (not to mention mathematics). Therefore, it is important to enhance their visual appeal by incorporating colors, design elements (such as frames and images), and formatting to make them more engaging and easier to navigate.

I need to find better ways of doing that (using my limited knowledge in the subject...).

---

## Coding the website:
There are all sorts of issues coming from the website code itself. The website is generated using [**Jekyll**](https://jekyllrb.com/), and in particular the [Jekyll-Gitbook repository](https://github.com/sighingnow/jekyll-gitbook).
It is not that hard to work with for simple changes, but it becomes increasingly harder as you advance, in particular if writing websites is not your primary work in life.

I had to add some latex support, implement the Obsidian callout environment, some wikilinks etc, but all was done in a sort of roundabout way. For example, Jekyll uses Ruby for extra scripts, and since I didn't want to learn Ruby just for that , I use it to just run instead python scripts. This is too dirty for my liking, and I would like to improve it.

Of course, some of the design issues will come down eventually to the coding part (and not just some simple css change).

---

## Some more stuff

There are other stuff, which I would be happy to have eventually:

1. While I developed this website to replace the standard static pdf notes, I would like to have the option of exporting it as pdf. This requires the markdown notes to supprt this time of export. For example, if there is an animation, then it should appear in the browser, but be replaces in the pdf version.

2. While markdown files are verstile when it comes to exporting them into different formats, and it is really easy working with Obsidian, this process still has its drawbacks. In particular the support for math is not as good as I would like it to be, and it is even worse when Hebrew is involved.
  
   However, I do like working with [LyX](https://www.lyx.org/), and it handles both Math and Hebrew quite well. I would really like to be able to convert lyx documents to md files. This way, I can also convert all my other notes that I written over the years. There is the [pandoc](https://pandoc.org/) program which helps with conversions, but as usual it broke down when I tried to convert latex files with Hebrew...

3. I would really like to have support for running code in the website, like google colab and python. Such support could be used for interesting exercises along the way, and more engaged learning. For now I use links to google colab, but it would be nice to keep everything in site.



---

**My homepage**: [https://prove-me-wrong.com/](https://prove-me-wrong.com/)

**Contact**:	 [totallyRealField@gmail.com](mailto:totallyRealField@gmail.com)

**Ofir David**

