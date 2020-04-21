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
import pandas as pd

iris_data = pd.read_csv('iris-data.csv')
iris_data.head()
```


![feature extraxtion](https://scontent-lhr8-1.xx.fbcdn.net/v/t1.0-9/91276582_10217815209705930_9016744201081061376_n.jpg?_nc_cat=101&_nc_sid=e007fa&_nc_oc=AQnG_0VONpHMqam7IAkkUj3F71W8EVH1-ITXJ0I42gUXnBTxiR9C9GwNBXeZmc_YIgc&_nc_ht=scontent-lhr8-1.xx&oh=48b5597e7b948b7f31783d51732c199c&oe=5EA9011B)

## Reference:

En.wikipedia.org. 2020. Petal. [online] Available at: <https://en.wikipedia.org/wiki/Petal> [Accessed 15 March 2020].<br>
En.wikipedia.org. 2020. Sepal. [online] Available at: <https://en.wikipedia.org/wiki/Sepal> [Accessed 15 March 2020].<br>
En.wikipedia.org. 2020. The Iris flower. [online] Available at: https://en.wikipedia.org/wiki/Iris_flower_data_set [Accessed 19 April 2020].<br>
