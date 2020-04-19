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
