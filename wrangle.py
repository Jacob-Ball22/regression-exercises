import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

import env
import os

def wrangle_zillow():
    """
    Acquires the zillow data from the CodeUp MySQL database
    Drops all 12,628 null values in the data (0.58% of the data)
    Changes data types for listed columns from float to int
    - bedroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, and fips
    """
    #Acquire the data
    url = env.get_db_url('zillow')
    df = pd.read_sql('''select bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
    from propertylandusetype
        join properties_2017
            using (propertylandusetypeid)
    WHERE propertylandusedesc = ("Single Family Residential");''', url)
    
    #Dropped nulls which drops 0.58% of the original data
    df = df.dropna()
    
    #Changed data types to int instead of float
    df.bedroomcnt = df.bedroomcnt.astype(int)
    df.calculatedfinishedsquarefeet = df.calculatedfinishedsquarefeet.astype(int)
    df.taxvaluedollarcnt = df.taxvaluedollarcnt.astype(int)
    df.yearbuilt = df.yearbuilt.astype(int)
    df.fips = df.fips.astype(int)
    
    return df
    
def split_data(df, col):
    """
    Recieves dataframe as 'df' and target variable to stratify as 'col'
    First split does a 60% train and 40% validate
    Second split uses the 40% validate to make 50% validate and 50% test
    """
    #first split
    train, validate_test = train_test_split(df, #send in initial df
                train_size = 0.60, #size of the train df, and the test size will default to 1-train_size
                random_state = 123, #set any number here for consistency
                stratify = df[col] #we should stratify on our target variable
                )
    
    #second split
    validate, test = train_test_split(validate_test, #we are spliting the 40% df we just made
                test_size = 0.50, #split 50/50
                random_state = 123, #gotta send in a random seed
                stratify = validate_test[col] #still got to stratify
                )
    
    return train, validate, test