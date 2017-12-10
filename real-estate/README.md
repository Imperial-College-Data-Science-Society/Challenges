# Real Estate

## Data

The Ames housing dataset (1) contains features of houses sold in Ames, IA and their sale prices. The features and prices can be found in `data.csv` or loaded using the provided reader (Python only).
Detailed information about the data can be found in description.txt.

```python
from reader import get_housing_data

# pandas DataFrame
df = get_housing_data()
# available features
df.columns
# house price - the target
df['SalePrice']
```

## Guidance

This is not an exhaustive list of tasks, the points are provided in order to guide you:

### Variable Relationships

Explore and visualize the relationships between the different house features. Identify any correlations between the variables.

### Feature Selection & Engineering

Select the most predictive features to use in the model. Engineer new features to improve model performance.

### Model

Build a regression model. Test the performance of different algorithms.

### Evaluation

Report results of your model and approach. Compare between models. Use appropriate metrics.

## References
1. De Cock D. Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project. Journal of Statistics Education [Internet]. 2011 Nov [cited 2017 Dec 7];19(3). Available from: https://www.tandfonline.com/doi/full/10.1080/10691898.2011.11889627
