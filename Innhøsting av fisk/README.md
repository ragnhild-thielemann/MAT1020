

Vi  antar at vi fisker torsk, og at nyttefunksjonen er gitt ved $L(h) = \sqrt{h}$ . Vi skal fiske i to år av en bestand som nå består av $B$ torsk. Diskonteringsraten er $\rho$ < 1, mens torsken formerer seg med en faktor $R$ > 1. For å løse dette problemet bruker vi negativ induksjon, der begynner med verdien ved $t$ = 3, før vi regner oss nedover. 


Dynamikken til torskebetanden er gitt ved B(0) = B , B(1) = R(B-h(0)), B(2) = R(B(1)-h(1)) og B(3) = R(B(2)-h(2)) , altså en linjær formering. Vi  definerer nyttefunksjonen 

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


Dette partiellderiverer vi på samme måte med hensyn på $h$ , som gir oss 

