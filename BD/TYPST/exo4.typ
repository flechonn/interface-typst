#show terms: it => {
    let title = label("Mon Exercice de Traitement du Signal")
    let duration = label("1h30")
    let difficulty = label("Facile")
    let solution = label("0")
    let figures = label("")
    let points = label("5")
    let bonus = label("0")
    let author = label("Moi")
    let references = label("")
    let language = label("Français")
    let material = label("")
}

= Exercice 1 
Considérez un signal sinusoïdal x(t)=$A⋅sin(2π*f*t+ϕ)$, où AA est l'amplitude, ff est la fréquence en Hz et ϕϕ est la phase en radians. Écrivez une fonction en Python pour calculer la valeur efficace (RMS) de ce signal sur une période donnée. Testez votre fonction avec $A=3$, $f=50$Hz et $ϕ=π*4$ sur une période de T=$1/f$.


= Solution

Solution de l'exercice:

Pour calculer la valeur efficace (RMS) d'un signal sinusoïdal $x(t)=A⋅sin(2*π*f*t+ϕ)$ nous pouvons utiliser la formule suivante :

$"RMS"=sqrt(1/T*integral_(0)^T x^2 dif x)$

où $A$ est l'amplitude, $f$ est la fréquence en Hz, $ϕ$ est la phase en radians, et $T$ est la période du signal ($T=1/f$).

Dans notre cas, avec $A=3$, $f=50$ Hz et $ϕ=4π$ la formule devient :

$"RMS"=sqrt(1/T*integral_(0)^T (3⋅sin(2π⋅50⋅t+4π))² dif x)$

Après résolution numérique de cette intégrale sur une période T, nous obtenons la valeur efficace du signal.

