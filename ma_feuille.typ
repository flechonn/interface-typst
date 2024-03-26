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