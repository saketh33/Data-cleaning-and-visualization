import numpy as np # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
df=pd.read_csv('C:\\Users\\saketh\\Documents\\co2 emission.csv')
print(df.head(10),df.info(),df.describe())
sns.heatmap(df.corr(), annot = True, cmap = 'coolwarm', center = 0)
df.hist(figsize= (10, 3))
plt.show()
fig = px.scatter(df, x="Year", y="Entity",
                 color="Year",
                 size='Year',
                 hover_data=['Annual CO₂ emissions (tonnes )', 'Code'],
                 title = "CO2 Emissions")
fig.show()
fig3 = go.Figure(data=go.Scatter(
    y = df['Entity'],
    mode='markers',
    marker=dict(
        size=16,
        color=df['Year'], #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    )
))
fig3.show()