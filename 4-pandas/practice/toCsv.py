import pandas as pd

data = {
    "Name": ["Shani", "Hani", "Money"],
    "Age": [20, 38, 24]
}

df = pd.DataFrame(data)

print(df)

df.to_csv("/Users/shanitiwari/Documents/machine-learning/4-pandas/practice/dataset/Output.csv", index=False)