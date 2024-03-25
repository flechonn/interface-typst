BD/TYPST/utilities.typ
#show: title 
 \ 
Ma Feuille d'exercices
#place(top + right, image("BD/LOGO/UFR_IM2AG_2020.jpg", width: 15%))
#show: lines 
#show: header 
author : Moi-même - date : 25 Mars 2024 - duration : 3 heures \ 
#show: modality 
Sont interdits : les documents, les ordinateurs, les téléphones (incluant smartphone, tablettes,... tout ce qui contient un dispositif électronique). Seuls les dictionnaires papier pour les personnes de langue étrangère sont autorisés. En cas de doutes sur l’énoncé, préciser les choix que vous faites sur votre copie et continuer. Il sera tenu compte de la qualité de la rédaction et de la clarté de la présentation (2 pts). Le barème indicatif : Exercice I : 5 points ; Exercice II : 5 points ; Problème III : 8 points Les exercices et le problème peuvent être traités indépendamment. Les durées sont indicatives, penser à se relire. \ 
#show: lines 
 \ 
#show: meta 
title : Addition Exercise 
duration : 30min 
difficulty : easy 
points : 10pts 
bonus : 0 
name : exo1 
 \ 
Calculate the sum of the following numbers : 

```py
let numbers = [5, 8, 12, 3]
let sum = 0
for n in numbers {
    text(n)
    sum += n
    if n != numbers[-1] {
        text(" + ")
    } else {
        text(" = ")
    }
}
``` \ 