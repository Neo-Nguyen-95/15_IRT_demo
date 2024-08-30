#%% LOAD
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('toan_de1.csv', index_col='student_id')

#%% EDA
# filter student with more than 25% of NA value (10 blank items)
df_item = df.T
df_remove = (df_item == ' ').sum().sort_values(ascending=False)
df_remove = df_remove[df_remove > 7]
remove_list = list(df_remove.index)

df_filter = df.loc[~df.index.isin(remove_list)]

# replace str to int value
df_filter = (df.replace(' ', 0)
             .replace('0', 0)
             .replace('1', 1)
             )  # replace blank value with 0

df_filter['raw_score'] = df_filter.sum(axis='columns')
df_filter = df_filter[df_filter['raw_score'] > 5]   # filter students <= 5

#%% CTT ANALYSIS
# item CTT difficulty
plt.figure(figsize=(16, 9), dpi=200)
data = df_filter.iloc[:, 0:40].mean().rename('CTT_diff').to_frame().reset_index()
sns.barplot(data=data, x='index', y='CTT_diff' )

# student raw score
plt.figure(dpi=200)
sns.histplot(data=df_filter, x='raw_score')

#%% EXPORT FOR IRT ANALYSIS
df_filter.iloc[:, 0:40].to_csv('toan_de1_cleaned.csv', index=False)
