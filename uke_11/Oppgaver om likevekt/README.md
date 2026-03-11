

# Oppgave 1

Vi tar utgangspunkt i avsnittet om høstning av fornybare naturresusser. Der antar vi at vi har en fiskestamme $B(t)$ , som vi høster $h(t)$ fra hvert år. Fiskestammen formerer seg ved en gitt difrensiallikning, som er beskrevet i notatet (kan være linjær, logistisk, Beverton-Holt). Dette gir  


$$B(t+1) = g(B(t) - h(t))$$


I første tilfelle betrakter vi en fiskestamme som formerer seg etter en linjær modell $G(B) = RB$ der $R > 1$ (R = 1 + $r_f$ der $r_f$ er prosentandelen den formerer seg med hvert år )

Vi antar at årets bestand er $B$ . 


Dersom bestanden skal være stabil, ønsker vi at betstanden $B$ skal være et fikspunkt for differenisallikninge. Dette gir

$$ 
\begin{aligned}
G(B) = RB = B \\
R(B-h) = B \\
R B - R h = B \\ 
R B - B = R h \\
h = \frac{B(R-1)}{R} 
\end{aligned}$$


Vi kan altså høste h = $\frac{B(R-1)}{R}$ hvert år, og fiskebestanden vil forstatt være stabil $B$ . 


Dersom $r_f$ = 0.2 , alstå at fisken formerer seg med faktor 1.2, får vi 


$$ 
\begin{aligned}
h = \frac{B(R-1)}{R} \\
h = \frac{B(1.2 - 1}{1.2}\\
h = \frac{B(0.2}{1.2}\\
h = \frac{1}{6} B
\end{aligned}$$

#### Vi kan altså fiske opp 1/6 av bestanden hvert år.


# Oppgave 2

I denne oppgaven ser vi på Beverton - Holt - modellen, der

$$ G(B) = \frac{RB}{1+bB} $$

Når vi skal finne bæreevnen $K$ , løser vi 


$$ 
\begin{aligned}
G(K) = K = \frac{RK}{1+bK} \\
K + K^2 b = R K \\
K + K^2 b - R K = 0 \\
K (1 + K b - R ) = 0 \\

K = 0 er en gydlig løsning \\

1 + K b - R = 0 \\
K = \frac{R-1}{b} \\

Dette blir den positive løsningen for K \neq 0
\begin{aligned} $$

