import pandas as pd
import numpy as np

# https://archive.ics.uci.edu/dataset/161/mammographic+mass

columns =["BI-RADS", "Age", "Shape", "Margin", "Density", "Severity"]

data = pd.read_csv("./mammographic_masses.data", names = columns, na_values = ["?"])

print(data.head(10))

"""
   BI-RADS   Age  Shape  Margin  Density  Severity
0      5.0  67.0    3.0     5.0      3.0         1
1      4.0  43.0    1.0     1.0      NaN         1
2      5.0  58.0    4.0     5.0      3.0         1
3      4.0  28.0    1.0     1.0      3.0         0
4      5.0  74.0    1.0     5.0      NaN         1
5      4.0  65.0    1.0     NaN      3.0         0
6      4.0  70.0    NaN     NaN      3.0         0
7      5.0  42.0    1.0     NaN      3.0         0
8      5.0  57.0    1.0     5.0      3.0         1
9      5.0  60.0    NaN     5.0      1.0         1    
    
    
"""
