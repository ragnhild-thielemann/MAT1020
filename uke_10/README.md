
## Oppgave 1
Vi skl vise at gitt to aksjer med forventet avkastning $r_1$ og $r_2$, der $r_1$ $\neq$ $r_2$ , så vil det være nøyaktig en optimal portefølge **w** = ( $w_1$ , $w_2$ )

Vi har at 


$$ w^T r_v = r $$


og 


$$ w^T 1 = 1 $$


Dette gir 


$$w_1 + w_2 = 1 \Leftrightarrow w_2 = 1-w_1 $$


Insatt i det første utrykket har vi da


$$ w^T r_v = r \Leftrightarrow w_1 * r_1 + w_2 * r_2 = r \Leftrightarrow w_1 * r_1 + w_2 * (1-r_1) = r \Leftrightarrow w_1 * r_1 + r_2 - r_2 * w_1 = r \Leftrightarrow w_1 ( r_1 - r_2 ) = r - r_2 \Leftrightarrow  w_1 = \frac{r-r_2}{r_1-r_2} $$

Da vi har at $r_1$ $\neq$ $r_2$ , alstå at forventetet produksjon fra de to vindmøllene er ulike, får vi nå et eksplisitt utrykk for inveseringen vi bør gjøre i vindpark 1. Inverseringen i vindpark 2 vil være $w_24$ = 1- $w_1$


Optimal portefølge blir da 


$$ w = ( \frac{r-r_2}{r_2-r_1} , \frac{r_1-r} {r_2 - r_1} )$$


Vi antar at kovariansmatrisen til avkasntingen til de to aksjene er 


$$ C = \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{pmatrix} $$


Variansen til hele portefølgen er da gitt ved matriseproduktet (som blir en skalar)


$$ Var(R) = w^T C w \Leftrightarrow \sigma ^ 2 = w_1^2 + Var( r_1 ) + w_2^2 + Var( r_1 ) + 2 w_1 w_2 * Cov( r_1 , r_2 ) $$


Da vi har 


$$ w = ( \frac{r-r_2}{r_2-r_1} , \frac{r_1-r} {r_2 - r_1} ) $$


får vi følgene utrykk for variansen ved en gitt forventet avkastning {r}


$$\sigma ^2 = \frac{Var(r_1)(r - r_2)^2 + Var(r_2)*(r - r_1)**2 + 2(r - r_1)(r - r_2)  Cov(r_1 , r_2)}{(r_1 - r_2)^2}$$


Dersom vi bruker de numeriske verdiene fra oppgaven (og får chat til å gjøre algebraen for oss) får vi følgene utrykk for $\sigma$ - $\mu$ - planet for sammenhengen mellom avkastning og varians. 


$$ Var(r) = 8.5 r^2 - 1.9 r + 0.115 $$


I scriptet  [oppgave_1.py] plotter jeg matrisemultiplikasjonen for hver optimal **w** for å finne variansen ved den gitte inverseringen, mot den analytiske løsningen til Chat. 


Dersom vi plotter disse mot hverandre, får vi følgene plott: 

![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/plott_mot_hveradnre.png)

