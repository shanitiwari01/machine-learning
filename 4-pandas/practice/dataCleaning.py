import pandas as pd

# Dataset
data = {
    'Name': ['Alice', None, 'Charlie'],
    'Age': [25, None, 35],
    'City': ['New York', None, 'Paris']
}

df = pd.DataFrame(data)

# print(df.isnull())

# df.dropna(axis=0, inplace=True)

# df["Age"].fillna(10, inplace=True)
# df["Age"].fillna(df['Age'].mean(), inplace=True)
# df['Age'].interpolate(method="linear", inplace=True, axis=0)

print(df)