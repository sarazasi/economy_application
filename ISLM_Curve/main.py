#Dash Bootstrap　アプリレイアウトを構築するモジュール レイアウトを行, 列で定義する

from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

#グラフ情報をインポート
import IS

#external_stylesheetsにBootstrapのテーマを入れる
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container([
    dbc.Row([
        html.Div('IS LM曲線', className="text-primary text-center fs-3")
    ]),

    dbc.Row([
        #dbc.Col([
        #    dcc.Graph(figure={}, id='is_graph')
        #], width=6), 
        dbc.Col([
            dcc.Graph(
                id='lm_graph', figure=IS.fig )
        ], width=6)
    ])
], fluid=True)

#@callback(
#    Output(component_id='my-first-graph-final', component_property='figure'),
#    Input(component_id='radio-buttons-final', component_property='value')
#)
#def update_graph(col_chosen):
#   fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#   return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)