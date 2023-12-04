from dash import dcc, html, Input, Output, dash_table
import dash
import plotly.express as px
import pandas as pd

# Загрузка данных
df = pd.read_csv('https://raw.githubusercontent.com/vladislawwwwww/csv/main/lr.csv', delimiter=';')

# Инициализация Dash-приложения
app = dash.Dash(__name__)

# Определение структуры дашборда с использованием стилей
app.layout = html.Div([
    html.H1("Анализ медицинских данных: Лабораторная работа", style={'color': '#333', 'textAlign': 'center'}),
    html.P(
        "Дашборд предоставляет визуальный анализ медицинских данных. Изучайте зависимости с помощью графиков и таблицы."),
    # График 1 (точечный)
    dcc.Graph(id='graph1', style={'margin-bottom': '20px'}),
    dcc.Dropdown(
        id='graph1-x-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='Дата',
        style={'width': '50%', 'margin-bottom': '20px'}
    ),

    # График 2 (столбчатый)
    dcc.Graph(id='graph2', style={'margin-bottom': '20px'}),
    dcc.Dropdown(
        id='graph2-x-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='Возраст',
        style={'width': '50%', 'margin-bottom': '20px'}
    ),

    # График 3 (круговой)
    dcc.Graph(id='graph3', style={'margin-bottom': '20px'}),
    dcc.Dropdown(
        id='graph3-x-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='Пол',
        style={'width': '50%', 'margin-bottom': '20px'}
    ),

    # График 4 (линейный)
    dcc.Graph(id='graph4', style={'margin-bottom': '20px'}),
    dcc.Dropdown(
        id='graph4-x-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='Дата',
        style={'width': '50%', 'margin-bottom': '20px'}
    ),
    dcc.RadioItems(
        id='graph4-scale',
        options=[
            {'label': 'Линейная', 'value': 'linear'},
            {'label': 'Логарифмическая', 'value': 'log'},
        ],
        value='linear',
        labelStyle={'display': 'block', 'margin-bottom': '20px'}
    ),

    # График 5 (ящичковый)
    dcc.Graph(id='graph5', style={'margin-bottom': '20px'}),
    dcc.Dropdown(
        id='graph5-x-dropdown',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='Холестерин',
        style={'width': '50%', 'margin-bottom': '20px'}
    ),

    # Таблица данных
    dash_table.DataTable(
        id='data-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'height': '300px', 'overflowY': 'auto', 'margin-top': '20px'},
        sort_action='native',
        sort_mode='multi',
        filter_action='native',
        page_action='native',
        page_size=10
    ),
], style={'font-family': 'Arial, sans-serif', 'max-width': '1000px', 'margin': 'auto'})


# Callback функция для обновления графиков
@app.callback(
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),
    Output('graph3', 'figure'),
    Output('graph4', 'figure'),
    Output('graph5', 'figure'),
    Input('graph1-x-dropdown', 'value'),
    Input('graph2-x-dropdown', 'value'),
    Input('graph3-x-dropdown', 'value'),
    Input('graph4-x-dropdown', 'value'),
    Input('graph5-x-dropdown', 'value'),
    Input('graph4-scale', 'value')
)
def update_graphs(x_col1, x_col2, x_col3, x_col4, x_col5, scale):
    try:
        # Обновление графиков
        fig1 = px.scatter(df, x=x_col1, y='Давление', title='Точечный график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )

        fig2 = px.bar(df, x=x_col2, y='Пульс', title='Столбчатый график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )

        fig3 = px.pie(df, names=x_col3, title='Круговой график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )

        fig4 = px.line(df, x=x_col4, y='Температура', title='Линейный график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
            yaxis_type=scale
        )

        fig5 = px.box(df, x=x_col5, y='Диагноз', title='Ящичковый график').update_layout(
            margin=dict(l=20, r=20, t=40, b=20),
            font=dict(family="Arial, sans-serif", size=12, color="Black"),
            paper_bgcolor="White",
        )
        return fig1, fig2, fig3, fig4, fig5
    except Exception as e:
        print(str(e))
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)