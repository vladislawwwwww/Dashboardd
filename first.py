from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('lr.csv', delimiter=';')

fig = px.bar(df, x="Возраст", y="Диагноз", color="Пол", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Лабораторная работа'),

    html.Div(children='''
        
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)