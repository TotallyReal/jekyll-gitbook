---
title: נוסחת פלנשרל
author: אופיר דוד
category: התמרות פורייה
layout: post
dir: rtl
cssclasses:
  - hebrew
---
# נוסחת פלנשרל

אם נחזור שוב לעולם של טורי פורייה, אז יכולנו להשתמש שם בשוויון פרסיבל ולקבל שעבור פונקציה $f:[-\pi,\pi]\to\CC$ רציפה למקוטעין עם מקדמי פורייה $a_n,b_n$ מתקיים ש
$$.\norm{f}_2^2=\frac{\abs{a_0}^2}{2}+ \sum_1^\infty \left(\abs{a_n}^2+\abs{b_n}^2\right)$$

כאשר  המקדמים שלנו הם ההתמרה $\hat{f}(\omega)$ שמוגדרים לכל מספר ממשי, לכן היינו מצפים לקבל שוויון (עד כדי קבוע) מהצורה:
$$.\norm{f}_2^2=C\int_{-\infty}^\infty \abs{\hat{f}(\omega)}^2\dom=C\norm{\hat{f}}_2^2$$

אבל, מייד יש לנו בעיות עם ההגדרה הזאת - עד עכשיו ההתמרה הוגדרה עבור פונקציות שעבורן $\norm f_1<\infty$ והן לא בהכרח מקיימות ש $\norm {f}_2 <\infty$ וגם הכיוון ההפוך לא נכון. למזלנו יש הרבה פונקציות שעבורן שתי הנורמות האלו סופיות, ואז הטענה הזאת תהיה נכונה.

> [!משפט] משפט פלנשרל:
> יהיו $f,g\in E^1(\RR)\cap E^1 (\RR)$ אז:
> 1. ההתמרות $\hat{f}, \hat{g}$ גם נמצאות ב $E^2(\RR)$,
> 2. מתקיים ש:
>    $$\int_{-\infty}^\infty \hat{f}(\omega) \overline{\hat{g}(\omega)} \dom = \frac{1}{2\pi} \int _{-\infty}^\infty f(x)\overline{g(x)} \dx$$
>    או בכתיב של מכפלות פנימיות $2\pi\angles{\hat{f}, \hat{g}}=\angles{f,g}$,
> 3. ובפרט מתקיים ש $\norm{f}_2=\norm{\hat{f}}_2$.

> [!הוכחה]- הוכחה:
> הרעיון באופן כללי הוא החלפת סדרי אינטגרציה, ואם מותר לנו לעשות אותם אז "קל" להראות שהטענה נכונה. נראה שכאשר ל $f,g$ יש תומכים סופיים, כלומר קיים $M>0$ מספיק גדול כך ש $f(x)=g(x)=0$ עבור $|x|>M$, אז ההחלפות מותרות. באופן כללי, יש צורך להשתמש בקירובים של פונקציות כלליות ע"י צמצום שלהם לקטעים סופיים, כלומר $f_M(x):=f(x)\cdot \chi_{[-M,M]}$ אבל לא נכנס לפרטים האלו כאן.
> 
>נתחיל גם עם ההנחה שגבולות אינטגרציה ששואפים ל $\pm \infty$ באותו קצב, ואז נראה איך נפתרים מזה. תחת ההנחות האלו נקבל ש 
> 
>$$\align{\int_{-N}^N \hat{f}(\omega) \overline{\hat{g}(\omega)} \dom & = \frac{1}{4\pi^2} \int_{-N}^N \left(\int_{-\infty}^\infty f(x)e^{-i \omega x} \dx \overline{\int_{-\infty}^\infty g(y)e^{-i \omega y} \dy} \right)\dom \\ & = \frac{1}{4\pi^2} \int_{-N}^N \left(\int_{-M}^M f(x)e^{-i \omega x} \dx \overline{\int_{-M}^M g(y)e^{-i \omega y} \dy} \right)\dom \\ & = \frac{1}{2\pi} \int_{-M}^M \int_{-M}^M  f(x)\overline{g(y)} \left( \int_{-N}^N\frac{e^{-i \omega (x-y)}}{2\pi} \dom \right)\dx \dy} $$
>
>אם נשאיף את $N\to\infty$ אז נקבל את פונקצית דירק בנקודה $x-y$ באינטגרל הפנימי, לכן סה"כ האינטגרל למעלה יהיה שווה ל
>$$.(*)=\frac{1}{2\pi} \int_{-M}^M f(x)\overline{g(x)} \dx=\frac{1}{2\pi} \int_{-\infty}^\infty f(x)\overline{g(x)} \dx$$
> 
> אם נבחר $f=g$ אז נקבל ש 
> $$.\limfi{N}\int_{-N}^N \abs{\hat{f}(\omega)}^2 \dom = \frac{1}{2\pi} \int_{-\infty}^\infty \abs{f(x)}^2 \dx$$
> פה האינטגרלים הם על פונקציות אי שליליות, ולכן הקצב שאיפה ל $\pm \infty$ בגבולות האינטגרציה לא משנה את ההתכנסות, ולכן נקבל ש $\norm {\hat{f}}_2^2= \frac{1}{2\pi}\norm{f}_2^2$.
> אם נחזור עכשיו לחישוב הראשון למעלה, אז נוכל להשתמש באי שוויון קושי שוורץ כדי לקבל ש 
> $$.\int_{-N}^N \abs{\hat{f}(\omega) \overline{\hat{g}(\omega)}} \dom =\angles{|\hat{f}|,|\hat{g}|} \leq \norm{\hat{f}}_2 \norm{\hat{g}}_2 = \frac{1}{4\pi^2}\norm{f}_2 \norm{g}_2 < \infty $$
> זה אומר שהאינטגרל מתכנס בהחלט, ולכן גם בלי הערך המוחלט הוא מתכנס, ללא קשר לקצב שאיפת הגבולות אינטגרציה ל $\pm \infty$. זה מסיים את ההוכחה עבור פונקציות עם תומך סופי.

# דוגמאות

> [!דוגמא] דוגמא: הפונקציה $e^{-a|x|}$ עבור $a>0$
> ראינו כבר שההתמרה של הפונקציה הזאת היא $\cf[e^{-a|x|}](\omega)=\frac{a}{\pi(\omega^2+a^2)}$. אם נחשב את הנורמה של הפונקציה נקבל ש
> $$.\norm{e^{-a|x|}}_2^2 = \int_{-\infty}^\infty e^{-2a|x|}\dx=2 \int_{0}^\infty e^{-2ax}\dx=\frac{e^{-2ax}}{-a}\mid_0^\infty = \frac{1}{a}$$
> מצד שני, שימוש בפלנשרל נותן ש
> $$.\int_{-\infty}^\infty \left(\frac{a}{\pi(\omega^2+a^2)}\right)^2 \dom = \frac{1}{2\pi} \frac{1}{a}$$
> אם נעביר אגפים ונשתמש בזוגיות של הפונקציה, נקבל ש
> $$.\int_{0}^\infty \left(\frac{1}{(\omega^2+a^2)}\right)^2 \dom = \frac{\pi}{4a^3} $$



> [!דוגמא] דוגמא: פונקציות מדרגה סימטריות
> עבור $a>0$ נסתכל על הפונקציה
> $$.f_a(x)=\chi_{[-a,a]}(x)=\cases{1 & |x|\leq a \\ 0 & |x| > a}$$
> עבור הפונקציות האלו ראינו ש $\hat{f}_a(\omega)=\frac{\sin(\omega a)}{\omega \pi}$. שימוש בפלנשרל עבור המכפלה הפנימית יתן לנו ש:
> $$\align{\int_{-\infty}^\infty \frac{\sin(\omega a)}{\omega \pi} \cdot \frac{\sin(\omega b)}{\omega \pi} \dom &= \frac{1}{2\pi} \int_{-\infty}^\infty f_a(x) f_b(x) \dx = \frac{1}{2\pi} \int_{-\infty}^\infty f_{\min(a,b)}(x) \dx \\&= \frac{\min(a,b)}{\pi}}$$