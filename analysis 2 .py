# IPython log file

import pandas as pd                         # open source data analysis and manipulation tool, built on top of the Python programming language

import seaborn as sns                       # data visualization library based on matplotlib.

import matplotlib.pyplot as plt             # comprehensive library for creating static, animated, and interactive visualizations in Python

import numpy as np                          # fundamental package for scientific computing with Python.

def display_menu():
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - Display Sepal length histogram")
    print("2 - Display Sepal width histogram")
    print("3 - Display Boxplot")
    print("4 - Exit")

if __name__ == "__main__":
	# execute only if run as a script 
	main()

df = sns.load_dataset("iris")               # download iris data set from seaborn library
print()
print()
print("                         Welcome in Iris data sets analysis:")
print()
print("Column and row structure")
print()
print(df.shape)   
print()                          # function to display data strucure count of rows and columns
print("Below is a species distibution:")
print()
print(df.groupby('species').size())         # count of rows grouped by spieces 
print()
print("Below is describe function of data:")
print()
print(df.describe())                        # used to view some basic statistical details like percentile, mean, std etc. of a data frame or a series of numeric values
print()
print("Dont forget to check folder for histograms and scatter plots. ")
print("https://github.com/rastislp/pands-project.git")
print()

#df.hist()                                  # 4 in 1 histogram  

plt.hist(df["sepal_length"], color="red")   # plot histogram of data from sepal_length collumn in red colour
plt.title("sepal length")                   # Create a title "sepal length" 
plt.xlabel("length (cm)")                   # create label on x-axis
plt.ylabel("Number of flowers")             # create label on y-axis
plt.savefig("sepal_length_histogram.png")   # save histogram figure
plt.clf()                                   # clear current figure

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

df.boxplot(by= 'species', grid=True)        # boxplot is a graph with a good indication of how the values in the data are spread out.
plt.savefig("Boxplot group by species.png")
plt.clf()  
 

display_menu()
	
while True:
	choice = input("Enter choice: ")
		
	if (choice == "1"):
		start https://github.com/rastislp/pands-project/blob/master/petal_length_histogram.png
	elif (choice == "2"):
		start https://github.com/rastislp/pands-project/blob/master/petal_length_histogram.png
	elif (choice == "3"):
		start https://github.com/rastislp/pands-project/blob/master/petal_length_histogram.png
	elif (choice == "4"):
		break;
	else:
		display_menu()