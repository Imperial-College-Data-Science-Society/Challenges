# Time Series

> `Volatility Prediction` 

## Definitions

Option pricing models, such as **Black–Scholes Model**, relies on reliable predictions
of implied volatility. **VIX** (CBOE Volatility Index) is a popular measure of the stock
market's expectation of volatility implied by S&P500 index options,
calculated and published by the Chicago Board Options Exchange (CBOE).

## Data

VIX values are provided, in the csv file `volatility.csv`. Use the provided snippet to import it:

```python
from reader import get_ivx

# pandas DataFrame
volatility = get_ivx()
```

## Guidance

This is not an exhaustive list of tasks, the points are provided in order to guide you:

### Decide on Model Nature (Generative or Discriminative)



### Model

Build a regression model.

### Evaluation

Report results of your model and approach. Highlight effectiveness of your this strategy.