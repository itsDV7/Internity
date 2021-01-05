import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\Code\Python\Pokemon.csv", index_col=0)
print(df.head())

sns.boxplot(data=df)
plt.show()

stats = df.drop(['Total','Stage','Legendary'], axis=1)
sns.boxplot(data=stats)
plt.show()

sns.catplot(data=stats,kind='box')
plt.show()

sns.set_style('whitegrid')
sns.boxplot(data=stats)
plt.show()

sns.barplot(x='Type 1',y='Defense',data=df)
plt.show()

sns.catplot(x='Type 1',y='Defense',data=stats,kind='bar')
plt.show()

set_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]

sns.barplot(x='Type 1',y='Defense',data=df, palette=set_colors)
plt.show()

sns.catplot(x='Type 1',y='Defense',data=df, palette=set_colors, kind='bar')
plt.show()

plt.figure(figsize=(12,8))
sns.swarmplot(x='Type 1',y='Defense',data=df,color='Red')
sns.boxplot(x='Type 1',y='Defense',data=df,palette=set_colors,saturation=0.1)
plt.title('Type vs Defense')
plt.show()

new_color = ['#FF0000', #Stage 1
             '#00FF00', #Stage 2
             '#0000FF', #Stage 3
            ]

sns.kdeplot(df.Attack, df.Defense, shade_lowest=True,hue='Stage',data=df,palette=new_color)
plt.show()

sns.histplot(x=df.Defense,stat='count',kde=True,data=df)
plt.show()

sns.jointplot(x='Defense',y='Type 1',data=df)
plt.show()

sns.jointplot(x='Defense',y='Attack',data=df,hue="Type 1",palette=set_colors)
plt.show()


facet = sns.FacetGrid(df,col='Stage',col_wrap=5,hue="Type 1",palette=set_colors)
facet.map(sns.scatterplot,"Attack","Defense")
facet.add_legend()
plt.show()

