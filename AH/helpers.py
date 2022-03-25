from decimal import InvalidOperation
import itertools
import pandas as pd 

def flatten_axes(axes):
    """
    This can take a 2D axes array and flattens it such that you can iterate over
    it 
    """
    return list(itertools.chain(*axes))

def iter_dict(dict):
    for k,v in dict.items():
        yield (k,v)

def split_df(df, attr, var, comp='==', copy=False):
    """
    splits a df based on common operators 
    could solve with less code and evals 
    but we're not that stupid... well, we are but still
    """
    if comp == "==":
        return df[df[attr] == var].copy() if copy else df[df[attr] == var]
    elif comp == "<":
        return df[df[attr] < var].copy() if copy else df[df[attr] < var]
    elif comp == ">":
        return df[df[attr] > var].copy() if copy else df[df[attr] > var]
    elif comp == "<=":
        return df[df[attr] <= var].copy() if copy else df[df[attr] <= var]
    elif comp == ">=":
        return df[df[attr] >= var].copy() if copy else df[df[attr] >= var]
    elif comp == "!=":
        return df[df[attr] != var].copy() if copy else df[df[attr] != var]
    else:
        raise InvalidOperation("Bad comparator")

def split_all(df, attr):
    """ 
    Splits a DF onto all unique conditions and returns list of subdfs 
    """
    dfs = []
    for att in df[attr].unique():
        dfs.append(split_df(df, attr, att))
    return dfs
