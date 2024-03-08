---
title: התמרת פורייה - סיכום
author: אופיר דוד
category: התמרות פורייה
layout: post
dir: rtl
cssclasses:
  - hebrew
---
# התמרת פורייה על $E^1(\RR)$ 

([[hebrew_Fourier_transform|רשימות]])

> [!הגדרה] הגדרה: התמרת פורייה
> עבור פונקציה $f:\RR\to \CC$ ו $\omega\in \RR$ נכתוב
> 
> $$.\hat f(\omega) := \frac{1}{2\pi} \int_{-\infty}^{\infty} f(x)e^{-i\omega x}dx = \angles{f,e^{i\omega x}}$$
> אם הגבול הזה קיים לכל $\omega \in \RR$ נקרא לפונקציה $\hat{f}:\RR\to\CC$ בשם **ההתמרת פורייה** של $f$.
> לעיתים נכתוב גם $\cf[f]=\hat{f}$.


> [!למה] למה:
> אם $f\in\ E^1(\RR)$, אז $\hat{f}(\omega)$ מוגדרת היטב לכל $\omega$ ומתקיים ש $\norm{\hat{f}}_\infty \leq \frac{1}{2\pi} \norm{f}_1$.


> [!משפט] משפט:
> עבור $f\in E^1(\RR)$ ההתמרה מקיימת:
> 1. הפונקציה $\hat{f}$ היא רציפה.
> 2. (הלמה של רימן לבג) $\limfi{\abs{\omega}} \hat{f}(\omega) = 0$.

---
# דוגמאות חשובות

|                                             $\hat{f}(\omega)$                                              |                  $f(x)$                   |
| :--------------------------------------------------------------------------------------------------------: | :---------------------------------------: |
| $\hat{f}(\omega)=\cases{\frac{\sin(\omega b)}{\omega \pi} & \omega \neq 0 \\ \frac{b}{\pi} & \omega = 0.}$ |            $\chi_{[-a,a]}(x)$             |
|                                        $\frac{1}{\pi(\omega^2+1)}$                                         |              $e^{-\abs{x}}$               |
|                                           $\frac{1}{1+i\omega}$                                            | $\chi_{[0,\infty)}(x) \cdot e^{-\abs{x}}$ |
|                                  $\frac{1}{2\sqrt{\pi}} e^{-\omega^2/4}$                                   |                $e^{-x^2}$                 |

# פעולות גאומטריות

([[basic properties|רשימות]])

|                  |                      $\hat{f}(\omega)$                      |                  $f(x)$                  |
| ---------------- | :---------------: | :-----------------: |
| **לינאריות**:    | $\alpha  \cdot \hat{f}(\omega)+\beta \cdot \hat{g}(\omega)$ | $\alpha \cdot  f(x) + \beta \cdot  g(x)$ |
| **מתיחה**:       |        $\frac{\hat{f}(\omega/\lambda)}{\|\lambda\|}$        |              $f(\lambda x)$              |
| **הצמדה**:       |                $\overline{\hat{f}(-\omega)}$                |            $\overline{f(x)}$             |
| **הזזה לסיבוב:** |             $e^{i\alpha \omega}\hat{f}(\omega)$             |              $f(x+\alpha)$               |
| **סיבוב להזזה**: |                     $\hat{f}(\omega-c)$                     |              $e^{icx}f(x)$               |
| **סינוס**:       |       $\frac{\cf[f](\omega-c)-\cf[f](\omega+c)}{2i}$        |              $f(x)\sin(cx)$              |
| **קוסינוס**:     |        $\frac{\cf[f](\omega-c)+\cf[f](\omega+c)}{2}$        |              $f(x)\cos(cx)$              |

# נגזרות

|                                     | $\hat{f}(\omega)$                              | $f(x)$            |
| ---------------- | :---------------: | :-----------------: |
| עבור $f(x),f'(x)\in E^1(\RR)$       | $i\omega \hat{f}(\omega)$                      | $f'(x)$           |
| עבור $f(x),x\cdot f(x)\in E^1(\RR)$ | $\hat{f}'(\omega)$                             | $-ix\cdot f(x)$   |

---
# ההתמרה ההפוכה

([[hebrew_delta_function|רשימות]])

> [!משפט] משפט: התמרת פורייה ההפוכה
> תהא $f\in E^1(\RR)$. בכל נקודה $x_0\in \RR$ בה יש לפונקציה נגזרות מתואמות, מתקיים ש
> $$\limfi{M} \int_{-M}^M \hat{f}(\omega)e^{i\omega x_0}\dom = \frac{f(x_0^-)+f(x_0^+)}{2}$$ 


> [!מסקנה] מסקנה: התמרה כפולה היא (כמעט) הזהות
> אם $f,\hat{f}\in E^1(\RR)$  ול $f$ יש נגזרות מתואמות ב $x_0$ אז מתקיים ש 
> $$\hat{\hat{f}}(x_0) = \frac{1}{2\pi} \frac{f(-x_0^+)+f(-x_0^-)}{2}$$
> ובפרט אם $f$ רציפה ב $x_0$ אז מתקיים ש 
> $$\hat{\hat{f}}(x_0) = \frac{1}{2\pi} f(-x_0)$$


> [!מסקנה] מסקנה:
> אם $f,\hat{f} \in E^1(\RR)$ ו $f$ רציפה עם נגזרות מתואמות, אז $f$ חסומה ומתקיים ש 
> $$.\norm f_\infty \leq \norm {\hat{f}}_1$$

# פלנשרל

([[hebrew_plancharel|רשימות]])

> [!הגדרה] התמרת פורייה ב $E^2(\RR)$
> תהא $f\in E^2(\RR)$ ועבור $M>0$ נסמן 
> $$.f_M(x):=f(x)\cdot \chi_{[-M,M]}(x)=\cases{f(x) & |x|\leq M \\ 0 & |x|>M}$$
> הפונקציות $f_M(x)$ נמצאות ב $E^1(\RR) \cap E^2(\RR)$ ונגדיר את התמרת פורייה של $f$ להיות
>  $$\hat{f}(\omega) = \limfi{M} \hat{f}_M(\omega)= \limfi{M} \frac{1}{2\pi} \int_{-M}^M f(x)e^{-i \omega x}\dx$$  
>  כאשר הגבול הוא בנורמת $\norm{\cdot}_2$.


> [!משפט] משפט פלנשרל:
> יהיו $f,g\in E^1(\RR)\cap E^2 (\RR)$ אז:
> 1. ההתמרות $\hat{f}, \hat{g}$ גם נמצאות ב $E^2(\RR)$,
> 2. מתקיים ש:
>    $$\int_{-\infty}^\infty \hat{f}(\omega) \overline{\hat{g}(\omega)} \dom = \frac{1}{2\pi} \int _{-\infty}^\infty f(x)\overline{g(x)} \dx$$
>    או בכתיב של מכפלות פנימיות $2\pi\angles{\hat{f}, \hat{g}}=\angles{f,g}$,
> 3. ובפרט מתקיים ש $\norm{f}_2=\norm{\hat{f}}_2$.

# קונבולוציה

. . . 