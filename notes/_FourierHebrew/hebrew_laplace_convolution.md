---
title: קונבולוציה
author: אופיר דוד
category: התמרות פורייה
layout: post
dir: rtl
cssclasses:
  - hebrew
---
$\newcommand{\Hs}[1]{H_{[#1, \infty)}}$
בדיוק כמו בהתמרת פורייה, גם בהתמרת לפלס נרצה לדעת מה זו ההתמרה של מכפלה של פונקציות, וגם פה זה יוביל אותנו לפעולת הקונבולוציה. בנוסף, בגלל שהתמרת לפלס היא על פונקציות שמוגדרות ב $[0,\infty)$ אז החישוב הוא אפילו יותר פשוט.

נזכיר שעבור פונקציות עם תומך ב $[0,\infty)$, כלומר פונקציות המתאפסות מחוץ לקבוצה הזאת : $f(x)=0, x<0$, נח לחשוב עליהן כ $H(t)f(t)$ כאשר $H(t)$ היא פונקציית הביסייד, ועבור פונקציות כאלו כאשר $x\geq 0$ נקבל ש 
$$\left[\;H(t)f(t)\;*\;H(t)g(t)\;\right]\;(x) = \int_{-\infty}^\infty H(x-t)f(x-t)\cdot H(t)g(t)\dt = \int_{0}^\infty H(x-t)f(x-t)\cdot g(t)\dt = \int_{0}^x f(x-t)\cdot g(t)\dt$$
כלומר, האינטגרל בתוך הקונבולוציה הוא תמיד על קטע סופי $[0,x]$ .
בדוגמא למטה אנחנו רואים את $H(t)g(t)$ באדום, את $H(x-t)f(x-t)$ בסגול, ואת המכפלה שלהם שנמצאת רק בתחום $[0,x]$ בשחור.
<iframe src="https://www.desmos.com/calculator/ojkqu75uok?embed" width="800" height="400" style="border: 1px solid #ccc" frameborder=0></iframe>

> [!מסקנה] מסקנה: קונבולוציה על פונקציות על מספרים חיוביים
> אם $f,g$ נתמכות ב $[0,\infty)$ אז הקונבולוציה שלהם מקיימת:
> $$.\dboxed{(f*g)(x)=\cases{\int_0^x f(x-t)g(t)\dt & x\geq 0 \\ 0 & x<0}}$$

> [!טענה] טענה: מכפלה של פונקציות הביסייד
> לכל $a,b\in \RR$ מתקיים ש 
> $$.(H(t-a)*H(t-b))(x) = (x-a-b)H(x-a-b)$$

> [!הוכחה]- הוכחה:
> חישוב של הקונבולוציה יתן:
> $$(H(t-a)*H(t-b))(x)= \int_{-\infty}^\infty H(x-t-a)\cdot H(t-b) \dt= \int_{b}^\infty H(x-t-a)\dt= \int_{-\infty}^{x-a-b} H(s)\ds$$
> אם $x-a-b<0$ אז האינטגרנד הוא זהותית אפס בתוך התחום $(-\infty,x-a-b]$. אחרת הוא שווה ל 1 ב $s\geq 0$ ולכן נקבל ש
> $$\int_{-\infty}^{x-a-b} H(s)\ds=\left\{\begin{array}{lr}0 & :x<a+b \\ x-a-b & :a+b \leq x\end{array}\right\}=(x-a-b)\cdot H(x-a-b)$$

התכונות הרגילות של הקונבולוציה נכונות גם במקרה שלנו:

> [!טענה] טענה:
> יהיו $f,g,h$ פונקציות הנתמכות ב $[0,\infty)$. אז בכל מקום בו הקונבולוציה קיימת מתקיים ש:
> 1. **אסוציאטיביות**: $f*(g*h)=(f*g)*h$.
> 2. **קומוטטיביות**: $f*g=g*f$.
> 3. **לינאריות**: לכל $\alpha \in \CC$ מתקיים $(f+\alpha g)*h=f*h+\alpha f*g$.

> [!משפט] משפט הקונבולוציה
> יהיו $f,g$ פונקציות הנתמכות ב $[0,\infty)$, ונניח שקיימים קבועים $K_f, K_g, s_0$ כך ש $|f(t)|\leq K_fe^{s_0t}$ ו $|g(t)|\leq K_g e^{s_0t}$. אז:
> 1. לכל $x\geq 0$ מתקיים ש
>    $$.|(f*g)(x)|\leq K_fK_gxe^{s_0x}$$
> 2. לכל $s>s_0$ ההתמרה של הקונבולוציה מוגדרת היטב ומתקיים ש 
>    $$.\cl\left[f*g\right](s)=\cl[f](s)\cdot \cl[g](s)$$

> [!הוכחה]- הוכחה:
> 1. עבור $x\geq 0$ מתקיים ש 
>    $$.|(f*g)(x)|\leq \int_0^x|f(x-t)|\cdot|g(t)|\dt\leq \int_0^xK_fK_ge^{s_0(x-t+t)}\dt=K_fK_ge^{s_0x}\int_0^x1\dt=K_fK_ge^{s_0x}x$$
> 2. מהחלק הראשון נקבל שהתמרת לפלס של $f*g$ מוגדת לכל $s>s_0$, ושווה ל:
>    $$.\cl[f*g](s) = \int_0^\infty \left(\int_0^tf(t-y)g(y)\dy\right)e^{-st}\dt$$
>    בגלל שכל האינטגרלים מתכנסים בהחלט, ניתן להשתמש ב[[hebrew_convolution|משפט פוביני]] כדי להחליף סדר אינטגרציה. התחום מוגדר ע"י $0\leq y\leq t$ ולכן $$.\int_0^\infty \left[\int_0^t (\cdots) \dy \right]\dt = \int_0^\infty \left[\int_0^\infty \chi_{[0,t]}(y)(\cdots) \dy\right] \dt = \int_0^\infty \left[\int_0^\infty \chi_{[0,t]}(y)(\cdots) \dt \right]\dy= \int_0^\infty \left[\int_y^\infty (\cdots) \dt \right]\dy$$
>    ![[integration order.png|400]]
>    סה"כ נקבל ש 
>    $$.\align{\cl[f*g](s) &= \int_0^\infty \left(\int_y^\infty f(t-y)g(y)e^{-st}\dt\right)\dy = \int_0^\infty g(y)e^{-sy}\left(\int_y^\infty f(t-y)e^{-s(t-y)}\dt\right)\dy \\ &= \int_0^\infty g(y)e^{-sy}\left(\int_0^\infty f(t)e^{-st}\dt\right)\dy = \cl[g](s)\cdot \cl[f](s)}$$
>    

## דוגמאות

> [!דוגמא] דוגמא 1
> [[hebrew_laplace|כבר ראינו]] שבהינתן $f$ רציפה למקוטעין, אם מגדירים את $g(t)=\int_0^tf(x)\dx$ אז $\cl[g](s)=\frac{1}{s}\cl[f](s)$ כאשר הרעיון היה להשתמש בתכונת הנגזרת, ואז להפוך אותה כדי לקבל אינטגרל. בנוסף, אנחנו יודעים ש $\frac{1}{s}=\cl[1](s)$ (או יותר נכון $\frac{1}{s}=\cl[H(t)](s)$) ולכן יש לנו מכפלה של התמרות. מצד שני, ניתן לכתוב $g(t)=(f(t)*H(t))(t)$ ולכן בעצם התוצאה הזאת נובעת גם ממשפט הקונבולוציה:
> $$.\cl[g](s)=\cl[H(t)*f(t)](s)=\cl[H](s)\cl[f](s)=\frac{1}{s}\cl[f](s)$$
