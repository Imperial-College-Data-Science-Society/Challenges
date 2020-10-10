import pandas as pd

def get_comments():

    """Get the toxic comments from csv.

    Returns
    -------
    x_train, x_test : Pandas Series of Object Data Type
        Unclean and untokenize Comments
    y_train, y_test : Pandas Dataframe of int64 Data Type
        Labels (either 0 or 1) for each category: toxic, severe_toxic, obscene, threat, insult, identity_hate

    Examples
    --------
    >>> from reader import get_comments
    >>> x_train, y_train, x_test, y_test = get_comments() 

    Notes
    -----
    The data is split into train and test sets as described in the original Kaggle 
    """

    df_train = pd.read_csv('train.csv')
    df_test = pd.read_csv('test_cleaned.csv')
    x_train = df_train['comment_text']
    x_test = df_test['comment_text']
    list_classes = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
    y_train = df_train[list_classes]
    y_test = df_test[list_classes]
    return x_train, y_train, x_test, y_test


if __name__ == "__main__":
    x_train, y_train, x_test, y_test = get_comments()
    print(x_train.head())
    print(y_train.head())
    print(x_test.head())
    print(y_test.head())