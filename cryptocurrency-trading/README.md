# Cryptocurrency Trading

## Background

Financial markets are often modelled as regression problems. The most unpredictable movements were those of cryptocurrencies. Can you predict their future values?

## Dataset

This dataset contains data for 4 cryptocurrencies (Bitcoin, Ethereum, Ripple, Bitcoin-Cash) over a 5 year period 2013-2018. Provided data is all in $USD and includes open/close, high/low, volume traded, spread and close ratio. Close ratio is defined as:

```
Close Ratio = (Close - Low)/(High - Low)
```

The dataset is provided in a simple `.csv` file. It is recommended to use the Python packages `numpy` and `pandas` to read and manipulate the data. Choice of programming language is not restricted, however Imperial Strategics & Data Science Society projects/workshops are in Python. 

## Guidance

This is not an exhaustive list of tasks, the points are provided in order to guide you:

### Understanding the Data

Limited features are provided in the dataset and so it may be useful to derive your own. Explain the thought process behind any decisions you make here.

### Feature Selection & Engineering

Select the most predictive features in the model. Which are useful and which aren't?

### Model

Select an appropriate regression model and tune it to improve its performance.

### Evaluation

Report your results using appropriate metrics and explain key decisions in your process. Suggest possible improvements.