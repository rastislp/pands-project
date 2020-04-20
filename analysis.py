# IPython log file

import pandas as pd            # open source data analysis and manipulation tool, built on top of the Python programming language

import seaborn as sns           # data visualization library based on matplotlib.

import matplotlib.pyplot as plt  # comprehensive library for creating static, animated, and interactive visualizations in Python

import numpy as np      # fundamental package for scientific computing with Python.

df = sns.load_dataset("iris")      # download iris data set from seaborn library
print()
print()
print("                         Welcome in Iris data sets analysis:")
print()
print("Column and row structure")
print()
print(df.shape)
print("Below is a species distibution:")
print(df.groupby('species').size())
print()
print("Below is describe function of data:")
print(df.describe())
plt.hist(df["sepal_length"], color="red")
plt.title("sepal length")
plt.xlabel("length (cm)")
plt.ylabel("Number of flowers")
plt.savefig("sepal_length_histogram.png")
plt.clf()

plt.hist(df["sepal_width"], color="green")
plt.title("sepal width")
plt.xlabel("width (cm)")
plt.ylabel("Number of flowers")
plt.savefig("sepal_width_histogram.png")
plt.clf()

plt.hist(df["petal_length"], color="orange")
plt.title("petal length")
plt.xlabel("length (cm)")
plt.ylabel("Number of flowers")
plt.savefig("petal_length_histogram.png")
plt.clf()

plt.hist(df["petal_width"], color="blue")
plt.title("petal width")
plt.xlabel("width (cm)")
plt.ylabel("Number of flowers")
plt.savefig("petal_width_histogram.png")
plt.clf()

