%%writefile gasolina.csv

dia,venda

1,5.11

2,4.99

3,5.02

4,5.21

5,5.07

6,5.09

7,5.13

8,5.12

9,4.94

10,5.03

import pandas as pd

csv_file = "gasolina.csv"
gasolina_df = pd.read_csv(csv_file)

import seaborn as sns
import matplotlib.pyplot as plt

with sns.axes_style('whitegrid'):
    grafico = sns.barplot(data=gasolina_df, x="dia", y="venda", errorbar=None, palette="pastel")
    grafico.set(title='Preço da Gasolina por dia', xlabel='Dia', ylabel='Preço')

    plt.savefig("gasolina.png")

import seaborn as sns
import matplotlib.pyplot as plt

with sns.axes_style('whitegrid'):
    grafico = sns.lineplot(data=gasolina_df, x='dia', y='venda')
    grafico.set(title='Preço da Gasolina por dia', xlabel='Dia', ylabel='Preço')

plt.savefig("gasolina.png")
