from sklearn.datasets import fetch_california_housing

dataset_housing = fetch_california_housing()

print(dataset_housing.feature_names)

print(dataset_housing.target_names)

"""
['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

['MedHouseVal']
"""
