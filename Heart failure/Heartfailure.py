import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('C:\\Users\\saketh\\Documents\\heart failure.csv')
print(data.head(5))
data.info()
print(data.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8))
sns.catplot(x='DEATH_EVENT', y='age', data=data)
sns.catplot(x='DEATH_EVENT', y='age', data=data, jitter=False)
sns.catplot(x='DEATH_EVENT', y='age', data=data, kind='swarm')
sns.catplot(x='DEATH_EVENT', y='age', hue='sex', data=data, kind='swarm')
sns.catplot(x='smoking', y='age', hue='sex', data=data, kind='swarm')
sns.catplot(x='DEATH_EVENT', y='platelets', hue='sex', data=data, kind='swarm')
sns.catplot(x='high_blood_pressure', y='platelets', hue='sex', data=data, kind='swarm')
sns.catplot(x='high_blood_pressure', y='platelets', hue='diabetes', data=data, kind='swarm')
sns.catplot(x='high_blood_pressure', y='platelets', hue='smoking', data=data, kind='swarm')

x = sns.catplot(x='anaemia', y='platelets', hue='smoking', data=data, kind='swarm')
y = sns.catplot(x='anaemia', y='platelets', hue='sex', data=data, kind='swarm')
z = sns.catplot(x='anaemia', y='platelets', hue='iabetes', data=data, kind='swarm')

plt.show()

import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})     # we use rcparams here beacuse if we dont give this we will get 
                                                        # an error sayin pyplot cant open more than 20 plots etc..

cat = ['anaemia', 'diabetes', 'smoking', 'sex']
con = ['creatinine_phosphokinase', 'age', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium']
for x in cat:
    for y in con:
        sns.catplot(x='DEATH_EVENT', y=y, hue=x, kind='box', data=data)
cat = ['anaemia', 'diabetes', 'smoking', 'sex']
con = ['creatinine_phosphokinase', 'age', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium']
for x in cat:
    for y in con:
        sns.catplot(x='DEATH_EVENT', y=y, hue=x, kind='boxen', data=data)
cat = ['anaemia', 'diabetes', 'smoking', 'sex']
con = ['creatinine_phosphokinase', 'age', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium']
for x in cat:
    for y in con:
        sns.catplot(x='DEATH_EVENT', y=y, hue=x, kind='violin', data=data)
cat = ['anaemia', 'diabetes', 'smoking', 'sex']
con = ['creatinine_phosphokinase', 'age', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium']
for x in cat:
    for y in con:
        sns.catplot(x='DEATH_EVENT', y=y, hue=x, kind='bar', data=data)
cat = ['anaemia', 'diabetes', 'smoking', 'sex']
con = ['creatinine_phosphokinase', 'age', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium']
for x in cat:
    for y in con:
        sns.catplot(x='DEATH_EVENT', y=y, hue=x, kind='point', data=data, markers=["^", "o"], linestyles=["-", "--"], )
plt.show()