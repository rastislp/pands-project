# Rastislav Petras G00252861
# Programming and Scripting
# Iris data set project

import pandas as pd                         # open source data analysis and manipulation tool, built on top of the Python programming language

import seaborn as sns                       # data visualization library based on matplotlib.

import matplotlib.pyplot as plt             # comprehensive library for creating static, animated, and interactive visualizations in Python

import numpy as np                          # fundamental package for scientific computing with Python.

import webbrowser as web

def display_menu():                         # funcion Menu 
    print("")
    print("MENU")
    print("=" * 4)
    print(" 1 - Display Sepal length histogram")
    print(" 2 - Display Sepal width histogram")
    print(" 3 - Display Petal length histogram")
    print(" 4 - Display Petal width histogram")
    print(" 5 - Display Boxplot")
    print(" 6 - Display distribution of sepal length")
    print(" 7 - Display distribution of sepal width")
    print(" 8 - Display distribution of petal length")
    print(" 9 - Display distribution of petal width")
    print("10 - Display scatter plot")
    print("a - About")
    print("q - Exit")
    print()

def about_menu():
	print("")
	print("Press y to explore Iris data set:")
	print("Press anything else to exit to main menu")
	print()



df = sns.load_dataset("iris")               # download iris data set from seaborn library

print()
print()
print("                         Welcome in Iris data sets analysis:")
print()
print("Column and row structure")
print()
print(df.shape)   
print()                       			    # function to display data strucure count of rows and columns
print("Below is a species distibution:")
print()
print(df.groupby('species').size())         # count of rows grouped by spieces 
print()
print("Below is describe function of data:")
print()
print(df.describe())                        # used to view some basic statistical details like percentile, mean, std etc. of a data frame or a series of numeric values
print()
print("Mean value for each individual specie of each type dimension: ")
print()
print(df.groupby('species').mean())
print()
print("Min value for each individual specie of each type dimension: ")
print()
print(df.groupby('species').min())
print()
print("Max value for each individual specie of each type dimension: ")
print()
print(df.groupby('species').max())
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
plt.savefig("Boxplot_group_by_species.png")
plt.clf()  
 
sns.violinplot(data=df, x='species', y='sepal_length')  # shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared.
plt.title("Distribution of sepal lenght")
plt.savefig("violin_plot_sepal_length.png")
plt.clf()  

sns.violinplot(data=df, x='species', y='sepal_width')
plt.title("Distribution of sepal width")
plt.savefig("violin_plot_sepal_width.png")
plt.clf()  

sns.violinplot(data=df, x='species', y='petal_length')
plt.title("Distribution of petal lenght")
plt.savefig("violin_plot_petal_length.png")
plt.clf()  

sns.violinplot(data=df, x='species', y='petal_width')
plt.title("Distribution of petal width")
plt.savefig("violin_plot_petal_width.png")
plt.clf()  

sns.pairplot(df, hue="species")
plt.savefig("scatter_plot.png")
plt.clf()  


display_menu()

while True:
	choice = input("Enter choice: ")
		
	if(choice == "1"):
	    web.open('https://github.com/rastislp/pands-project/blob/master/sepal_length_histogram.png')
        
	elif(choice == "2"):
		web.open('https://github.com/rastislp/pands-project/blob/master/sepal_width_histogram.png')

	elif(choice == "3"):
	    web.open('https://github.com/rastislp/pands-project/blob/master/petal_length_histogram.png')

	elif(choice == "4"):
		web.open('https://github.com/rastislp/pands-project/blob/master/petal_width_histogram.png')
		
	elif(choice == "5"):
		web.open('https://github.com/rastislp/pands-project/blob/master/Boxplot_group_by_species.png')
		
	elif(choice == "6"):
		web.open('https://github.com/rastislp/pands-project/blob/master/violin_plot_sepal_length.png')
		
	elif(choice == "7"):
		web.open('https://github.com/rastislp/pands-project/blob/master/violin_plot_sepal_width.png')

	elif(choice == "8"):
	    web.open('https://github.com/rastislp/pands-project/blob/master/violin_plot_petal_length.png')

	elif(choice == "9"):
		web.open('https://github.com/rastislp/pands-project/blob/master/violin_plot_petal_width.png')
		
	elif(choice == "10"):
		web.open('https://github.com/rastislp/pands-project/blob/master/scatter_plot.png')
		
	elif(choice == "a"):
		print()
		print(" This program Analysis.py is written by Rastislav Petras. Student of Higher Diploma in Data Analytics at GMIT.")
		print("The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician")
		print("and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of ")
		print("linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data")
		print("to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in")
		print("the Gaspé Peninsula all from the same pasture, and picked on the same day and measured at the same time by the same person")
		print("with the same apparatus.")
		print()
		about_menu()
		print()
		while True:
			about = input("Select one: ")
		
			if(about == "y"):
	        		web.open('https://en.wikipedia.org/wiki/Iris_flower_data_set')
	        		display_menu()
	        		break
			else:
				display_menu()	
				break
		

    
		
	elif(choice == "q"):            # when q is pressed aplication will exit
		break
   
	else:
		display_menu()
#def urlopen():
