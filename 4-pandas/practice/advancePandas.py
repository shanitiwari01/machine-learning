import pandas as pd

# Dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)

# Add Data
df["Salary"] = [10000, 34000, 53000]

# Insert Data
df.insert(0, "Person Id", ['HDI24', 'SOE24', 'JDI23'])

print(df)

# Update whole colum
df["Salary"] = df["Salary"] + 500

# Update specific location
df.loc[2, "Salary"] = 20000

print(df)

# Delete column
df.drop(columns=["Person Id"], inplace=True)

print(df)