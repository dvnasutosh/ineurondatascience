# Statistics- Everything Encapsulated

---

## Types of Stats:

---

    - Descriptive Statistics
    - Inferential Statistics

### Descriptive Statistics

---

`<def>`**Summerise data with one value** `<def/>`

    - Central Tendency Of data
      - Dispersion method
      - Proability Theory
      - Probability Distributiion Function

### Inferential Statistics

---

`<def>`**Finds out the conclusion for population based on sample Data** `<def/>`

- Sample/ Population
- Hypothesis Testing
- Z-Test
- T-Test
- F-Test
- Anova Test
- Chi-Square Test

## Types of Data

- Structured Data
  - Numeric Data
    - Continuous ( *e.g. Temperature, Weight*)
    - Discrete  (*e.g. Whole Numbers- Number of Students*)
  - Categorical Data
    - Nominal (*e.g. Gender, Blood Group, Color of hair*)
    - Ordinal (*e.g. Education, Ranking in army*)
- Unstructured Data
  - JSON
  - Video
  - Image
  - Voice
  - Text
  - etc.

## Scales of Measurement

1. Nominal Scale Data

   - QUalitative/Categorical
   - Order doesn't matter
   - e.g. Gender, Color, Labels
2. Ordinal Scale Data

   - Categorical
   - Ranking and Order Matters
   - Difference cannot be measured
   - e.g. Race result- 1st(3min),2nd(5 min), 3rd(10 min)
3. Interval Scale Data

   - The Order matters
   - Difference can be measured
   - Ratio cannot be measured as there is no zero point.
   - E.g. Temperature. 20C vs 10C
4. Ratio Scale Data

   - Ratio can be measured as Zero value exists
   - Order obviously matters
   - e.g. Marks of a student

# Descriptive Statistics

## Measure of Central Tendency

- **Mean**- It is the balance point at which the whole dataset can be balanced. If the whole dataset were to be represented with a single value of majorment This will be one of the major choices
  > ## $\sum_{i=1}^n\frac{x_{i}}{n}$
  >
- **Median**- The positionally central value. Which also can be used to represent a dataset.
  Steps 
  1. sort(dataset,ascending=True)
  2. *If* len(dataset)==odd 
      > # dataset <sub>   $\scriptsize{} [\frac{n+1}{2}]$ </sub>
      *else:*
      > # (dataset <sub> $\scriptsize{} [\frac{n}{2}]$ </sub> +dataset <sub>   $\scriptsize{} [\frac{n}{2}+1]$ </sub>) $\times \frac{1}{2}$
- **Mode** - Highest frequency value amongst all values in a dataset.
     > ##  *max(**dataset**)* 
