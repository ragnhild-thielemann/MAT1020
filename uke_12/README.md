

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
x_{n} = \frac{1}{4} x_{n-1} + \frac{5}{4}  x_{n-2} \leftrightarrow x_{n+1} = \frac{1}{4} x_{n} + \frac{5}{4}  x_{n-1} 
$$


Vi har tidligere vist at løsningene $r_1$ og $r_2$ er løsningene på den karrakteristiske likningen 

$$ r^2 - \frac{1}{4} r - \frac{5}{4} $$

gir løsningen på differenslikning, så vi vil ha en løsning på formen 


$$
x_n = A r_1 + B r_2

$$


Når vi løser den karakteristiske likningen får vi


$$ \begin{align}
r_1 = \frac{5}{4} \\
r_2 = -1 \\
\end {align}
$$ 

Satt inn i startbetingelsene får vi følgene liknignsett


$$ \begin{align}
A r_1^0 + B r_2^0 = 190 \\
A r_1^1 + B r_2^1 = 260 \\

A  + B  = 190 \\
A \frac{5}{4} - B = 260 \\

A = 200
B = -10
\end {align}
$$ 

