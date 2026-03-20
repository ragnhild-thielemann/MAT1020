

### Oppgave 2.
 En smittsom sykdom sprer seg i en befolkning. Av dem som
er syke ´en uke, vil 25 % fortsatt være syke uken etter. Sykdommen har en
inkubasjonstid på to uker, og en person som var syk for to uker siden, vil i
gjennomsnitt ha smittet $\frac{5}{4}$
person som blir syk denne uken. Vi lar $x_n$ være
antall personer som er syke etter $n$ uker.

#### oppgave b)

Når vi skal finne en differensløsning på problemet, ser vi først at en person som ble smittet for to uker siden er oppghavet til $\frac{5}{4}$ syk person denne uken. I tilegg vil $\frac{1}{4}$ av dem som var syke forrgje uke være syke i dag. Det gir følgene differenslikning:


$$
x_{n} = \frac{1}{4} x_{n-1} + \frac{5}{4}  x_{n-2} \leftrightarrow x_{n+1} = \frac{1}{4} x_{n} + \frac{5}{4}  x_{n-1} 
$$


Vi har tidligere vist at løsningene $r_1$ og $r_2$ er løsningene på den karrakteristiske likningen 

$$ r^2 - \frac{1}{4} r - \frac{5}{4} $$

gir løsningen på differenslikning, så vi vil ha en løsning på formen 


$$
x_n = A r_1^n + B r_2^n
$$


Når vi løser den karakteristiske likningen får vi


$$ \begin{align}
r_1 = \frac{5}{4} \\
r_2 = -1 \\
\end {align}
$$ 


Satt inn i startbetingelsene får vi følgene liknignsett


$$
\begin{aligned}
A + B &= 190 \\
\frac{5}{4}A - B &= 260 \\
A &= 200 \\
B &= -10
\end{aligned}
$$


Løsningen er altså


$$
x_n = 200 ( \frac{5}{4} )^n -10 (-1)^n
$$

Programmet som er lagt ved regner både ut løsningene på differenslikningen, og regner den analytiske løsningen. 

#### oppgave c)

Ved den nye informasjoen, får vi en ny differenslikning vi skal løse. 
Vi har at hver person som var syk for to uker siden, bare smitter $\frac{3}{4}$ person denne uken. Dette gir følgene differenslikning : 


$$
x_{n+1} = \frac{1}{4} x_{n} + \frac{3}{4}  x_{n-1} 
$$


Ved å løse den karakteristiske likningen, får vi følgene løsning: 


$$ \begin{align}
r_1 = \frac{-3}{4} \\
r_2 = 1 \\
\end {align}
$$ 


Satt inn i startbetningelsene, får vi følgene løsning på differenslikningen


$$
x_n = 230  -40 (\frac{-3}{4})^n
$$


Når vi plotter de utviklingen av  sykdommen i de to oppgavene, får vi følgene plott
![Modelering](https://github.com/ragnhild-thielemann/MAT1020/blob/main/images/sykdom.png)

Dette viser at dersom vi setter at hver person bare smitter $\frac{3}{4}$ , vil antall syke i befolkningen gå mot 0. 