import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

# Dashアプリケーションの初期化（Bootstrapテーマの適用）
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 投資関数と貯蓄関数のパラメータ
I0 = 100  # 自発的投資
b = 0.25  # 金利の感応度
s = 0.2   # 限界貯蓄性向

# 所得(Y)と金利(r)の範囲を設定
Y = np.linspace(0, 500, 100)
r = np.linspace(0, 0.2, 100)

# 投資関数と貯蓄関数
I = I0 - b * r
S = s * Y

# IS曲線（投資 = 貯蓄）
IS = I0 - b * r

# Dashレイアウトの設定
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dcc.Graph(
            id='investment-function',
            figure={
                'data': [go.Scatter(x=I, y=r, mode='lines', name='investment function')],
                'layout': go.Layout(
                    title='投資関数', 
                    xaxis = dict(title='Investment (I)', autorange='reversed'), 
                    yaxis_title='Interest Rate (r)')
            }
        ), width=6),

        dbc.Col(dcc.Graph(
            id='is-curve',
            figure={
                'data': [go.Scatter(x=Y, y=IS, mode='lines', name='IS Curve')],
                'layout': go.Layout(title='IS曲線', xaxis_title='Income (Y)', yaxis_title='Interest Rate (r)')
            }
        ), width=6),
    ]),

    dbc.Row([
        dbc.Col(dcc.Graph(
            id='45-degree-line',
            figure={
                'data': [go.Scatter(x=Y, y=Y, mode='lines', name='45 degree line')],
                'layout': go.Layout(title='45度線', 
                                    xaxis = dict(title='Income (Y)', autorange='reversed'), 
                                    yaxis = dict(title='Interest Rate (r)', autorange='reversed')), 
            }
        ), width=6),
        dbc.Col(dcc.Graph(
            id='saving-function',
            figure={
                'data': [go.Scatter(x=S, y=Y, mode='lines', name='Saving Function')],
                'layout': go.Layout(title='貯蓄関数', 
                                    xaxis_title='Saving (S)', 
                                    yaxis = dict(title='Income (Y)', autorange='reversed'))
            }
        ), width=6),

    ])
], fluid=True)

# サーバーの起動
if __name__ == '__main__':
    app.run_server(debug=True)
