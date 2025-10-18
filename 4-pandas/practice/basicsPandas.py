import pandas as pd

df = pd.read_csv("/Users/shanitiwari/Documents/machine-learning/4-pandas/practice/dataset/NQ_in_1_hour.csv")

# Starting 10 rows
print(df.head(10))

# Ending 10 rows
print(df.tail(10))

# Dataset Info
print(df.info())

# Descriptive Statistics
print(df.describe())

# Number of rows, and column
print(df.shape)

# Column names
print(df.columns)

# Accessing Series
series = df['volume']
print(series)

# Select multiple column
print(df[['open', 'close']])

# Filtering rows
filterRows = df[(df['open'] > 18000) & (df['close'] < 20000)]
print(filterRows)