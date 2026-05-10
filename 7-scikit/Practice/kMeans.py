from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Customers": ["Harry", "Ben", "Lotus", "Karry", "Narry", "Narendra"],
    "Age": [20, 25, 44, 34, 43, 56],
    "Spending": [100, 400, 200, 600, 300, 700]
}

df = pd.DataFrame(data)

x = df[["Age", "Spending"]]

model = KMeans(n_clusters=2, random_state=42, n_init=10)