#import "../BD/TYPST/utilities.typ" :* 
#show: title 
 \ 
hagrid
#show: lines 
#show: header 
 \ 
#show: modality 
#show: lines 
 \ 
#main_meta[title Addition Exercise bonus #h(1fr) duration ($tilde.op$ 30min) | points 10pts] \ 

#show: meta 

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
#main_meta[title Integration Exercise #h(1fr) duration ($tilde.op$ 30min) | points 20pts] \ 

#show: meta 

 \ \ 
#show: exercise 
Write an algorithm to find the maximum element in an array of integers.
 \ \ 
