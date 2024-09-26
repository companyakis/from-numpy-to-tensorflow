import pandas as pd
import numpy as np

# https://archive.ics.uci.edu/dataset/161/mammographic+mass

columns =["BI-RADS", "Age", "Shape", "Margin", "Density", "Severity"]

data = pd.read_csv("./mammographic_masses.data", names = columns, na_values = ["?"])

data = data.dropna()

print(data.head(10))

print(data.isnull().sum())

"""

    BI-RADS   Age  Shape  Margin  Density  Severity
0       5.0  67.0    3.0     5.0      3.0         1
2       5.0  58.0    4.0     5.0      3.0         1
3       4.0  28.0    1.0     1.0      3.0         0
8       5.0  57.0    1.0     5.0      3.0         1
10      5.0  76.0    1.0     4.0      3.0         1
11      3.0  42.0    2.0     1.0      3.0         1
13      4.0  36.0    3.0     1.0      2.0         0
14      4.0  60.0    2.0     1.0      2.0         0
15      4.0  54.0    1.0     1.0      3.0         0
16      3.0  52.0    3.0     4.0      3.0         0


BI-RADS     0
Age         0
Shape       0
Margin      0
Density     0
Severity    0
dtype: int64

"""
