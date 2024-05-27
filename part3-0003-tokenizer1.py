# data

import tensorflow as tf
import pandas as pd

raw_data = pd.read_csv("/IMDB Dataset.csv", engine="python", encoding= "utf-8")

print(raw_data.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50000 entries, 0 to 49999
Data columns (total 2 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   review     50000 non-null  object
 1   sentiment  50000 non-null  object
dtypes: object(2)
memory usage: 781.4+ KB
None

"""
