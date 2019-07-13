import pandas as pd 
import numpy as np 
import seaborn as sns
from matplotlib import pyplot as plt 
from matplotlib import style 


df  = pd.read_csv("train.csv")


#This creates a df to show how many null values there are in the columns
total = df.isnull().sum().sort_values(ascending=False)
percent_1 = df.isnull().sum()/df.isnull().count()*100
percent_2 = (round(percent_1, 1)).sort_values(ascending=False)
missing_data = pd.concat([total, percent_2], axis=1, keys=['Total', '%'])


#Need to analyse which data would be most relevant for the ML Model
sur = "Survived"
not_sur = "Not Survived"
new_df = df.head(5)
#Creating a plot to see the different sex and age of the survivors compared to non survivors
#fig, axes = plt.subplots(nrows=1, ncols=2,figsize=(10,4))
men = df[df["Sex"]== "male"]
female = df[df["Sex"] == "female"]
women_sur = female[female["Survived"] == 1]
women_not_sur = female[female["Survived"] == 0]
men_sur = men[men["Survived"] == 1]
men_not_sur = men[men["Survived"] == 0]

"""#Drawing Plots
'''FEMALE'''
ax = sns.distplot(women_sur.Age.dropna(),bins=18, label = sur, color= "g", ax = axes[0], kde =False)
ax = sns.distplot(women_not_sur.Age.dropna(), bins=40, label = not_sur, color="r",  ax = axes[0], kde =False)
ax.legend()
ax.set_title("Female")

'''MALE'''
ax = sns.distplot(men_sur.Age.dropna(), bins=18, label = sur, color= "g", ax = axes[1], kde =False)
ax = sns.distplot(men_not_sur.Age.dropna(), bins=40, label = not_sur, color="r",  ax = axes[1], kde =False)
ax.legend()
ax.set_title("Male")"""


#Comparing different ticket classes to survival by where they embarked their journey 
'''FacetGrid = sns.FacetGrid(df, row='Embarked', size=4.5, aspect=1.6)
FacetGrid.map(sns.pointplot, 'Pclass', 'Survived', 'Sex', palette=None,  order=None, hue_order=None )
FacetGrid.add_legend()'''

#PClass in comparison to Survival
#sns.barplot(x='Pclass', y='Survived', data=df)



