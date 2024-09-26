from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np

# there are diff strategies -> mean, median, most_frequent...

# https://archive.ics.uci.edu/dataset/161/mammographic+mass

columns =["BI-RADS", "Age", "Shape", "Margin", "Density", "Severity"]

data = pd.read_csv("./mammographic_masses.data", names = columns, na_values = ["?"])

imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")

imputer = imputer.fit(data)

data = imputer.transform(data)

print(type(data)) # <class 'numpy.ndarray'>

data = pd.DataFrame(data, columns = columns)

print(data.head(10))

print(data.isnull().sum())

"""
   BI-RADS   Age     Shape    Margin   Density  Severity
0      5.0  67.0  3.000000  5.000000  3.000000       1.0
1      4.0  43.0  1.000000  1.000000  2.910734       1.0
2      5.0  58.0  4.000000  5.000000  3.000000       1.0
3      4.0  28.0  1.000000  1.000000  3.000000       0.0
4      5.0  74.0  1.000000  5.000000  2.910734       1.0
5      4.0  65.0  1.000000  2.796276  3.000000       0.0
6      4.0  70.0  2.721505  2.796276  3.000000       0.0
7      5.0  42.0  1.000000  2.796276  3.000000       0.0
8      5.0  57.0  1.000000  5.000000  3.000000       1.0
9      5.0  60.0  2.721505  5.000000  1.000000       1.0

BI-RADS     0
Age         0
Shape       0
Margin      0
Density     0
Severity    0
dtype: int64

"""
