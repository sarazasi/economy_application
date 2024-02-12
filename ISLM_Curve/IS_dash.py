import numpy as np
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objs as go

# Dashアプリケーションの初期化
app = dash.Dash(__name__)

ys = {}
x_t = np.arange(-4, 0)
y = 1.5 * x_t + 10
ys["投資関数"] = y

x_s = np.arange(0, 5)
y = -2 * x_s + 2
ys["貯蓄関数"] = y

x_f = np.arange(-5, 1)
y = x_f
ys["45度線"] = y

x_is = np.arange(1, 5)
y = -3 * x_is + 13
ys["IS曲線"] = y

x = [x_t, x_s, x_f, x_is]

plot = []
colors = ('red', 'blue', 'green', 'orange', 'black')
for i, (name, y) in enumerate(ys.items()):
    d = go.Scatter(
        x=x[i], y=y, name=name,
        marker_color=colors[i],
        showlegend=True, 
        text=f'{i}個目'
    )
    plot.append(d)

buttons = [
    {
        'label': 'All',
        'method': 'update',
        'args': [{'visible': [True] * len(plot)}],
    }
]

visibles = [
    [True if i == j else False for i in range(len(plot))] for j in range(len(plot))
]

for i, visible in enumerate(visibles):
    button = {
        'label': f'Process {i+1}',
        'method': 'update',
        'args': [{'visible': visible}],
    }
    buttons.append(button)

updatemenus = [{
    'buttons': buttons,
    'direction': 'down',
    'showactive': True,
}]

layout = go.Layout(
    title='IS曲線',
    updatemenus=updatemenus,
    xaxis=dict(range=[-10, 10]),
    yaxis=dict(range=[-12, 12])
)

fig = go.Figure(data=plot, layout=layout)

# Dashレイアウトの設定
# app.layout = html.Div([
#     dcc.Graph(id='graph', figure=fig)
# ])

#dbcのレイアウト
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dcc.Graph(
            id = 'graph', 
            figure = fig,
        ), width = 6), 
    ],),
    dbc.Row([
        dbc.Col(

        )
    ])
], fluid = True)

if __name__ == '__main__':
    app.run_server(debug=True)