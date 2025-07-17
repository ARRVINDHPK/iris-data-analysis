import os
import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('data/iris.csv')
except FileNotFoundError:
    # Load the Iris dataset from a URL
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = pd.read_csv(url)


'''print(df.describe())
df.info()
print()
print(df['species'].value_counts())'''

'''print(df[(df['petal_length'] > 1.35) & (df['petal_length'] < 1.65)])
print("no of flowers in maximum raNGE IS:",len(df[(df['petal_length'] > 1.35) & (df['petal_length'] < 1.65)]))
# Visualizing the Iris dataset
plt.figure(figsize=(10, 6))'''

plt.hist(df['petal_length'], bins=20, color='skyblue')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

plt.scatter(df['sepal_length'], df['sepal_width'], alpha=0.7)
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}

for species, color in colors.items():
    subset = df[df['species'] == species]
    plt.scatter(subset['sepal_length'], subset['sepal_width'], label=species, color=color)

plt.title('Sepal Length vs Width (by Species)')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()

