
## Oppgave 1
Vi  antar at vi fisker torsk, og at nyttefunksjonen er gitt ved $L(h) = \sqrt{h}$ (Kvadratfunksjonen gir en konkav funksjon, som henger sammen med avtakene marginalproduktivitet for nytten oppnådd). Vi skal fiske i to år av en bestand som nå består av $B$ torsk. Diskonteringsraten er $\rho$ < 1, mens torsken formerer seg med en faktor $R$ > 1. For å løse dette problemet bruker vi negativ induksjon, der begynner med verdien ved $t$ = 3, før vi regner oss nedover. 


Dynamikken til torskebetanden er gitt ved 


$$\begin{align}B(0) = B , B(1) = R(B-h(0)), B(2) = R(B(1)-h(1)) og B(3) = R(B(2)-h(2)) \end{align}$$


, altså en linjær dynamisk funksjon. Vi  definerer nyttefunksjonen 


$$
V(t, B) =
\max_{\substack{
0 \le h(t) \le B \\
0 \le h(t+1) \le B(t+1) \\
0 \le h(2) \le B(2)
}}
\left[
\sum_{s=t}^{2} \rho^s \sqrt{h(s)} + \rho^3 \sqrt{B(3)}
\right]
$$


### Oppgave a)

V(3,B) er verdien til torsken etter tre år, altså når vi er ferdige med å fiske. Dette kan omtales som "skrapverdien", og er gitt ved 


$$ V(3,B) = \rho^3 \sqrt{B(3)} $$


Verdeien til fisken etter tre år er altså diskonteringsfaktoren opphøyd i tre, multiplisert med kvadratroten av mengden fisk som er igjen. 

### Oppgave b)
Vi skal nå bruke dynamisk porgrammeringsprinsipp til å finne den optimale h*(2) og verdifunksjonen V(2,B) , alstå optimal innhøsting av torsk etter to år for å makimere verdien.

Dette gir utrykket for verdien for utaket av fisk etter to år:


$$ \begin{align}
V(2,B) &= \rho^2 \sqrt{h(2)} + \rho^3 \sqrt{B(3)} \\
&= \rho^2 \sqrt{h(2)} + \rho^3 \sqrt{R(B(2)-h(2))} 
\end{align}
$$

For å finne optimal innhøsting, deriverer vi dette med hensyn på $h$ , som vi så setter lik null for å maksimere funksjonsverdien:



$$
\begin{align}
\frac{\partial}{\partial h} V(2,B)
&= \frac{\partial}{\partial h} \left( \rho^2 \sqrt{h} + \rho^3 \sqrt{R(B - h)} \right) = 0 \\
\frac{\rho^2}{2\sqrt{h}} 
&= \frac{\rho^3 \sqrt{R}}{2\sqrt{B - h}} \\
\frac{1}{\sqrt{h}} 
&= \rho \frac{\sqrt{R}}{\sqrt{B - h}} \\ 
\frac{1}{h} 
&= \frac{\rho^2 R}{B - h} \\
B - h 
&= \rho^2 R h \\
h_{optimal}
&= \frac{B}{1 + \rho^2 R}
\end{align}
$$


Når vi setter dette inn i utrykket for $V(2,B)$ , og setter konstantene utenfor, slik at vi får en funksjon av B, får vi følgene


$$
\begin{align}
V(2,B)_{optimal}
&= \rho^2 \sqrt{\frac{B}{1 + \rho^2 R}} + \rho^3 \sqrt{R(B(2)-\frac{B}{1 + \rho^2 R}}
\\ 
 &= \frac{\rho^2 + R \rho^4}{\sqrt{1+ \rho^2 R}} \sqrt{B} 
\end{align} 
$$


Dette gir oss et utrykk for optimal innhøsting andre året vi fisker  torsk. 

### Oppgave c) 

Når vi skal finne optimal innhøsting i $t$ = 1, bruker vi den samme negative induksjonen. Vi setter


$$ \begin{align}
V(1,B)_{optimal} = \rho \sqrt{h(1)} + V(2,R(B(1)-h(1)) \end{align} $$


Da vi i forrigje oppgave regnet ut $V(2,B)_{optimal}$ til å være: 


$$ \begin{align}
V(2,B)_{optimal}  &= \frac{\rho^2 + R \rho^4}{\sqrt{1+ \rho^2 R}} \sqrt{B} 
\end{align} $$ 


har vi et problem på formen med en konstant $A_1$ 


$$ \begin{align}
V(1,B)_{optimal} = \rho \sqrt{h(1)} + V(2,R(B(1)-h(1)) \\
\rho \sqrt{h} + A_{1} \sqrt{R(B-h)}
\end{align} $$


Vi løser nå den generelle problemstillingen for den negative induksjonen for optimal innhøsting etter tid $t$ .


$$\begin{align} 
V(t,B)_{optimal} &= a \sqrt{h} + b \sqrt{R(B-h)} \\
\frac{\partial}{\partial h} V(t,B)
&= \frac{\partial}{\partial h} \left( a \sqrt{h} + b \sqrt{R(B - h)} \right) &= 0 \\
\frac{a}{\sqrt{h}} &= \frac{b \sqrt{R}}{\sqrt{B-h}}
\\
h_{optimal} &= \frac{a^2 B}{b^2 R + a^2}
\end{align}$$

Når vi setter inn $h_{optimal}$ som funksjonsverdi, får vi følgene resulat for den genrelle løsningen for parametererene $a$ og $b$ . Dette gir 


$$ \begin{align}
V(B) &= a \sqrt{h} + b \sqrt{R(B-h)} \\
&= a \sqrt{\frac{a^2 B}{b^2 R + a^2}} + b \sqrt{R(B-\frac{a^2 B}{b^2 R + a^2})} \\
&= a \sqrt{\frac{a^2 B}{b^2 R + a^2}} + b \sqrt{\frac{b^2 B R^2}{b^2 R + a^2}} \\ 
&= \frac{a^2 \sqrt{B} + b^2 R \sqrt{B}}{\sqrt{b^2 R + a^2}} \\
V(B) &= \sqrt{a^2 + b^2 R}  \sqrt{B}
\end{align}$$


Når vi har regnet den genrelle formelen, blir oppgaven med negativ induksjon mye lettere, da vi ender opp med like problemer, men at paramterene $a$ og $b$ endrer seg. 



For $V(1,B)$ er parameterene $a$ = $\rho$ og $b$ = $A_1$ . Dette gir 


$$
\begin{align} 
h_{optimal} &= \frac{\rho^2 B}{A_1^2 R + \rho^2} \\ 
V(1,B) &= \sqrt{\rho^2 + A_1^2 R} * \sqrt{B} 
\end{align} $$


### Oppgave d)

Når vi skal regne det optimale uttaket av  torsk ved det første året, har vi igjen et problem på formen 


$$ \begin{align}
V(0,B)_{optimal} = \sqrt{h(0)} + V(1,R(B(0)-h(0)) \\
\sqrt{h} + A_{2} \sqrt{R(B-h)}
\end{align} $$


Parameterene for den genrelle løsningen er da $a$ = 1 og $b$ = $A_2$ . 

Det gir løsningen for optimalt uttak det første året til 


$$ 
\begin{align} h_{optimal} &= \frac{ B}{(A_2^2 R + 1} \\
V(B) &= \sqrt{1 + A_2^2 R}  \sqrt{B}
\end{align} $$


### Oppgave e)

B(3) vil være gitt ved en dynamisk prosess med flere ledd, der vi regner oss tilbake i tid. 


$$\begin{align}
B(3) &= R(B(2)-h(2)) \\
&= R(R(B(1)-h(1))) \\
&= R(R(R(B-h(0))) \end{align}$$

## Oppgave 2

I oppgave 1 fant vi at den genrelle løsningen på det generelle probelmet for negativ induksjon var 


$$ \begin{align} h_{optimal} &= \frac{a^2 B}{b^2 R + a^2} \\

V(B) &= \sqrt{a^2 + b^2 R}  \end{align} $$


Dermed kan vi sette inn konstantene fra oppgaven. 


$$ \begin{align} 

B(0) &= B &= 100 \\ R &= 1.1 \\ \rho &= frac{1}{1.05} \end{align} $$

Vi finner den optimale innhøstingen, først gitt etter tre år. Dette er et optimeringsproblem på formen 


$$ \begin{align} V(2,B(2)) &= \rho^2 \sqrt{h(2)} + V(3,R(B(2)-h(2)) \\
&= a \sqrt{h} + b \sqrt{R(B-h)} 
\end{align} $$


Når vi setter inn de numeriske løsningene for det optimale uttaket får vi 


$$ \begin{align} h_{optimal} &= \frac{(1.05^2)^2 *100}{(1.05^3)^2 1.1 + (1.05^2)^2} &= \end{align}$$


