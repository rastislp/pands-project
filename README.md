<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/Images/GMIT.jpg > <br>
<h3 align="center">Rastislav Petras g00252861</h3>
</p>


<h3 align="center">Programming and Scripting </h3>
<h3 align="center">Iris data set </h3>

## Iris flower data set
The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other
## Insight into Iris 
Petals are modified leaves that surround the reproductive parts of flowers. They are often brightly coloured or unusually shaped to attract pollinators. Together, all of the petals of a flower are called a corolla(Petal, 2020).

A sepal (/ˈsɛpəl/ or /ˈsiːpəl/) is a part of the flower of angiosperms (flowering plants). Usually green, sepals typically function as protection for the flower in bud, and often as support for the petals when in bloom (Sepal, 2020).

<p align="center">
<img src=https://scontent-lhr8-1.xx.fbcdn.net/v/t1.0-9/91546695_10217815430031438_6635654391338631168_n.jpg?_nc_cat=109&_nc_sid=e007fa&_nc_oc=AQlGEa9PB17-jqYLO8hLQebdGO7efA26cl7sKxnYgns_IZFlVAI-35GzICcFA9ZM_qs&_nc_ht=scontent-lhr8-1.xx&oh=d3e6753ac73d8e3801d73fa3c890b8ac&oe=5EAA39E1> </p>

<p align="center">
<img src=https://scontent-lht6-1.xx.fbcdn.net/v/t1.0-9/90604043_10217753213596066_4742260450224242688_n.jpg?_nc_cat=108&_nc_sid=e007fa&_nc_oc=AQl04voN31mICTnqOfwfAhYkC4XL1-qDnO_dJgbpkh8yz0Cz11hX8nhXVgSazaGWbVQ&_nc_ht=scontent-lht6-1.xx&oh=43266b8962d0ce95163244bb2f7db6bb&oe=5EA9ACF2> </p>

Main key points about dataset:
* main data strucure is 4 columns and 150 rows
* name of those columns are as follow sepal length, sepal width, petal length, petal width.
* in addition there is another column "species" that categorize and name given data
* categories represent 3 flowers: Iris setosa, Iris Verginica, Iris versicolor.
* all types of data are distributed equaly between 3 flowers.

<h3 align="center">Some of excel data strucure analysis prior python deployment  </h3>

<p align="center">
<img src=https://scontent-lht6-1.xx.fbcdn.net/v/t1.0-9/91468972_10217815209665929_8933676484149641216_n.jpg?_nc_cat=105&_nc_sid=e007fa&_nc_oc=AQmr6mVjQHv7SBT2QOlEzavgI1v9Nh22RwV-Cy7DrSS6WTiF-EI2wsPGGBnVN_kR2iw&_nc_ht=scontent-lht6-1.xx&oh=78a6a86028353a770a33e5f755e7276b&oe=5EA87ED9> </p>


### Required libraries


This project uses several Python packages that come standard with the Anaconda Python distribution. The primary libraries that we'll be using are:

* matplotlib: comprehensive library for creating static, animated, and interactive visualizations in Python
* Seaborn: data visualization library based on matplotlib.
* webbrowser: module provides a high-level interface to allow displaying Web-based documents to users

```javascript
import seaborn as sns                 
import matplotlib.pyplot as plt       
import webbrowser as web					    
```
### Program menu and submenu functions

These are special features of analysis program. Selecting between numbers 1-10 would open a selected plot via webbrowser.
Option "a" will opens a submenu while option "q" will terminate application.

```javascript
def display_menu():                      
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
```
### Load dataset

Load_dataset function library load Iris data set within a seaborn library a store them as variable df.

```javascript
df = sns.load_dataset("iris") 
```
### Column and row structure

Function to display data strucure count of rows and columns.

```javascript
print(df.shape)   
```
<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/Images/shape.png > <br></p>
### Species distibution

Count of rows grouped by spieces

```javascript
print(df.groupby('species').size())
```
<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/Images/species.png > <br></p>

### Describe 

Used to view some basic statistical details like percentile, mean, std etc. of a data frame or a series of numeric values.

```javascript
print(df.describe())  
```
<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/Images/describe.png > <br></p>

### Mean

Mean value for each individual specie of each type dimension.

```javascript
print(df.groupby('species').mean())	
```
<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/Images/mean.png > <br></p>

### Min

Min value for each individual specie of each type dimension.

```javascript
print(df.groupby('species').min())
```
<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/Images/min.png > <br></p>

### Max

Max value for each individual specie of each type dimension.

```javascript
print("Max value for each individual specie of each type dimension: ")
print(df.groupby('species').max())
```

<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/Images/max.png > <br></p>


### Histograms

```javascript
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
```

<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/Images/histogram.png > <br></p>

### Boxplot

Boxplot is a graph with a good indication of how the values in the data are spread out.

```javascript
df.boxplot(by= 'species', grid=True)        
plt.savefig("Boxplot_group_by_species.png")
plt.clf()
```
<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/Boxplot_group_by_species.png > <br></p>

### Violinplot

Shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared.

```javascript
sns.violinplot(data=df, x='species', y='sepal_length')  
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
```
<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/Images/violin.png > <br></p>

### Pairplot Matrix

Seaborn function library to plot matrix of 16 plots.

```javascript
sns.pairplot(df, hue="species")       					
plt.savefig("scatter_plot.png")
plt.clf() 
```
<p align="center">
<img src= https://github.com/rastislp/pands-project/blob/master/scatter_plot.png > <br></p>

## Reference:

En.wikipedia.org. 2020. Petal. [online] Available at: <https://en.wikipedia.org/wiki/Petal> [Accessed 15 March 2020].<br>
En.wikipedia.org. 2020. Sepal. [online] Available at: <https://en.wikipedia.org/wiki/Sepal> [Accessed 15 March 2020].<br>
En.wikipedia.org. 2020. The Iris flower. [online] Available at: https://en.wikipedia.org/wiki/Iris_flower_data_set [Accessed 19 April 2020].<br>
