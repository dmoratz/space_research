# Intercoder Reliability Report

_Generated: 2026-05-27 11:41:14_

## Inputs

- Claude processed long frame: 13548 (book x chapter x question) cells across 46 books
- Human-coded books (5): The Martian; The Three-Body Problem; Planet of the Apes; Off on a Comet; Ender's Game
- Paired (Claude + Human) (book, chapter, question) rows: 1440

## Cleaning summary

- Raw human-coded long rows: 1440
- After corrections + NA -> 'Other / Unsure': 1440
- After chapter alignment to Claude: 1440
- Non-canonical values coerced to 'Other / Unsure': 76

## Thresholds

- kappa >= 0.6
- alpha >= 0.667

## Corpus-wide pooled summary

| n_cells| n_one_other| n_cells_excl_one_other| pooled_exact_agreement| mean_kappa| mean_kappa_weighted| mean_alpha| pooled_alpha_all| pooled_alpha_excl_one_other|
|-------:|-----------:|----------------------:|----------------------:|----------:|-------------------:|----------:|----------------:|---------------------------:|
|    1440|         555|                    885|                  0.403|      0.225|               0.499|      0.718|            0.388|                       0.647|

## Pooled-by-question results

| q_number| n_pairs| exact_agreement|  kappa| kappa_weighted|  alpha|scale   |
|--------:|-------:|---------------:|------:|--------------:|------:|:-------|
|        1|     124|           0.355|  0.192|          0.206|  0.794|ordinal |
|        2|     124|           0.226|  0.004|         -0.082|  0.751|ordinal |
|        3|     124|           0.411|  0.230|          0.886|  0.903|ordinal |
|        4|     114|           0.491|  0.360|          0.643|  0.890|ordinal |
|        5|     124|           0.605|  0.477|          0.779|  0.907|ordinal |
|        6|     124|           0.444|  0.269|          0.856|  0.996|ordinal |
|        7|     124|           0.500|  0.270|          0.561|  0.920|ordinal |
|        8|     124|           0.274| -0.079|         -0.313|  0.746|ordinal |
|        9|     124|           0.153|  0.027|             NA| -0.051|nominal |
|       10|     124|           0.540|  0.334|          0.887|  0.943|ordinal |
|       11|     124|           0.234|  0.058|             NA| -0.094|nominal |
|       12|      86|           0.709|  0.558|          0.572|  0.906|ordinal |
