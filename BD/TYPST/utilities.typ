// GLOBAL SHEET TEMPLATE

#set text(
  font: "Inria Serif",
  size: 10pt,
)
#set page(
  paper: "a4",
)

// SHEET HEADING TEMPLATE 
#let title(doc) = [
  #set text(16pt)
  #doc
]

#let header(doc) = [
  #set align(center)
  #set text(12pt, weight: "bold")
  #show "author" : [Author]
  #show "date" : [Date]
  #show "duration" : [Duration]
  #doc
]

#let modality(doc) = [
  #set text(10pt, weight: "regular")
  #set align(start)
  #set par(justify: true)
  #doc
]

#let lines(doc) = [
  #line(length: 100%)
  #doc
]

// SHEET CONTENT (EXERCISES) TEMPLATE

#let body(doc) = [
  #set text(font: "Inria Serif", 11pt)
  #doc
]

#let meta(doc) = [
  #set text(font: "Inria Serif", 8pt)
  #doc
]