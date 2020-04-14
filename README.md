# pands-project
Final project

## Insight into Iris 
Petals are modified leaves that surround the reproductive parts of flowers. They are often brightly coloured or unusually shaped to attract pollinators. Together, all of the petals of a flower are called a corolla(Petal, 2020).

A sepal (/ˈsɛpəl/ or /ˈsiːpəl/) is a part of the flower of angiosperms (flowering plants). Usually green, sepals typically function as protection for the flower in bud, and often as support for the petals when in bloom (Sepal, 2020).

![feature extraxtion](https://scontent-lhr8-1.xx.fbcdn.net/v/t1.0-9/91546695_10217815430031438_6635654391338631168_n.jpg?_nc_cat=109&_nc_sid=e007fa&_nc_oc=AQlGEa9PB17-jqYLO8hLQebdGO7efA26cl7sKxnYgns_IZFlVAI-35GzICcFA9ZM_qs&_nc_ht=scontent-lhr8-1.xx&oh=d3e6753ac73d8e3801d73fa3c890b8ac&oe=5EAA39E1)

![feature extraxtion](https://scontent-lht6-1.xx.fbcdn.net/v/t1.0-9/90604043_10217753213596066_4742260450224242688_n.jpg?_nc_cat=108&_nc_sid=e007fa&_nc_oc=AQl04voN31mICTnqOfwfAhYkC4XL1-qDnO_dJgbpkh8yz0Cz11hX8nhXVgSazaGWbVQ&_nc_ht=scontent-lht6-1.xx&oh=43266b8962d0ce95163244bb2f7db6bb&oe=5EA9ACF2)

Main key points about dataset:
* main data strucure is 4 columns and 150 rows
* name of those columns are as follow sepal length, sepal width, petal length, petal width.
* in addition there is another column "species" that categorize and name given data
* categories represent 3 flowers: Iris setosa, Iris Verginica, Iris versicolor.
* all types of data are distributed equaly between 3 flowers.

![feature extraxtion](https://scontent-lht6-1.xx.fbcdn.net/v/t1.0-9/91468972_10217815209665929_8933676484149641216_n.jpg?_nc_cat=105&_nc_sid=e007fa&_nc_oc=AQmr6mVjQHv7SBT2QOlEzavgI1v9Nh22RwV-Cy7DrSS6WTiF-EI2wsPGGBnVN_kR2iw&_nc_ht=scontent-lht6-1.xx&oh=78a6a86028353a770a33e5f755e7276b&oe=5EA87ED9)

![feature extraxtion](https://scontent-lhr8-1.xx.fbcdn.net/v/t1.0-9/91276582_10217815209705930_9016744201081061376_n.jpg?_nc_cat=101&_nc_sid=e007fa&_nc_oc=AQnG_0VONpHMqam7IAkkUj3F71W8EVH1-ITXJ0I42gUXnBTxiR9C9GwNBXeZmc_YIgc&_nc_ht=scontent-lhr8-1.xx&oh=48b5597e7b948b7f31783d51732c199c&oe=5EA9011B)





{
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>sepal_length_cm</th>\n",
       "      <th>sepal_width_cm</th>\n",
       "      <th>petal_length_cm</th>\n",
       "      <th>petal_width_cm</th>\n",
       "      <th>class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   sepal_length_cm  sepal_width_cm  petal_length_cm  petal_width_cm  \\\n",
       "0              5.1             3.5              1.4             0.2   \n",
       "1              4.9             3.0              1.4             0.2   \n",
       "2              4.7             3.2              1.3             0.2   \n",
       "3              4.6             3.1              1.5             0.2   \n",
       "4              5.0             3.6              1.4             0.2   \n",
       "\n",
       "         class  \n",
       "0  Iris-setosa  \n",
       "1  Iris-setosa  \n",
       "2  Iris-setosa  \n",
       "3  Iris-setosa  \n",
       "4  Iris-setosa  "
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "iris_data = pd.read_csv('iris-data.csv')\n",
    "iris_data.head()"
   ]
  }












### Required libraries


This project uses several Python packages that come standard with the Anaconda Python distribution. The primary libraries that we'll be using are:

NumPy: Provides a fast numerical array structure and helper functions.
pandas: Provides a DataFrame structure to store data in memory and work with it easily and efficiently.
matplotlib: Basic plotting library in Python; most other Python plotting libraries are built on top of it.
Seaborn: Advanced statistical plotting library.






## Reference:

En.wikipedia.org. 2020. Petal. [online] Available at: <https://en.wikipedia.org/wiki/Petal> [Accessed 15 March 2020].
En.wikipedia.org. 2020. Sepal. [online] Available at: <https://en.wikipedia.org/wiki/Sepal> [Accessed 15 March 2020].
