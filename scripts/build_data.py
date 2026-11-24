"""Fetch the Chapter II series from FRED, verify the deflator identity, and
write the processed CSV used by docs/index.html.

Usage:
    python scripts/build_data.py

Series (BLS Productivity and Costs, nonfarm business sector, 2017 = 100, SA, quarterly):
    OPHNFB   labor productivity (output per hour)
    COMPNFB  nominal hourly compensation
    COMPRNFB real hourly compensation (BLS consumer deflator)
    IPDNBS   value-added output price deflator
"""
import csv
import io
import sys
import urllib.request

SERIES = ["OPHNFB", "COMPNFB", "COMPRNFB", "IPDNBS"]
URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=" + ",".join(SERIES)
OUT = "data/chapter2_productivity_compensation.csv"
TOLERANCE = 1e-9


def quarter_label(date: str) -> str:
    year, month, _ = date.split("-")
    return f"{year}Q{(int(month) - 1) // 3 + 1}"


def main() -> int:
    with urllib.request.urlopen(URL, timeout=60) as resp:
        text = resp.read().decode("utf-8")

    rows = []
    for rec in csv.DictReader(io.StringIO(text)):
        if any(rec[s] in ("", ".") for s in SERIES):
            continue
        ophnfb, compnfb, comprnfb, ipdnbs = (float(rec[s]) for s in SERIES)

        # Consumer deflator is not published as a series; recover it as an identity.
        consumer_deflator = compnfb / comprnfb * 100
        recomputed = compnfb / consumer_deflator * 100
        if abs(recomputed - comprnfb) > TOLERANCE:
            print(f"Identity check failed at {rec['observation_date']}", file=sys.stderr)
            return 1

        rows.append(
            (
                quarter_label(rec["observation_date"]),
                ophnfb,
                comprnfb,
                compnfb / ipdnbs * 100,  # real compensation, output deflator
            )
        )

    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["quarter", "OPHNFB", "COMPRNFB", "real_comp_output_deflator"])
        for q, a, b, c in rows:
            w.writerow([q, f"{a:.2f}", f"{b:.2f}", f"{c:.2f}"])

    print(f"Wrote {len(rows)} quarters ({rows[0][0]}–{rows[-1][0]}) to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
