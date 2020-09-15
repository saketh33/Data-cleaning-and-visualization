import numpy as np
import plotly.express as px
import pandas as pd
u_cols = ['user_id', 'location', 'age']
users = pd.read_csv('C:\\Users\\saketh\\Documents\\BX-Users.csv', sep=';', names=u_cols, encoding='latin-1',skiprows=1)
print(users.head(10))
b_cols = ['isbn', 'book_title' ,'book_author','year_of_publication', 'publisher', 'img_s', 'img_m', 'img_l']
books = pd.read_csv('C:\\Users\\saketh\\Documents\\BX-Books.csv', sep=';', names=b_cols, encoding='latin-1', low_memory=False, skiprows=1)
r_cols = ['user_id', 'isbn', 'rating']
ratings = pd.read_csv('C:\\Users\\saketh\\Documents\\BX-Book-Ratings.csv', sep=';', names=r_cols, encoding='latin-1', low_memory=False, skiprows=1)
df = pd.merge(users, ratings, on='user_id')
df = pd.merge(df, books, on='isbn')
print(df.head (10))
ds = df['rating'].value_counts().reset_index()
ds.columns = ['value', 'count']
fig = px.bar(ds,x='value',y="count",orientation='v',title='Ranking distribution',width=800,height=600)
fig.show()
ds = df['year_of_publication'].value_counts().reset_index()
ds.columns = ['value', 'count']
ds['value'] = ds['value'] + 'year'
ds = ds.sort_values('count')
fig = px.bar(ds.tail(50), x='count', y="value", orientation='h', title='Top 50 years of publishing',width=900,height=900)
fig.show()
ds = df['book_author'].value_counts().reset_index()
ds.columns = ['author', 'count']
ds = ds.sort_values('count')
fig = px.bar(ds.tail(50), x='count', y="author", orientation='h', title='Authors with largest number of votes', width=900,height=900)
fig.show()
ds = df['book_title'].value_counts().reset_index()
ds.columns = ['book_title', 'count']
ds = ds.sort_values('count')
fig = px.bar(ds.tail(50), x='count', y='book_title', orientation='h', title='Books with largest number of votes', width=900,height=900)
fig.show()