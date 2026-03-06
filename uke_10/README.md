
## Oppgave 1

#### a)
Vi skl vise at gitt to aksjer med forventet avkastning $r_1$ og $r_2$, der $r_1$ $\neq$ $r_2$ , så vil det være nøyaktig en optimal portefølge **w** = ( $w_1$ , $w_2$ )

Vi har at 


$$ w^T r_v = r $$


og 


$$ w^T 1 = 1 $$


Dette gir 


$$w_1 + w_2 = 1 \Leftrightarrow w_2 = 1-w_1 $$


Insatt i det første utrykket har vi da


$$ w^T r_v = r \Leftrightarrow w_1 * r_1 + w_2 * r_2 = r \Leftrightarrow w_1 * r_1 + w_2 * (1-r_1) = r \Leftrightarrow w_1 * r_1 + r_2 - r_2 * w_1 = r \Leftrightarrow w_1 ( r_1 - r_2 ) = r - r_2 \Leftrightarrow  w_1 = \frac{r-r_2}{r_1-r_2} $$

Da vi har at $r_1$ $\neq$ $r_2$ , alstå at forventetet produksjon fra de to vindmøllene er ulike (hvis ikke vil alle portefølger være like gode) får vi nå et eksplisitt utrykk for inveseringen vi bør gjøre i vindpark 1. Inverseringen i vindpark 2 vil være $w_24$ = 1- $w_1$ 


Optimal portefølge blir da 


$$ w = ( \frac{r-r_2}{r_2-r_1} , \frac{r_1-r} {r_2 - r_1} )$$


#### b


Vi antar at kovariansmatrisen til avkasntingen til de to aksjene er 


$$
C =
\begin{pmatrix}
C_{11} & C_{12} \\
C_{21} & C_{22}
\end{pmatrix}
$$

Dersom vi skal utrykke variansen i portefølgen med V(R), bruker vi utrykket fra Markowich portefølgeteori for varians


$$  \sigma^ 2= w^T C w $$

Vi har w = ( $w_1$ , $w_2$ ) , som gir





Variansen til hele portefølgen er da gitt ved matriseproduktet (som blir en skalar)


$$ Var(R) = w^T C w \Leftrightarrow \sigma ^ 2 = w_1^2  Var( r_1 ) + w_2^2  Var( r_2 ) + 2 w_1 w_2 * Cov( r_1 , r_2 ) $$


Da vi har 


$$ w = ( \frac{r-r_2}{r_2-r_1} , \frac{r_1-r} {r_2 - r_1} ) $$


får vi følgene utrykk for variansen ved en gitt forventet avkastning {r}


$$\sigma ^2 = \frac{Var(r_1)(r - r_2)^2 + Var(r_2)*(r - r_1)**2 + 2(r - r_1)(r - r_2)  Cov(r_1 , r_2)}{(r_1 - r_2)^2}$$


Dersom vi bruker de numeriske verdiene fra oppgaven (og får chat til å gjøre algebraen for oss) får vi følgene utrykk for $\sigma$ - $\mu$ - planet for sammenhengen mellom avkastning og varians. 


$$ Var(r) = 8.5 r^2 - 1.9 r + 0.115 $$


I scriptet  [oppgave_1.py] plotter jeg matrisemultiplikasjonen for hver optimal **w** for å finne variansen ved den gitte inverseringen, mot den analytiske løsningen til Chat. 


Dersom vi plotter disse mot hverandre, får vi følgene plott: 

![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/plott_mot_hveradnre.png)

## Oppgave 2

Vi ønsker å minimere 


$$ E [(R-E)**2] $$


Altså variansen i prosuert strøm ved tidspunktet $t$ og etterspurt strøm i tidspunktet $t$ . Det kan vises at dette kan skrives som 


$$\sigma = Var(R) + (\mu_r - \mu_e)^2 + Var(E) + 2 Cov(R,E) $$


Da produsert mengde strøm er uavhening av etterspurt strøm, vil $Cov(R,E) = 0$ . 



Vi har at 


$$ Var(R) = w^T C w $$ 


og at 


$$ \mu_r = w^T r $$



Insatt i utrykket gir dette:


$$ \sigma = w^T C w + (w^T r  - \mu_e)^2 + Var(E) $$


Vi har nå et utrykk for variansen som en funksjon av fordelingen av  vindparker **w**, som vi kan derivere, og sette lik 0. Da vi i neste oppgave skal vise at denne er poritivt defitt, vil nullpunktene være minimumspunkter for varians. 


Når dette deriveres, får vi 


$$ 2 C w + 2 (w^T r - \mu_r) r = 0\Leftrightarrow C w + (w ^T r ) r= \mu_r r \Leftrightarrow C w + (r^T w ) r = \mu_r r \Leftrightarrow (C + r r^T ) w = \mu_r r \Leftrightarrow w = \mu_r (C + r r^T )^{-1} r $$


Dette regner vi ut numersisk med de insatte verdiene fra oppgaven, der $\mu_r$ = 200

Vi får da at optimal instalering av kapasiteten bør fordeles slik


$$
w =
\begin{pmatrix}
123 \\
153 \\
138
\end{pmatrix}
$$

Gjennomsnittlig strømproduksjon for alle kraftverkene er gitt ved 


$$ \mu_r = w^T r \Leftrightarrow 
\mu_r
 = \begin{pmatrix}
123 &
153 &
138
\end{pmatrix}\begin{pmatrix}
0.4 \\
0.3 \\
0.5
\end{pmatrix} = 164 $$


#### Gjennomsnittlig strømproduksjon ved kraftverkene er altså 164 MWh


## Oppgave 3

Siste del av oppgaven går på å bruke linjær algebra til å vise at vektoren **w** som gir ekstremalverdien $w_0$ er et minimumspunkt. da vi krever at **w** > 0, kan vi ikke bruke langranges multiplikatormetode for å finne mininimpumsverdenen til 


$$ \sigma^2 = w^T C w $$ 


under bibetingelsene

$$ w^T r = \mu_r $$


og 


$$ w^T 1 = \kappa $$


### a) 

Vi begynner med definisjonen av n x n - matrise $C$ som er $postivt defitt$ matrise, som dersom 


$$ w^T C w > 0 for alle w \neq 0 $$


Dette betyr at C bare har postive egenverdier, slik at avbildningen vil være positiv. Dermed vil ekstremalpuntkene til utrykket være minimumspunkter.


Vi antar at $C$ er kovariansmatrisen til de stokastiske variablene $W_1$ , $W_2$ , $W_3$ , $W_n$ . 


Variansen til 


$$Y = w_1 X_1 + w_2 X_2 + w_3 X_3 ... w_n X_n $$


er


$$\sigma^2 = Var(Y) = w^T C w = w_1^2 Var(X_1) + w_2^2 Var(X_2) + ... +  w_n^2 Var(X_n) >= 0 for alle w $$ 


#### Dermed har vi vist at C er ikke-negativt defitt. 

### b)


Da vi har at at matrisen C er symetrisk, positivt defitt, har vi:


$$ x^T C x > 0 for x \neq 0 $$

Setter 

$$ x = C^{-1} y $$


Dette gir 


$$ x^T C x \Leftrightarrow y^T C^{-1} C C^{-1} y \Leftrightarrow y^T C^{-1} y > 0 for y \neq 0 $$


Slik at $C^{-1}$ er postivt defitt.



