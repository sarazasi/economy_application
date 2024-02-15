import numpy as np
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Output, Input
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Dashアプリケーションの初期化
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#IS曲線
ys = {}
x_t = np.arange(-6, -1)
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

xl_2 = np.arange(0, 8)
y = -0.75*xl_2
ym["L1対国民所得"] = y

xl_3 = np.arange(-4, 1)
y = -xl_3 - 4
ym["実質貨幣供給"] = y

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
#シフト用にそれぞれを格納
plot_is = plot[:4]
plot_lm = plot[4:8]

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
    xaxis=dict(range=[-10, 10], title=dict(text='L1',font=dict(size=17,color='black'))),
    yaxis=dict(range=[-12, 12], title=dict(text='L2',font=dict(size=17,color='black'))), 
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
#シフトするグラフのレイアウト
layout_sift_is = go.Layout(
    title='IS曲線のシフトの様子',
    xaxis=dict(range=[-10, 10]),
    yaxis=dict(range=[-12, 12]), 
    width = 800, 
    height = 800, 
)
layout_sift_lm = go.Layout(
    title='LM曲線のシフトの様子',
    xaxis=dict(range=[-10, 10]),
    yaxis=dict(range=[-12, 12]), 
    width = 800, 
    height = 800, 
)

# 2x2のサブプロットを作成
fig_is = make_subplots(rows=2, cols=2,
                    subplot_titles=(
                        "投資関数", "IS曲線", "45度線", "貯蓄関数"), 
                        vertical_spacing=0.2, 
                        horizontal_spacing=0.2)

# 投資関数
fig_is.add_trace(plot[0],
              row=1, col=1)
fig_is.update_yaxes(title_text="投資", range = [-12, 12], row=1, col=1)
fig_is.update_xaxes(title_text="利子率"  , range = [-10, 10], row=1, col=1)

# 貯蓄関数
fig_is.add_trace(plot[1],
              row=2, col=2)
fig_is.update_yaxes(title_text="国民所得", range=[-12, 12], row=2, col=2)
fig_is.update_xaxes(title_text="貯蓄", range=[-10, 10], row=2, col=2)

# 45度線
fig_is.add_trace(plot[2],
              row=2, col=1)
fig_is.update_yaxes(title_text="投資", range=[-12, 12], row=2, col=1)
fig_is.update_xaxes(title_text="貯蓄", range=[-10, 10], row=2, col=1)

# IS曲線
fig_is.add_trace(plot[3],
              row=1, col=2)
fig_is.update_yaxes(title_text="国民所得",   range = [-12, 12], row=1, col=2)
fig_is.update_xaxes(title_text="利子率", range = [-10, 10], row=1, col=2)

# グラフ全体のレイアウトを更新
fig_is.update_layout(height=600, width=800, title_text="IS曲線の導出に使う4つのグラフ", 
                  margin=dict(l=50, r=50, t=100, b=50))

# 2x2のサブプロットを作成
fig_lm = make_subplots(rows=2, cols=2,
                    subplot_titles=(
                        "利子率対L2", "LM曲線", "実質貨幣供給", "L1対国民所得",   ), 
                        vertical_spacing=0.2, 
                        horizontal_spacing=0.2)

# 利子率対L2
fig_lm.add_trace(plot[4],
              row=1, col=1)
fig_lm.update_yaxes(title_text="L2", range=[-12, 12], row=1, col=1)
fig_lm.update_xaxes(title_text="利子率", range=[-10, 10], row=1, col=1)

# L1対国民所得
fig_lm.add_trace(plot[5],
              row=2, col=2)
fig_lm.update_yaxes(title_text="国民所得", range=[-12, 12], row=2, col=2)
fig_lm.update_xaxes(title_text="L1", range=[-10, 10], row=2, col=2)

# 実質貨幣供給
fig_lm.add_trace(plot[6],
              row=2, col=1)
fig_lm.update_yaxes(title_text="L2", range=[-12, 12],row=2, col=1)
fig_lm.update_xaxes(title_text="L1", range=[-10, 10],row=2, col=1)


# LM曲線
fig_lm.add_trace(plot[7],
              row=1, col=2)
fig_lm.update_yaxes(title_text="国民所得", range=[-12, 12], row=1, col=2)
fig_lm.update_xaxes(title_text="利子率", range=[-10, 10], row=1, col=2)

# グラフ全体のレイアウトを更新
fig_lm.update_layout(height=600, width=800, title_text="LM曲線の導出に使う4つのグラフ", 
                  margin=dict(l=50, r=50, t=100, b=50))

#プルダウンボタンを作成
button_is = [
    {'label' : '投資関数', 'value' : '投資関数'}, 
    {'label' : '45度線', 'value' : '45度線'}, 
    {'label' : '貯蓄関数', 'value' : '貯蓄関数'}, 
    {'label' : 'IS曲線', 'value' : 'IS曲線'}
]
button_lm = [
    {'label' : '利子率対L2', 'value' : '利子率対L2'}, 
    {'label' : '実質貨幣供給', 'value' : '実質貨幣供給'}, 
    {'label' : 'L1対国民所得', 'value' : 'L1対国民所得'}, 
    {'label' : 'LM曲線', 'value' : 'LM曲線'}
]
#本文のテキスト
four_is = [
    open(r'.\Text\four_glaf_is1.txt', 'r', encoding="utf-8_sig"), 
    open(r'.\Text\four_glaf_is2.txt', 'r', encoding="utf-8_sig"), 
    open(r'.\Text\four_glaf_is3.txt', 'r', encoding="utf-8_sig"), 
    open(r'.\Text\four_glaf_is4.txt', 'r', encoding="utf-8_sig"), 
]
f_is = [
    four_is[1].read(), 
    four_is[2].read(), 
    four_is[3].read(), 
    four_is[0].read()
]
four_lm = [
    open(r'.\Text\four_glaf_lm1.txt', 'r', encoding="utf-8_sig"), 
    open(r'.\Text\four_glaf_lm2.txt', 'r', encoding="utf-8_sig"), 
    open(r'.\Text\four_glaf_lm3.txt', 'r', encoding="utf-8_sig"),
    open(r'.\Text\four_glaf_lm4.txt', 'r', encoding="utf-8_sig"), 
]
f_lm = [
    four_lm[0].read(), 
    four_lm[1].read(), 
    four_lm[3].read(), 
    four_lm[2].read()
]
glaf_islm = open(r'.\Text\glaf-islm.txt', 'r', encoding="utf-8_sig")
sift = [
    open(r'.\Text\sift-is.txt', 'r', encoding="utf-8_sig"), 
    open(r'.\Text\sift-lm.txt', 'r', encoding="utf-8_sig")
]
path_is = [
    open(r'.\Text\glaf_is1.txt', 'r', encoding="utf-8_sig"),
    open(r'.\Text\glaf_is2.txt', 'r', encoding="utf-8_sig"),
    open(r'.\Text\glaf_is3.txt', 'r', encoding="utf-8_sig"),
]
temp1 = path_is[0].read()
temp2 = path_is[2].read()
glaf_is = [
    temp1, 
    temp1, 
    path_is[1].read(), 
    temp2, 
    temp2
]
path_lm = [
    open(r'.\Text\glaf_lm1.txt', 'r', encoding="utf-8_sig"),  
    open(r'.\Text\glaf_lm2.txt', 'r', encoding="utf-8_sig"), 
    open(r'.\Text\glaf_lm3.txt', 'r', encoding="utf-8_sig"), 
]
temp1 = path_lm[0].read() 
temp2 = path_lm[2].read()
glaf_lm = [
    temp1,
    temp1,
    path_lm[1].read(), 
    temp2,
    temp2
]

#各グラフの説明
text_is = {
    button_is[0]['label'] : f_is[0], 
    button_is[1]['label'] : f_is[1], 
    button_is[2]['label'] : f_is[2], 
    button_is[3]['label'] : f_is[3]
}
text_lm = {
    button_lm[0]['label'] : f_lm[0], 
    button_lm[1]['label'] : f_lm[1], 
    button_lm[2]['label'] : f_lm[2], 
    button_lm[3]['label'] : f_lm[3]
}

#dbcのレイアウト
app.layout = dbc.Container([
    # 各グラフの描画（IS曲線）
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id = 'all-graph_is', 
                figure = fig_is
            ), 
        ]), 
        dbc.Col([
            html.Div(
                dcc.Dropdown(
                    id='dropdown_is',
                    options=button_is,
                    multi=False,
                    placeholder='IS曲線',
                    value = 'IS曲線'
                ),
                style={'width': '15%', 'display': 'inline-block','margin-right': 10, 'margin-top':10}
            ), 
            html.Div(id = 'is_ex', className="article")
        ])
    ]), 
    # 各グラフの描画（LM曲線）
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id = 'all-graph_lm', 
                figure = fig_lm
            ), 
        ]), 
        dbc.Col([
            html.Div(
                dcc.Dropdown(
                    id='dropdown_lm',
                    options=button_lm,
                    multi=False,
                    placeholder='LM曲線',
                    value = 'LM曲線'
                ),
                style={'width': '15%', 'display': 'inline-block','margin-right': 10, 'margin-top':10}
            ),  
            html.Div(id='lm_ex', className='article'),
        ])   
    ]), 

    # IS曲線のnextボタン
    dbc.Row([
        dbc.Col([
            dbc.Button("Next", id = 'btn1', n_clicks=4)
        ]), 
    ],),
    # IS曲線のグラフと説明文
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id = 'graph_is', 
                figure = {}
            )
        ], ), 
        dbc.Col([
            html.Div(id='text1', className='article')
        ])
    ]), 

    # LM曲線のnextボタン
    dbc.Row([
        dbc.Col([
            dbc.Button("Next", id = 'btn2', n_clicks=4)
        ]), 
    ],),
    # LM曲線のグラフと説明文
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id = 'graph_lm', 
                figure = {}
            )
        ], ), 
        dbc.Col([
            html.Div(id='text2', className="article")
        ])
    ]), 

    # ISLM曲線のグラフと説明文
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id = 'graph_islm', 
                figure = go.Figure(data=[plot[3], plot[7]], layout = layout_islm),
            ),
        ], ), 
        dbc.Col([
            html.Div(glaf_islm.read(), id='text3', className="article")
        ])
    ]), 

    #IS曲線のスライド
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='is-graph', figure={}, ), 
        ], width=6), 
        dbc.Col([
            html.Div('政府支出', className = 'head1'),
            dcc.Slider(
             id='graph-slider_i',
             min=-2,
             max=5,
             value=0,
             step=1,
             marks={i: str(i) for i in range(-2, 6)}, 
             updatemode='drag'
            ),

            html.Div('税金', className = 'head2'), 
            dcc.Slider(
             id='graph-slider_s',
             min=-3,
             max=3,
             value=0,
             step=1,
             marks={i: str(i) for i in range(-5, 4)}, 
             updatemode='drag'
            ),
            html.Div(sift[0].read(), className='article')
        ]),
    ]),

    #LM曲線のスライド
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='lm-graph', figure={}, ), 
        ], width=6), 
        dbc.Col([
            html.Div('実質貨幣供給', className = 'head1'),
            dcc.Slider(
             id='graph-slider_lm',
             min=-3,
             max=5,
             value=0,
             step=1,
             marks={i: str(i) for i in range(-3, 6)}, 
             updatemode='drag'
            ),
            html.Div(sift[1].read(), className = 'article')
        ]),
    ]),
], fluid = True)
#ボタンでグラフを変化
@app.callback(
    Output(component_id='graph_is', component_property='figure'),
    Output(component_id='text1', component_property='children'),
    Output(component_id='graph_lm', component_property='figure'),
    Output(component_id='text2', component_property='children'),
    Input(component_id="btn1", component_property='n_clicks'), 
    Input(component_id="btn2", component_property='n_clicks'), 
)
def on_button_click(n1, n2):
    n1 = n1%5
    n2 = n2%5 + 4
    if n1 == 4:
        data_i = plot[:4]
    else:
        data_i = plot[n1]

    if n2 == 8:
        data_l = plot[4:8]
    else:
        data_l = plot[n2]
    
    return go.Figure(data = data_i, layout = layout_IS), glaf_is[n1%5], go.Figure(data = data_l, layout = layout_LM), glaf_lm[(n2+1)%5]

# スライダーでISグラフをシフト
@callback(
    Output(component_id='is-graph', component_property='figure'),
    Input(component_id='graph-slider_i', component_property='value'), 
    Input(component_id = 'graph-slider_s', component_property = 'value')
)
def on_slider_i(slider_value_i, slider_value_s):
    #投資関数
    x = np.arange(-6 - slider_value_i, -1 - slider_value_i, 0.1)
    y = 1.5 * (x + slider_value_i) + 10
    #投資関数を編集
    plot_is[0] = go.Scatter(
        x=x, y=y, name='投資関数',
        marker_color='red',
        showlegend=True,
        mode = 'lines'
    )
    #貯蓄関数
    x = np.arange(0, 5)
    y = -2*x + (2 - slider_value_s)
    #貯蓄関数を編集
    plot_is[1] = go.Scatter(
        x=x, y=y, name='貯蓄関数',
        marker_color='blue',
        showlegend=True,
        mode = 'lines'
    )
    slider_value = slider_value_i + slider_value_s
    x = np.arange(1 + slider_value, 5 + slider_value, 0.1)
    y = -3 * (x - slider_value) + 13
    #IS曲線を編集
    plot_is[3] = go.Scatter(
        x=x, y=y, name='IS曲線',
        marker_color='orange',
        showlegend=True,
        mode = 'lines'
    )
    return go.Figure(data = plot_is, layout=layout_sift_is)

# スライダーでLMグラフをシフト
@callback(
    Output(component_id='lm-graph', component_property='figure'),
    Input(component_id='graph-slider_lm', component_property='value'),
)
def on_slider_i(slider_value):
    x = np.arange(-4 - slider_value, 1)
    y = -(x + slider_value) - 4
    #実質貨幣供給のグラフを編集
    plot_lm[2] = go.Scatter(
        x=x, y=y, name='実質貨幣供給',
        marker_color='#ff69b4',
        showlegend=True,
        mode = 'lines'
    )
    x = np.arange(1 + slider_value, 8 + slider_value, 0.1)
    y = 0.7669392271704*(x - slider_value) + 2
    #LM曲線を編集
    plot_lm[3] = go.Scatter(
        x=x, y=y, name='IS曲線',
        marker_color='#800080',
        showlegend=True,
        mode = 'lines'
    )
    return go.Figure(data = plot_lm, layout=layout_sift_lm)

#ドロップダウン処理
@callback(
    Output(component_id='is_ex', component_property='children'),
    Output(component_id='lm_ex', component_property='children'),
    Input(component_id='dropdown_is', component_property='value'),
    Input(component_id='dropdown_lm', component_property='value')
)
def on_dropdown(dd_is, dd_lm):
   return text_is[dd_is], text_lm[dd_lm]

if __name__ == '__main__':
    app.run(debug=True)