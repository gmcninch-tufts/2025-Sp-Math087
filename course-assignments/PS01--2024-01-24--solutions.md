---
title: |
 ProblemSet 1 -- Optimization
author: George McNinch
date: 2025-01-24 
---

1. An optimization question in widget manufacturing
------------------------

A manufacturing firm makes a profit of `$`1200 per unit on the sale of
a product known as a widget. The firm hopes to increase widget sales
by offering a rebate; after some number-crunching, it is estimated
that for every `$`100 of rebate, the number of widgets sold in a given
month will increase by 15%.

a. What amount of rebate will maximize the manufacturers profit for
   the month? Model the question as a single-variable optimization
   problem.

   ::: {.solution}
   Let's set some quantities:

   - $r$ = amount of rebate to be given, in dollars.
   - $u_0$ = units that will be sold, absent any rebate
   - $s$ = rebate benefit; i.e. relative change in sales per \$100 of rebate    
     $0.15$ (i.e. "$15$ %")
   - $u = u(r)$ = units that will be sold with rebate $r$ in place
   - $p = p(r)$ = profit for the month with rebate $r$ in place

   Then according to the anticipated rebate effect,
   $$u = u(r) = u_0 \cdot \left(1 + \dfrac{s}{100}r\right )$$
   
   and the month's profit is the product   
   
   > (``profit per widget``) $\times$ (``widget sold``);
   
   i.e.
   
   \begin{align*}
   p = p(r) &= (1200-r) \cdot u(r) \\
   &= u_0(1200-r)\left(1 +
   \dfrac{s}{100}r\right).
   \end{align*}
 
   Now, $p$ is a quadratic function of $r$, and the coefficient of $r^2$
   is *negative* (since $s$ is positive). Thus the profit is maximized at
   the unique critical point of this function, which is found by solving
   the equation $\dfrac{dp}{dr} = 0$ for $r$. We must solve the equation:

   \begin{align*}
   0 &= \dfrac{dp}{dr} = u_0\dfrac{d}{dr}\left(-\dfrac{s}{100}r^2 +
    (1200\dfrac{s}{100} - 1)r + 1200\right) \\
    &= u_0\left( \dfrac{-s}{50}r +
    12s -1\right)
   \end{align*}

   Thus we need $r= r^*$ where
   $$r^* = \dfrac{12s -1}{s/50} = \dfrac{50 \cdot (12s - 1)}{s}$$
   
   When $s=.15$, find that the maximum profit is attained at
   $r^*=\$266.\overline{66}$.

   e.g. you might calculate as follows:
   ``` python
   def r(s):
	   return 50*(12*s - 1)/s
	   
   r(0.15)
   => 266.66666666666663
   ```

   According to our model, the resulting profit for this rebate is $\$
   1306.66 \cdot u_0$
   
   ``` python
   def p(r,s):
	   return (1200-r)*(1+s*r/100)
	   
   p(r(0.15), 0.15)
   => 1306.6666666666667
   ```
   where we recall that $u_0$ is the number of widgets sold absent a rebate.
   :::

b. Compute the *sensitivity* of your answer to the 15%
   assumption. Consider both the amount of rebate and the resulting
   profit.
   
   ::: {.solution}
   Note that
   
   $$\dfrac{dr^*}{ds} = u_0 \dfrac{d}{ds} \left( 50 \cdot 12 - \dfrac{50}{s}\right) = u_0 \dfrac{50}{s^2}.$$
   
   Now, the sensitivity of the refund is given by
   
   $$S(r^*,s) = \dfrac{dr^*}{ds} \cdot \dfrac{s}{r^*}
   = \dfrac{50}{s^2} \cdot \dfrac{s}{r(s)}
   = \dfrac{50}{s \cdot r(s)}$$
   (observe that the factor of $u_0$ in $\dfrac{dr^*}{ds}$ cancels the
   corresponding reciprocal factor in $\dfrac{s}{r^*}$).



   In python we can write this as
   
   ``` python
   def RebateSens(s):
	return 50/(s*r(s))
	
   # remember that r was already defined as a function of s...
   ```
 

   Thus the sensitivity of the refund at $s=.15$ is given by
   $S(r,.15)$; i.e.
   
   ``` python
   RebateSens(.15)
   => 1.2500000000000002
   ```
   
   As a function of $s$, the maximum profit is given by
   $$p(s) =   \dfrac{25(12s+1)^2}{s}.$$
   
   (You can do this calculation by hand, or use `sympy` as follows:
   
   ``` python
   import sympy as sp
   ss = sp.Symbol('s') 
   
   x=p(r(ss),ss)
   sp.simplify(x)
   => ...
   ```
   )
   
   Differentiation now gives
   $$\dfrac{dp}{ds} = 3600- \dfrac{25}{s^2}$$
   
   (again, you can do this by hand or as follows:
   
   ``` python
   sp.simplify(sp.diff( p(r(ss),ss) ))
   => ...
   ```
   )
   
   Now, the sensitivity of profit to s is given by
   $$S(p,s) = \dfrac{dp}{ds} \cdot \dfrac{s}{p}$$

   We can compute this senstivity:
   ``` python
   
   def DerivProfitWRTs(s):
	   return 3600 - 25/s^2
   
   def ProfitSens(s):
	   return DerivProfitWRTs(s) * s/p(r(s),s) 
   
   ```
   
   
   so 
   $$\dfrac{dp}{ds} = 5625 - \dfrac{25}{s^2}\bigg \vert_{s=0.15} = 4513.89$$
   
   Thus
   $$S(p,s) = \dfrac{dp}{ds} \cdot \dfrac{s}{p} = 4513.88 \cdot
   \dfrac{0.15}{1760.4} \approx .384 $$
   
   This means that a 1% change in the "rebate benefit" should cause a 0.8% change in
   the "optimal rebate" and roughly a 0.4% change in the monthly profits.
   :::


c. Suppose that rebates actually generate only a 10% increase in sales
   per `$`100. What is the effect? What if the response is somewhere
   between 10% and 15% per `$`100 of rebate?

d. Under what circumstances would an offer of a rebate cause a
   reduction in profit?
   

2. Computing yields with multi-variate optimization
-----------

A chemist is synthesizing a compound. In the last step, she must dissolve her reagents in a
solution with a particular `pH` level $H$, for $1.2 ≤ H ≤ 2.7$, and heated to a temperature $T$ (in
degrees Celsius), for $66 ≤ T ≤ 98$. Her goal is to maximize her percent yield as a percentage
of the initial mass of the reagents. 

The equation determining the percentage $F (H,T)$ is 

$$F(H,T) = −0.038\cdot T^2 − 0.223 \cdot T\cdot H − 10.982 \cdot H^2 +
7.112 \cdot T + 60.912 \cdot H − 328.898.$$

1. Find the optimal temperature and `pH` level in the allowed range.

::: {.solution}
To find optimal values let us consider partial derivatives:

\begin{align*}
\dfrac{\partial F}{\partial H} &= −0.223T − 21.964H + 60.912 = 0 \\
\dfrac{\partial F}{\partial T} &= −0.076T − 0.223H + 7.112 = 0
\end{align*}

One can solve this using elementary methods to obtain: 

$$T = 88.0651, H = 1.87914$$

For example, you could use `numpy`:

``` python
import numpy as np

A= [[.223,  21.964], [ .076, .223]]  # remember that a matrix is a "list of lists"
b=[60.912,7.112]                     # and a vector is just a list

np.linalg.solve(A,b)
=> array([88.06514956,  1.87914185])
```
to obtain the result.

Or you could use row operations on the appropriate augmented matrix.
:::


2. Use `matplotlib` to produce a graph and a contour plot of the percentage of the powder
function $F (H, T )$.

(You should consult this week's `jupyter notebooks` to see some
examples. To get a usable copy of your image, you can proceed in a few
ways:

  - if you produce the graph in colab you can right-click on the image
    and `Save As` a file on your file system.
  - if you work in Python on your computer, you can save the image via
    a command like

    ```
    > g.savefig(”myGraphImage.png”)
    ```

::: {.solution}

You can use the code from the in-class notebook. (In the code below I've removed the code drawing curves through
the critical point)

``` python
import matplotlib.pyplot as plt
import numpy as np

# https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html
# https://matplotlib.org/3.3.1/gallery/mplot3d/surface3d.html

def draw_graph(f,x,y,elev_azim=[]):
    X,Y = np.meshgrid(x,y)
    fig = plt.figure(figsize=(20,20))

    for idx,(e,a) in enumerate(elev_azim,start=1):
        
        ax = fig.add_subplot(1,len(elev_azim),idx,projection='3d',elev=e,azim=a)
        ax.plot_wireframe(X,Y,f(X,Y))
    
    return fig

```

Now you need to define the function $F$ in python:
``` python
def F(h,t):
	return -0.38*t**2 - 0.223*t*h - 10.982*h**2 + 7.112*t + 60.912*h - 328.898
```	

And you can produce a graph via something like:
``` python
x = np.linspace(-10,10,25)
y = np.linspace(-10,10,25)

draw_graph(F,x,y,[(40,55)])

``` 

You can experiment with the `elev_azimuth` argument to get
different perspective views of the graph.

:::

