#show terms: meta => {
    let title = label("Addition Exercise")
    let duration = label("30min")
    let difficulty = label("easy")
    let solution = label("1")
    let figures = label("")
    let points = label("10pts")
    let bonus = label("1")
    let author = label("")
    let references = label("Link")
    let language = label("english")
    let material = label("Algo")
    let name = label("exo1")
}

= Exercise

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

= Solution

sum = 5 + 8 + 12 + 3 = 28.
