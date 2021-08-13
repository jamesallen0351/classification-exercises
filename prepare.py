import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

import warnings
warnings.filterwarnings("ignore")

import acquire

# getting iris data from acquire 
df = acquire.get_iris_data()

# Drop the species_id and measurement_id columns 
# mesurement_id not selected in aquire file
df = df.drop(columns = ['species_id'])

# Rename the species_name column to just species.

df = df.rename(columns={"species_name": "species"})

# Create dummy variables of the species name.
df_dummy = pd.get_dummies(df[['species']])

# append dummy df cols to the original df. 
df = pd.concat([df, df_dummy], axis = 1)


# Create a function named prep_iris that accepts the untransformed iris data, and returns the data with the transformations above applied.

def prep_iris(df):

    df.drop(columns = ['species_id'])
    df.rename(columns={"species_name": "species"})
    df_dummy = pd.get_dummies(df[['species']])
    
    return pd.concat([df, df_dummy], axis = 1)