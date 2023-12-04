from dash import Dash, dcc, html, Input, Output
import dash
import plotly.express as px
import pandas as pd


df = pd.read_csv('lr.csv', delimiter=';')


app = dash.Dash(__name__)


app.layout = html.Div([
    html.H1("Графики с Dash и Plotly"),

    # График 1 (точечный)
    dcc.Graph(id='graph1'),

    # График 2 (столбчатый)
    dcc.Graph(id='graph2'),

    # График 3 (круговой)
    dcc.Graph(id='graph3'),

    # График 4 (линейный)
    dcc.Graph(id='graph4'),

    # График 5 (ящичковый)
    dcc.Graph(id='graph5'),
])


@app.callback(
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),
    Output('graph3', 'figure'),
    Output('graph4', 'figure'),
    Output('graph5', 'figure'),
    Input('graph1', 'relayoutData'),
    Input('graph2', 'relayoutData'),
    Input('graph3', 'relayoutData'),
    Input('graph4', 'relayoutData'),
    Input('graph5', 'relayoutData'),
)
def update_graphs(relayout_data1, relayout_data2, relayout_data3, relayout_data4, relayout_data5):
    try:

        fig1 = px.scatter(df, x='Температура', y='Давление', title='Точечный график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )

        fig2 = px.bar(df, x='Температура', y='Пульс', title='Столбчатый график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )

        fig3 = px.pie(df, names='Пол', title='Круговой график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )

        fig4 = px.line(df, x='Дата', y='Температура', title='Линейный график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )

        fig5 = px.box(df, x='Холестерин', y='Диагноз', title='Ящичковый график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )

        return fig1, fig2, fig3, fig4, fig5
    except Exception as e:
        print(str(e))
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)