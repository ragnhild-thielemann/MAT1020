# Kapittel 2
## 2.1 Utnyttelse av  en begrenset naturresuss

![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/oljeee.jpg)


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


## 2.2 Differensiallikninger for utnvinning av  en fornybar resuss

![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/fisk.jpg)

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
    - Logistisk vekst gir bare mening for $B<\frac{k(r+1)}{r}$ Utenfor dette får vi negativ vekst. 


$$ g(B) = B + r B (1-\frac{B}{K}) = B ( 1 + r ((1-\frac{B}{K})$$


- Ricker - modellen
    - Stabiliserer seg ved bæreevnen $K$ . Den deriverte (som vi måler langs y-aksen) vil gå mot 0 når populasjonen når bæreevnen.
    


$$g(B) = B e^{r(1-\frac{B}{K})}$$


- Gitt taylorutviklingen, har vi for små vedier av x at $e^x = 1 + x$ . Dette gir for små verdier et utrykk som er likt som den logistiske modellen.


$$ g(B) = B ( 1+ r(1-\frac{B}{K})$$ 




- Beverton - Holt modellen
    - Bæreevnen er gitt ved $K$ = $\frac{R-1}{b} $ 
    


$$ g(B) = \frac{RB} {1+bB} $$




![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/absolutt.png)

Utviklingen over tid viser at både Ricker-modellen og den logistiske modellen gir ustabile populasjonsdynamikker (ocilerer for gitte startverdier), mens Beverton–Holt-modellen fører til en stabil populasjon.

#### Om fikspunkt

Modellene vil konvergere mot $g(K) = K$ , alstå at den konvergerer mot bæreevnen. 
### Schaefer-modellen: Høsting av naturresusser 

Dersom vi henter ut resusser $h(t)$ fra en populasjon (slik at den formerer seg) $B(t)$ , vil populasjonen utvikle seg ved en  differensiallikning $g$ (som kan være en av dynamikkene vi så på i forrje avsnitt), gitt ved


$$ B(t + 1) = g(B(t) - h(t)) , 0<= h(t) <= B(t)$$


Vi tar utgangspunkt i at $B(t)$ betegner en fiskebestand. 
- Fiskingen skjer på starten av året, mens reproduksjonen (ved differensiallikningn $g$ ) skjer på slutten av året. 


Hvor mye vi henter ut, er proposjonalt med 
- $B$ = fiskebestanden vi fisker i

- $e$ = investeringene i fiskebåter for å hente opp fisken 
- $q$ = hvor effektivt fiskebåtene henter opp fisken (effektiviteten til investeringene) 


Dette gir 


$$h = q e B = H(e,B) $$


slik at $h$ blir en skalarfunksjon. (fra ECON1410 kjenner vi dette som en produktfunksjon med to variable). 

Vi har at

   - $H(0,e)=H(B,0)=0$
  - Vi antar at $H(e,B)$ er kontiunelig paritell deriverbar, slik at vi kan derivere både med hensyn på $B$ og $e$ . Dermed kan vi analysere følsomheten av høstingen for små endringer i både biomassen $B$ og innsattsen for å hente ut biomassen $e$ . Dette gir 


$$
\begin{cases}
0 \le H_B(e,B) := \frac{\partial H}{\partial B}(e,B), \\
0 \le H_e(e,B) := \frac{\partial H}{\partial e}(e,B)
\end{cases}
$$


Biologer og økonomer har to ulike måter å tilnærme seg funksjonen H( $e$ , B) for innhøstingen av en begrenset naturresuss. For en biolog, beskriver den hvor mye av populasjonen som blir fjernet, og omtales som **høstingsfunksjonen** . 

For en økonom, er H( $e$ ,B) en **produksfunksjon** med to insatsfaktorer, realkapital og fiskebestand. For økonomer, kan produktfunksjonen beskrives som 


$$H(e,B) = q e^{$\alpha$} B^{$\beta$} $$ 


der $\alpha$ >= 0 og $\beta$ >= 0 beskriver elastisiteten til produksjonen. 
- En høy verdi for $\alpha$ gjør at en liten endring i inveseringene gir en vesentlig høyere produksjon. Tilsvarende for parameteren $\beta$ .


### Gordon-modellen : Økonomisk modell for utnyttelse av en resuss

Gordon-modellen ønsker å maksimere profitten ved å høste en naturresuss. Vi  har en kostnadsfunksjon $C(e)$ , som avheniger av investeringene $e$ , og vi selger fisken til prisne $p$ . Profitten er da gitt ved


$$R(e,B) := p(H(e,B)) - C(e) $$


- $C(0)$ = 0 
    - Om vi ikke gjør noen investeringer, har vi heller ingen kostnader
- $C'(e)$ > 0, da en økning i antall fiskebåter vil føre til økte kostander. 
- Vi antar at kostnadene er linjære, slik at vi har $C(e) = ce$ , $c>0$

Profittfunksjonen $R(e,B)$ kan maksimeres under bibetingelsen om at $B = g(B-H(e,B))$ . Optimeringsproblemet er altså å maksimere profitten, samtidig som bestanden $B$ ligger i et fikspunkt for funksjonen $g(B-H(e,B))$ . Da vil populasjonen være stabil over tid. 


#### Maksimere profitten for alle fremtidige generasjoner

Da vi ønsker en bærekraftig utnyttelse av resussen, ønker vi å maksimere profitten fra fiskebestanden for nåværende, og alle fremtidige genereasjoener. Vi summererer derfor profitten for alle generasjoner, der vi legger til en diskonteringsfaktor 0 < $\rho$ < 1. Dette gir følgene funksjon, som vi ønsker å maksimere


$$ \underset{e(t_0),...,e(T-1)}{\max}
\sum_{t=t_0}^{T-1} \rho^t (p H(e(t),B(t)) - C(e(t)) $$


#### Maksimere nytten 

For å maksimere samfunnets totale nytte av innhøstingen av en fiskebestatd, måler vi igjen summen av diskontrete nytteverdier fra høstienen i hver periode. Dette skrive som 


$$ \underset{h(t_0),...h(T-1)}{\max}
\sum_{t=t_0}^{T-1} \rho^t ((L(h(t)) + \rho^T L(B(T)) $$


- Leddene $\rho^t ((L(h(t))$ beskriver nåverdiene til nytten vi får fra å høste $h(t)$ av bestanden $B(t)$

- Det siste leddet $\rho^T ((L(h(T))$ beskriver verdien av bestanddelen som er igjen etter vi har hentet ut resussene. Dette viser at resussen har en verdi, til tross for at vi ikke henter den ut, og gjør den til penger. 