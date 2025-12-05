# código de geração do gráfico 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dados_gasolina_df = pd.read_csv('/content/EBAC-ColetaDeDados/Modulo18/gasolina.csv')
#dados_gasolina_df.head()

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data= dados_gasolina_df, x='dia', y='venda')
  grafico.set(title='Preçõ da gasolina por dia', xlabel='Dia', ylabel='Preço da gasolina')

#Comando para salvar o grafico gerado
plt.savefig('gasolina.png')