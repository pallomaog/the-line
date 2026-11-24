# The Line — Chapter II: Productivity & Labor

An interactive data essay on how U.S. labor productivity and hourly compensation have moved since 1947, and how much the gap between them depends on measurement choices.

**Live page:** https://pallomaog.github.io/the-line/

## Key findings (BLS data, 1947 Q1 – 2026 Q3)

How far labor productivity runs ahead of real hourly compensation, nonfarm business sector:

| Start | Consumer deflator | Output deflator |
|---|---|---|
| 1947 Q1 | +70% | +24% |
| 1979 Q1 | +56% | +18% |

The gap is real under both deflators and about two thirds smaller when pay is deflated with the same output price index used for productivity. Measured as a ratio, so the result does not depend on the scale of the index.

## What the page does

- **Two live measurement controls.** Deflator (consumer prices vs. sector output prices) and index origin (1947 Q1 vs. 1979 Q1). The reader sees how each choice changes the answer.
- **A ratio panel** (productivity ÷ compensation − 1), where zero means the two grow together.
- **A two-point check** from the 2017 baseline to the latest quarter.
- **An explicit limits section** naming what the chart cannot answer: average vs. median pay, labor share, depreciation. Both sides of the published debate are cited.

## Method

| Item | Detail |
|---|---|
| Sources | BLS Productivity and Costs via FRED: OPHNFB, COMPNFB, COMPRNFB, IPDNBS |
| Frequency | Quarterly, seasonally adjusted, 2017 = 100 |
| Consumer deflator | Recovered as COMPNFB ÷ COMPRNFB × 100 (an identity; BLS does not publish it as a series) |
| Output-deflated pay | COMPNFB ÷ IPDNBS × 100 |
| Build check | Re-deflating with the recovered deflator reproduces COMPRNFB to floating-point tolerance |
| Known seam | The BLS consumer deflator switches to CPI-U-RS in 1978 Q1; marked on the chart |

## Repository structure

```
index.html                                    Interactive page (self-contained)
data/chapter2_productivity_compensation.csv   Processed series, 1947Q1–2026Q3
scripts/build_data.py                         Fetches FRED data, verifies the identity, writes the CSV
```

## Reproduce

```bash
python scripts/build_data.py
```

Requires Python 3.9+ and no third-party packages. Data in this repository was retrieved on 24 Nov 2026; later BLS revisions will change values slightly.

## Status

Chapter II of a planned five-chapter project (money, productivity & labor, cost of living, energy, institutions). The separate average-hourly-earnings exhibit on the page is still concept geometry and is labeled as such.

## Author

Palloma Gitahy — Data & Business Intelligence · [LinkedIn](https://linkedin.com/in/pallomagitahy)

## License

Code: MIT. Data: U.S. Bureau of Labor Statistics (public domain), retrieved via FRED, Federal Reserve Bank of St. Louis.
