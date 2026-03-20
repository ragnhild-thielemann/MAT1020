

### Oppgave 2.
 En smittsom sykdom sprer seg i en befolkning. Av dem som
er syke ´en uke, vil 25 % fortsatt være syke uken etter. Sykdommen har en
inkubasjonstid på to uker, og en person som var syk for to uker siden, vil i
gjennomsnitt ha smittet $\frac{5}{4}$
person som blir syk denne uken. Vi lar $x_n$ være
antall personer som er syke etter $n$ uker.

#### Løsning

Når vi skal finne en differensløsning på problemet, ser vi først at en person som ble smittet for to uker siden er oppghavet til $\frac{5}{4}$ syk person denne uken. I tilegg vil $\frac{1}{4}$ av dem som var syke forrgje uke være syke i dag. Det gir følgene differenslikning:


$$
x_{n+2} = \frac{1}{4} x_{n+1} + \frac{1}{4}  x_{n} \leftrightarrow x_{n+1} = \frac{1}{4} x_{n} + \frac{1}{4}  x_{n-1} 
$$