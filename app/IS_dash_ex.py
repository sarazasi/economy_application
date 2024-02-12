import numpy as np
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
import plotly.graph_objs as go

# Dashアプリケーションの初期化
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#IS曲線
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

x_i = [x_t, x_s, x_f, x_is]

#LM曲線
ym = {}
xl_1 = np.arange(-6,1)
y = xl_1 + 6
ym["利子率対L2"] = y

xl_2 = np.arange(-4, 1)
y = -xl_2 - 4
ym["実質貨幣供給"] = y

xl_3 = np.arange(0, 8)
y = -0.75*xl_3
ym["L1対国民所得"] = y

xl_4 = np.arange(1, 8)
y = 0.7669392271704 * xl_4 + 2
ym["LM曲線"] = y

x_l = [xl_1, xl_2, xl_3, xl_4]

# グラフ情報をplotに全て格納
plot = []
colors = ('red', 'blue', 'green', 'orange', '#deb887', '#66cdaa', '#ff69b4', '#800080')
for i, (name, y), in enumerate(ys.items()):
    d = go.Scatter(
        x=x_i[i], y=y, name=name,
        marker_color=colors[i],
        showlegend=True,
        mode = 'lines'
    )
    plot.append(d)
for i, (name, y) in enumerate(ym.items()):
    d = go.Scatter(
        x=x_l[i], y=y, name=name,
        marker_color=colors[i+4],
        showlegend=True, 
        mode = 'lines',
    )
    plot.append(d)

# IS曲線のレイアウト
layout_IS = go.Layout(
    title='IS曲線',
    xaxis=dict(range=[-10, 10]),
    yaxis=dict(range=[-12, 12]), 
    width = 800, 
    height = 800,
)
# LM曲線のレイアウト
layout_LM = go.Layout(
    title='LM曲線',
    xaxis=dict(range=[-10, 10]),
    yaxis=dict(range=[-12, 12]), 
    width = 800, 
    height = 800, 
)
# ISLM曲線のレイアウト
layout_islm = go.Layout(
    title='IS-LM曲線',
    xaxis=dict(range=[-10, 10]),
    yaxis=dict(range=[-12, 12]), 
    width = 800, 
    height = 800, 
)

#dbcのレイアウト
app.layout = dbc.Container([
    # IS曲線のnextボタン
    dbc.Row([
        dbc.Col([
            dbc.Button("Next", id = 'btn1', n_clicks=0)
        ]), 
    ],),
    # IS曲線のグラフと説明文
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id = 'graph_is', 
                figure = {}
            )
        ]), 
        dbc.Col([
            html.Div(id='text1', className='my-class')
        ])
    ]), 
    # LM曲線のnextボタン
    dbc.Row([
        dbc.Col([
            dbc.Button("Next", id = 'btn2', n_clicks=0)
        ]), 
    ],),

    # LM曲線のグラフと説明文
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id = 'graph_lm', 
                figure = {}
            )
        ]), 
        dbc.Col([
            html.Div(id='text2', className="text-primary text-center fs-3")
        ])
    ]), 
    # ISLM曲線のグラフと説明文
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id = 'graph_islm', 
                figure = go.Figure(data=[plot[3], plot[7]], layout = layout_islm),
            ),
        ]), 
        dbc.Col([
            html.Div(id='text3', className="text-primary text-center fs-3")
        ])
    ])
], fluid = True)
@app.callback(
    Output(component_id='graph_is', component_property='figure'),
    Output(component_id='text1', component_property='children'),
    Output(component_id='graph_lm', component_property='figure'),
    Output(component_id='text2', component_property='children'),
    Input(component_id="btn1", component_property='n_clicks'), 
    Input(component_id="btn2", component_property='n_clicks')
)
def on_button_click(n1, n2):
    n1 = n1%5
    text1 = f'{n1%5 + 1}個目'

    n2 = n2%4 + 4
    text2 = f'{n2%4 + 1}個目'

    if n1 == 4:
        data_i = plot[:4]
    else:
        data_i = plot[n1]

    if n2 == 7:
        data_l = plot[4:8]
    else:
        data_l = plot[n2]

    return go.Figure(data = data_i, layout = layout_IS), text1, go.Figure(data = data_l, layout = layout_LM), text2

if __name__ == '__main__':
    app.run(debug=True)