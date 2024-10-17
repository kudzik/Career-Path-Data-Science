import plotly_express as px

df = px.data.iris()
df.head()
px.scatter(data_frame=df, x="sepal_length", y="sepal_width", color="species")
