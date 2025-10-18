import pandas as pd

# dataFrame = pd.read_csv("/Users/shanitiwari/Documents/machine-learning/4-pandas/practice/dataset/NQ_in_1_hour.csv")

dataFrame = pd.read_json("/Users/shanitiwari/Documents/machine-learning/4-pandas/practice/dataset/dataset-metadata.json")

print(dataFrame)