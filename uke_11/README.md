## Diskontert nytte
## 2.1 Utnyttelse av  en begrenset naturresuss

![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/olje.png)


Vi tenker oss at vi har en gitt mengde av en naturresuss $S(t)$ , som vi henter ut en mengde $h(t)$. Mengden vi har ved tiden $t$ = $t_0$ + 1  blir da en dynamisk modell fra $t_0$ til tidshorisonten $T$ , der vi har 


$$ S(t + 1) = S(t) - h(t) \\
t = t_0 , t_0 + 1 , t_0 + 2 , T -1 $$


Vi har at

$$ 0 <= h(t) $$

Da vi bare kan hente ut en postiv størrelse av resussen. Grunnet fysiske begrensinger (vi kan ikke hente ut mer enn den totale beholdningen) har vi: 


$$h(t) <= S(t)$$


og 

$$0<=S(t)$$


Grunnet ønsket om å ha en viss mengde etter endt utnyttelse av resussen, skriver vi gjerne 


$$S^{b} <= S(t)$$



Da $S(t)$ er en begrenset resuss, ønsker vi at alle generasjoner frem i tid får utnyttet resussen. En slik bærekraftig utnyttelse kan omtales som **Maximim Rawls criterion** , og handler om å maksimere den totale opplevde velferden av en resuss. Dette gir følgene optimeringsproblem

### Utrykk for diskontrent nytte

$$ \underset{h(t_0),...,h(T-1)}{\max}
\sum_{t=t_0}^{T-1} \rho^t L(h(t)) $$


der:
- $L(h(t))$ er nytten generasjonen $t$ får av mengden $h(t)$ de utnvinner fra den tømbare naturresussen $S(t)$ 

- $\rho$ = diskonereingsfaktor (hvor mye vi verdsetter senere generasjoner frem i tid). Dette er gitt ved $p$ = $\frac{1}{1 + r_f}$ 
    - $r_f$ er hvor mye vi diskonteringsfakoren. En høy verdi for $r_f$, vil bety at vi verdsetter senere genersjoner lavt. $r_f$ = 0 vil si at alle generasjoner verdsettes like høyt. 

- $t$ = tidspunkt (generasjon)

Da 0 < $p$ < 1 anser vi nytteverdien fremtidige generasjoner får av en naturresuss som avtakene. Dess lavere verdi for $\rho$ , dess større andel $h(t)$ bør tidligere generasjoner hente ut av $S(t)$


## 2.2 Differensiallikninger for utnvinning av  en begrenset resuss

### Ulike modeller for utvikling av en populasjon

Biologer beskriver gjerne utviklingen i en populasjon som en differensiallikning, gitt ved 


$$B(t + 1) = g(B(t)) $$


Det er ulike dynamiske modeller for å beskrive utviklingen til en art, som er plottet nedenfor. Nedenfor er det plottet ulike dynamiske modeller for populasjonen, samt forklaring av de ulike modellene. 

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
    - Stabiliserer seg ved bæreevnen $K$ . Den deriverte (som vi måler langs y-aksen) vil gå mot 0 når populasjonen når bæreevnen.


$$g(B) = B e^{r(1-\frac{B}{K})}$$


- Beverton - Holt modellen
    - Bæreevnen er gitt ved $K$ = $\frac{R-1}{b} . 


$$ g(B) = \frac{RB} {1+bB} $$




![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/absolutt.png)

Utviklingen over tid viser at både Ricker-modellen og den logistiske modellen gir ustabile populasjonsdynamikker (ocilerer for gitte startverdier), mens Beverton–Holt-modellen fører til en stabil populasjon.


### Høsting av naturresusser

Dersom vi henter ut resusser $h(t)$ fra en naturlig populasjon (slik at den formerer seg) $B(t)$ , vil populasjonen utvikle seg ved en  differensiallikning $g$ (som kan være en av dynamikkene vi så på i forrje avsnitt), gitt ved


$$ B(t + 1) = g(B(t) - h(t)) , 0<= h(t) <= B(t)$$


Vi tar utgangspunkt i at $B(t)$ betegner en fiskebestand. 
    - Fisket skjer på starten av året, mens reproduksjonen (ved differensiallikningn $g$ ) skjer på slutten av året. 


Hvor mye vi henter ut, er proposjonalt med $B$ , samt $e$ (investeringene vi gjør for å hente ut naturresussene) og $q$ (hvor effektive inveseteringene henter ut naturresussene). 


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