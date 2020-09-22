import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
data= pd.read_csv('C:\\Users\\saketh\\Documents\\vgsales.csv')
print(data.head())
data.dropna(how="any", inplace=True)
print(data.info())
data.Year = data.Year.astype(int)
fig = px.scatter(data, x="Year", y="NA_Sales",
                 color="NA_Sales",
                 size='NA_Sales',
                 hover_data=['Rank','Name', 'Platform', 'Genre', 'Publisher'],
                 title = "Sales in North America")
fig.show()
import plotly.graph_objects as go
fig1 = go.Figure()
fig1.add_trace(go.Scatter(
    x=data['Year'], y=np.sin(data['EU_Sales']),
    name='sin',
    mode='markers',
    marker_color='rgba(152, 0, 0, .8)'))
fig1.update_traces(mode='markers', marker_line_width=2, marker_size=10)
fig1.update_layout(title='Sales in Europe',
                  yaxis_zeroline=False, xaxis_zeroline=False)
fig1.show()
fig2 = go.Figure(data=go.Scatter(x=data['Year'],
                                y=data['JP_Sales'],
                                mode='markers',
                                marker_color=data['Rank'],
                                text=data['Name'])) # hover text goes here

fig2.update_layout(title='Sales in Japan')
fig2.show()
fig3 = go.Figure(data=go.Scatter(
    y = data['Other_Sales'],
    mode='markers',
    marker=dict(
        size=16,
        color=data['Rank'], #set color equal to a variable
        colorscale='Viridis', # one of plotly colorscales
        showscale=True
    )
))
fig3.update_layout(title='Sales in Other countries')
fig3.show()
fig4 = go.Figure(data=go.Scatter(
    x=data['Year'],
    y=data['Global_Sales'],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3])
))
fig4.update_layout(title="Sales in GLobal")
fig4.show()