import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

def plot_variable_pairs(train):
    sns.pairplot(data=train, kind='reg', corner=True)
    return plt.show()

def plot_categorical_and_continuous_vars (train, cat_col, cont_col):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
    sns.boxplot(x=cat_col, y=cont_col, data=train, ax=axes[0])
    axes[0].set_title('Boxplot')

    sns.violinplot(x=cat_col, y=cont_col, data=train, ax=axes[1])
    axes[1].set_title('Violinplot')

    sns.barplot(x=cat_col, y=cont_col, data=train, ax=axes[2])
    axes[2].set_title('Barplot')
    
    return plt.show()