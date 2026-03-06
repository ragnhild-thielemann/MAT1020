## Diskontert nytte
#### En begrenset naturresuss (kull, olje, gass)

![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/olje.png)


Vi tenker oss at vi har en gitt mengde av en naturresuss $S(t)$ , som vi henter ut en mengde $h(t)$. Dette blir da en dynamisk modell fra $t_0$ til tidshorisonten $T$ , der vi har 


$$ S(t + 1) = S(t) - h(t) \\
t = t_0 , t_0 + 1 , t_0 + 2 , T -1 $$


Vi har at

$$ 0 <= h(t) $$

Da vi bare kan hente ut en postiv størrelse av resussen. Grunnet fysiske begrensinger (vi kan ikke hente ut mer enn den totale beholdningen) har vi: 


$$h(t) <= S(t)$$


og 

$$0<=S(t)$$


#### Nytte (velferd/tilfredshet) i fremtiden verdesettes mindre enn nytte i dag.

Diskontert nytte skrives som


$$ \underset{h(t_0),...,h(T-1)}{\max}
\sum_{t=t_0}^{T-1} \rho^t L(h(t)) $$


der:
- $L(h(t))$ er nytten av forbruket i perioden (generasjonen $t$ ) 

- $p$ = diskonereingsfaktor (hvor mye vi verdsetter senere generasjoner). Dette er gitt ved $p$ = $\frac{1}{1 + r_f}$ 
    - $r_f$ er hvor mye vi diskonerere senere generasjoner.En høy verdi for denne, vil bety at vi verdsetter senere genersjoner lavt. $r_f$ = 0 vil si at alle generasjoner verdsettes like høyt. 

- $t$ = tidspunkt (generasjon)

Da 0 < $p$ < 1 anser vi nytteverdien til en begrenset naturresuss som avtakene etterhvert når tiden utvikler seg. 

Vi ønsker å maksimere total nytte av den begrensede naturresussen, slik som gir oss optimeringsproblemet vårt. 


## 




## Differensiallikninger for utviklingen i populasjonen

Utviklingen i en populajson kan modeleres ved 


$$B(t + 1) = g(B(t)) $$

som er en differensiallikning. Nedenfor er det plottet ulike dynamiske modeller for populasjonen, samt forklaring av de ulike modellene. 

![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/modeller.png)
##### Om plottet

- Bæreevnen $K$ er den minste $K$ > 0 som tilfredstiller $g(K)=K$ , altså som er et fikspunkt der populasjonen stabilserererseg. 
- Parameterene er $r$ = 1.9 , $K$ = 10 og $B$ = 2

#### Ulike modeller for å modelere utviklingen
- Logistisk modell. 
    - $r$ > 0 er hvor mye populasjonen vokser
    - $K$ er naturens bæreevne. Vi ser av plottet at derivertverdeien går mot null, som tilsvarer tidspunktet der populasjonen stabiliserer seg. 


$$ g(B) = B + r B (1-\frac{B}{K}) $$


- Ricker - modellen
    - Stabiliserer seg ved bæreevnen $K$


$$g(B) = B exp^{r(1-\frac{B}{K}))$$


- Beverton - Holt modellen


$$ g(B) = \frac{RB} {1+bB} $$




![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/absolutt.png)

Vi ser av hvordan de ulike modellene utvikler seg over tid at både Ricker-modellen og den logistiske tilnærmingen er ustabile, mens Beverton–Holt-modellen fører til at populasjonen stabiliserer seg.


## Høsting av naturresusser

Dersom vi henter ut resusser fra den naturlige populasjonen, vil den utvikle seg 


$$ B(t + 1) = g(B(t) - h(t)) , 0<= h(t) <= B(t)$$


der $h(t)$ er hvor mye vi henter ut ved tidspunktet $t$ . Hvor mye vi henter ut, er proposjonalt med $B$ , samt $e$ (investeringene vi gjør for å hente ut naturresussene) og $q$ (hvor effektive inveseteringene henter ut naturresussene). 


Dette gir 


$$h = q e B = H(e,B) $$


slik at $h$ blir en skalarfunksjon. (fra ECON1410 kjenner vi dette som en produktfunksjon med to variable). 

- $H(0,e)=H(B,0)=0$
- Vi antar at $H(e,B)$ er kontiunelig paritell deriverbar, slik at vi kan derivere både med hensyn på $B$ og $e$ . Dermed kan vi analysere følsomheten av høstingen for små endringer i både biomassen $B$ og innsattsen for å hente ut biomassen $e$ . Dette gir 


$$
\begin{cases}
0 \le H_B(e,B) := \frac{\partial H}{\partial B}(e,B), \\
0 \le H_e(e,B) := \frac{\partial H}{\partial e}(e,B)
\end{cases}
$$