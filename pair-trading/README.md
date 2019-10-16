# Finance

> `Pairs Trading` strategy

## Definitions

**Pairs Trading** is a statistical arbitrage and convergence trading strategy.

The strategy monitors performance of two historically correlated securities. When the correlation between the two securities temporarily weakens, i.e. one stock moves up while the other moves down, the pairs trade would be to short the outperforming stock and to long the underperforming one, betting that the "spread" between the two would eventually converge.

## Data

Adjusted close prices for S&P500 constitutes are provided from **2010-01-01** to **2017-12-10**,
in the csv file `prices.csv`. Use the provided snippet to import it:

```python
from reader import get_prices

# pandas DataFrame
prices = get_prices()
# list of S&P500 constitutes
symbols = prices.columns
# Apple price
aapl = prices['AAPL']
```

## Guidance

This is not an exhaustive list of tasks, the points are provided in order to guide you:

### Define Universe

503 symbols are provided, narrow down the number of tickers, either randomly or systematically.

### Correlations Pairs

Identify suitable pairs of symbols, whose correlation satisfies our objective.

### Model

Build a regression model.

### Evaluation

Report results of your model and approach. Highlight effectiveness of your this strategy.