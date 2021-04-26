# Required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import datetime, re

#Reading pastry dataset
df = pd.read_csv('../datasets/coffee_shop/pastry.csv')

# Drops null values
df.dropna(inplace = True)

# Replaces column to remove special character
df = df.rename(columns={'% waste': 'pct_waste'})

# Converts percentage strings to equivalent numbers
df["pct_waste"] = df["pct_waste"].replace({'%':''}, regex=True).astype(int) / 100

# Converts percentage strings to equivalent numbers
df["transaction_weekday"] = pd.to_datetime(df['transaction_date'], format = '%m/%d/%Y').dt.dayofweek

sns.jointplot(df)

# save heatmap as .png file
# dpi - sets the resolution of the saved image in dots/inches
plt.figure(figsize=(16, 6))
heatmap = sns.heatmap(df.corr(), annot = True)
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':18}, pad=12);
# plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
#plt.show()
