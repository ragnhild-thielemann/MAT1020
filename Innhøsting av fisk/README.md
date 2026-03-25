

Vi  antar at vi fisker torsk, og at nyttefunksjonen er gitt ved $L(h) = \sqrt{h}$ . Vi skal fiske i to år av en bestand som nå består av $B$ torsk. Diskonteringsraten er $\rho$ < 1, mens torsken formerer seg med en faktor $R$ > 1. Vi skal fiske torsk som optimerer 


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

Dette gir utrykket:


$$ \begin{align}
V(2,B) &= \rho^2 \sqrt{h(2)} + \rho^3 \sqrt{B(3)} \\
&= \rho^2 \sqrt{h(2)} \rho^3 \sqrt{R(B(2)-h(2))}
&=
\end{align}
$$