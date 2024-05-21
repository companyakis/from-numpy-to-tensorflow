import tensorflow as tf
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.datasets import fetch_california_housing

model_data = fetch_california_housing()

X = model_data.data

y = model_data.target

print(f"Type X: {type(X)} and type y: {type(y)}") # Type X: <class 'numpy.ndarray'> and type y: <class 'numpy.ndarray'>

print(model_data["feature_names"])

print(model_data["target_names"])

"""
Type X: <class 'numpy.ndarray'> and type y: <class 'numpy.ndarray'>

['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

['MedHouseVal']

"""
