import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('C:\\Users\\saketh\\Documents\\health insurance\\train.csv')
print(df.head(10))
print(df.shape[0])
print(df.shape[1])
print(df.info())
print(df.describe())
print(df.isna().sum())
print([i for i in df.columns if df[i].dtype=='object'])
print([i for i in df.columns if df[i].dtype=='int64'or'float64'])
print(df.corr())
for i in df.columns:
    print(df[i].unique())
cat_cols=[i for i in df.columns if df[i].dtype=='object']
num_cols=[j for j in df.columns if (df[j].dtype=='int64')|(df[j].dtypes=='float64')]
fig, axes=plt.subplots(2,2, figsize=(10,10))
for i, j in enumerate(cat_cols):
    ax=axes[int(i/2),i%2]
    sns.countplot(df[j], ax=ax)
fig.delaxes(axes[1,1])
plt.show()
df['Driving_License'].value_counts().plot(kind='bar')
plt.show()
df['Previously_Insured'].value_counts().plot(kind='bar')
plt.show()
kde_data=['Age','Annual_Premium','Vintage']
fig, axes=plt.subplots(2,2, figsize=(10,10))
for i,j in enumerate(kde_data):
    ax=axes[int(i/2), i%2]
    sns.kdeplot(df[j], ax=ax)
fig.delaxes(axes[1,1])
plt.show()
## bivariate plots
plt.figure(figsize=(20,6))
sns.lineplot(x=df['Age'],y=df['Annual_Premium'])

plt.figure(figsize=(10,10))
sns.heatmap(df.corr(), annot=True)
plt.show()