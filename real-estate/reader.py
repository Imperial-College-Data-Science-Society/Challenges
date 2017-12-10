import pandas as pd

def get_housing_data():

    """Get the Ames housing dataset.

    Returns
    -------
    data : pd.DataFrame
        Dataframe containing the house features and prices. 

    Examples
    --------
    >>> from reader import get_housing_data
    >>> df = get_housing_data() 

    Notes
    -----
    Description of columns can be found in description.txt.

    References
    ----------
    1. De Cock D. Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project.
    Journal of Statistics Education [Internet]. 2011 Nov [cited 2017 Dec 7];19(3).
    Available from: https://www.tandfonline.com/doi/full/10.1080/10691898.2011.11889627
    """
    
    return pd.read_csv('data.csv')
