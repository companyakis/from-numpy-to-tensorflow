from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

# there are diff strategies -> mean, median, most_frequent...

# https://archive.ics.uci.edu/dataset/161/mammographic+mass

columns =["BI-RADS", "Age", "Shape", "Margin", "Density", "Severity"]

data = pd.read_csv("./mammographic_masses.data", names = columns, na_values = ["?"])

print(data.isnull().sum())

imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")

"""

BI-RADS      2
Age          5
Shape       31
Margin      48
Density     76
Severity     0
dtype: int64

"""
