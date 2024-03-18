// fichier contenant toute les fonctions pratiques de mise en forme

#let temp(title: [],body) = {
  set text(font: "New Computer Modern Sans",lang: "en",14pt)
  show math.equation: set text(font: "New Computer Modern Math",weight: 400)
  set page ("a4",
    numbering: "---  1  ---",
    number-align: center,
    flipped: false,
    margin: (left:0.5cm, right: 0.5cm, top: 1.8cm, bottom: 1.2cm),
    header: [
    #set text(10pt)
    #h(1fr) Huy-Phan Nhat 
    #h(1fr) _#datetime.today().display()_
  ],
  )
  align(center, text(15pt)[
  *#title*]
  ,
  )
  set heading(numbering: "1.1")
  body  
}
  #import "@preview/physica:0.9.1": *
  #import "@preview/ctheorems:1.1.0": *
  #import "@preview/xarrow:0.2.0": *
  #import "@preview/showybox:2.0.1": *
  #import "@preview/chem-par:0.0.1": *
  #import "@preview/i-figured:0.2.3": *
  #import "@preview/unify:0.4.3": *
  #import "@preview/nth:1.0.0": *
  #let proof = thmplain(
    "proof",
    "Proof",
    separator: [.],
    base: "theorem",
    bodyfmt: body => [
    #body #h(1fr) $square$ // float a QED symbol to the right
    ]
    ).with(numbering: none)
  #let solution = thmplain(
    "proof",
    "Solution",
    separator: [.],
    base: "theorem",
    bodyfmt: body => [
    #body #h(1fr) $square$ // float a QED symbol to the right
    ],
    ).with(numbering: none)
  #let solution2 = thmplain(
    "proof",
    "Solution",
    separator: [:],
    base: "theorem",
    bodyfmt: body => [
    #body #h(1fr) // float a QED symbol to the right
    ],
    ).with(numbering: none)
    
#let iff = "if and only if"
#let spn = $upright("span")$
#let Spn = $upright("Span")$
#let WLOG = "Without loss of generality"
#let wlog = "without loss of generality"
#let rhs = "right hand side"
#let lhs = "left hand side"
#let vsp = "vector space"
#let vsps = "vector spaces"
#let sbsp = "subspace"
#let fn = "function"
#let fns = "functions"
#let lincom = "linear combination"
#let lincoms = "linear combinations"
#let indep = "linearly independent"
#let dep = "linearly dependent"
#let defi = "definition"
#let ax = "axiom"
#let the = "theorem"
#let lem = "lemma"
#let Fn = "Function"
#let Fns = "Functions"
#let pro = "proposition"
#let Pro = "Proposition"
#let Defi = "Definition"
#let Ax = "Axiom"
#let The = "Theorem"
#let Lem = "Lemma"
#let sbs = "subset"
#let un = "union"
#let scamu = "scalar multiplication"
#let sbs = "subspace"
#let adid = "additive identity"
#let lid = "linear dependence lemma"
#let findem = "finite-dimensional"