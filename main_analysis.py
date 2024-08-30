import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ctt_coef = pd.read_csv('item_ctt_coef.csv')
ctt_coef = ctt_coef[['itemName', 'itemMean']].set_index('itemName')

irt_coef = pd.read_csv('item_irt2pl_coef.csv')
irt_coef = irt_coef[['Unnamed: 0', 'a', 'b']].set_index('Unnamed: 0')

irt_fit = pd.read_csv('item_irt2pl_fit.csv')
irt_fit.drop(columns='Unnamed: 0', inplace=True)
irt_fit = irt_fit.set_index('item')

df = pd.concat([ctt_coef, irt_coef, irt_fit], axis='columns')
df_lite = df.loc[~df.index.isin(['T11', 'T30'])]

sns.scatterplot(df_lite, x='b', y='itemMean')

df.to_csv('item_summary.csv')
