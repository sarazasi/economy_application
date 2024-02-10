#Dash Bootstrap　アプリレイアウトを構築するモジュール レイアウトを行, 列で定義する

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np

#グラフ情報をインポート
# import IS

#external_stylesheetsにBootstrapのテーマを入れる
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container([
    dbc.Row([
        html.Div('IS LM曲線', className="text-primary text-center fs-3")
    ]),

    dbc.Row([
        dcc.Graph(id='is-graph', figure={}, ), 
    ]),
    dbc.Row([
       dcc.Slider(
        id='graph-slider',
        min=-10,
        max=10,
        value=0,
        step=1,
        marks={i: str(i) for i in range(-10, 11)}, 
        updatemode='drag'
        ) 
    ]),

], fluid=True)


@callback(
   Output(component_id='is-graph', component_property='figure'),
   Input(component_id='graph-slider', component_property='value')
)
def update_graph(slider_value):
    layout = go.Layout(
            font_size=20,  # グラフ全体のフォントサイズ
            hoverlabel_font_size=20,  # ホバーのフォントサイズ
        		xaxis_range=(-10, 10),  # 横軸の表示範囲
        		yaxis_range=(-12, 12),  # 縦軸の表示範囲
        		legend=dict(x=1, xanchor='right'),  # 凡例のx位置をプロット領域の右端に
   	)
    # グラフのデータを更新
    x = np.arange(0+slider_value, 3+slider_value, 0.1)
    y = 3 * (x-slider_value)  # スライダーの値で波を移動
    data = [go.Scatter(x=x, y=y, mode='lines')]
    
    return go.Figure(data=data, layout=layout)

#Run the app
if __name__ == '__main__':
  app.run(debug=True)