import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from string import ascii_letters
df = pd.read_csv("C:\\Users\\saketh\\Documents\\survey rkl.csv", sep=';')
corr = df.corr()
print(corr)
corr.to_csv('correlations.csv',index=False)
corr.to_csv('C:\\Users\\saketh\\Documents\\correlations.csv',index=False)
sns.set(style="white")
f, ax = plt.subplots(figsize=(21, 19))
# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)
# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.show()