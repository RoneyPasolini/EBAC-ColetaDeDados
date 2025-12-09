import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados_gasolina_df = pd.read_csv('/content/EBAC-ColetaDeDados/Modulo19/gasolina.csv')

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data = dados_gasolina_df, x='dia', y='venda')

plt.savefig('gasolina.png')