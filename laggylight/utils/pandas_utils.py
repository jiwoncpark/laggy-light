from __future__ import absolute_import, division, print_function

import pandas as pd
import numpy as np

__all__ = ['dict_of_dict_to_columns', 'a_relationship_b', 'get_unique_values', 'gaussian_noise',]

def dict_of_dict_to_columns(main_df, dict_column, dict_key):
    """Converts a dictionary entry of a dictionary defined in string format into columns"""
    
    if isinstance(main_df[dict_column][0], dict):
        # Already of type dict
        pass
    else:
        # Convert unicode to dict in dict_column 
        main_df[dict_column] = main_df[dict_column].apply(eval)
    strdict_df = (main_df[dict_column].copy().apply(pd.Series))[dict_key].copy().apply(pd.Series)
    main_df = pd.concat([main_df.drop([dict_column, ], axis=1), strdict_df], axis=1)
    return main_df

def a_relationship_b(a, b, column=None, column_a=None, column_b=None, relationship='subset'):
    """Checks if the unique values of a column in dataframe a form a subset of those in b
    Parameters
    ----------
    a : Pandas.Dataframe
    b : Pandas.Dataframe
    column : str
    column_a : str
    column_b : str
    
    """
    
    if column_a is None and column_b is None:
        if column is not None:
            column_a = column
            column_b = column
        else:
            raise ValueError("Must define column if not defining column_a and column_b.")
    elif column_a is not None and column_b is not None:
        if column is not None:
            raise ValueError("Cannot define column if defining column_a and column_b.")
        else:
            pass
    else:
        raise ValueError("Must define both column_a and column_b or neither.")
    
    values_a = set(a[column_a].unique().copy())
    values_b = set(b[column_b].unique().copy())
    
    if relationship=='subset':
        return values_a.issubset(values_b)
    elif relationship=='superset':
        return values_a.issuperset(values_b)
    elif relationship=='equal':
        return values_a == values_b
    else:
        valueError("Relationship must be one of 'subset', 'superset', 'equal'.")

def gaussian_noise(mean, stdev, shape=None, measurement=1.0):
    """Given a mean and a standard deviation of a measurement, adds Gaussian noise to the data
    
    Parameters
    ----------
    mean : float
        the mean of Gaussian
    stdev : float
        the standard deviation of Gaussian
    shape : array or list or None
        the shape of noise to be returned
        If None, returns a scalar noise [default: None]
    measurement : float
        scaling factor, for adding fractional errors.
        If 1.0, error is absolute. [default: 1.0]
                   
    """
    return measurement*np.random.normal(loc=mean, scale=stdev, size=shape)
