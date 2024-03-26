#import "BD/TYPST/utilities.typ" :* 
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
#main_meta[title Integration Exercise #h(1fr) duration ($tilde.op$ 30min) | points 20pts] \ 

#show: meta 
difficulty hard
 | solution 1

 \ \ 
#show: exercise 
Write an algorithm to find the maximum element in an array of integers.
#show: solution_header 
 \ \ 
 solution 
 \ 
#show: solution 
 ```py
def find_max_element(arr):
  # Initialize max_element with the first element of the array
  max_element = arr[0]
  
  # Iterate through the array starting from the second element
  for num in arr[1:]:
      # Update max_element if the current element is greater
      if num > max_element:
          max_element = num
  
  # Return the maximum element
  return max_element

# Example usage:
array = [3, 5, 2, 9, 10, 7, 1]
print("Maximum element in the array:", find_max_element(array))

``` \ \ 
#main_meta[title Addition Exercise bonus #h(1fr) duration ($tilde.op$ 30min) | points 10pts] \ 

#show: meta 
difficulty easy

 \ \ 
#show: exercise 
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
```
 \ \ 
