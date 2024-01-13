import numpy as np
import plotly.graph_objects as go
import plotly.io as pio

ys = {}
x_t = np.arange(-4, 0)
# グラフの作成
y = 1.5 * x_t + 10
ys["投資関数"] = y

#x_t = np.arange(-4, 0)
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
#print(ys)

# グラフの要素を作成
i = 0
plot = []
colors = ('red', 'blue', 'green', 'orange', 'black')
for num, (name, y) in enumerate(ys.items()):
    d = go.Scatter(
        x=x[i], y=y, name=name,
        marker_color=colors[num],  # プロット線の色
        showlegend=True  # 凡例を常に表示
    )
    i = i+1
    plot.append(d)

# 全プロット表示用のボタン作成
button_all = dict(
    label='all',  # ボタンのラベル
    method='update',  # ボタンの適用範囲はデータプロットとレイアウト
    args=[
        dict(visible=[True, True]),  # y1, y2の両方を表示
        dict(title='all plots'),  # グラフタイトル
    ]
)
# 全プロット表示用のボタンを先に入れる
buttons = [button_all]

# 該当するプロットの位置をTrueにすると表示になる
visibles = dict(
    #button1=[True, True, False, False, False],  # x+0, x+1
    #button2=[False, False, True, True, False],  # x+2, X+3
    #button3=[False, False, False, False, True]  # x+4
    process1=[True, True, False, False],
    process2=[True, True, True, False], 
    process3=[True, True, True, True]
)

# visiblesをforで回す
for label, visible in visibles.items():
    # ボタン作成
    button = dict(
        label=label,  # ボタンのラベル
        method='update',  # ボタンの適用範囲はデータプロットとレイアウト
        args=[
            dict(visible=visible),  # y1のみ表示
            dict(title=label),  # グラフタイトル
        ]
    )
    buttons.append(button)

# レイアウトに設置するためのupdatemenus作成
updatemenus = [
    dict(
        active=0,  # 初期グラフで見た目上、押されるボタン
        type='buttons',  # ボタンのタイプはボタンに
        direction='right',  # ボタンは右向きに配置
        x=0.5, y=1.01,  # ボタンの位置
        xanchor='center', yanchor='bottom',  # ボタンの位置の基準
        buttons=buttons,  # ここに設定したボタン情報を入れる
    )
]

# レイアウトの作成
layout = go.Layout(
    title='IS曲線',  # グラフタイトル
    font_size=20,  # グラフ全体のフォントサイズ
    hoverlabel_font_size=20,  # ホバーのフォントサイズ
    xaxis_range=(-10, 10),  # 横軸の表示範囲
    yaxis_range=(-12, 12),  # 縦軸の表示範囲
    legend=dict(x=1, xanchor='right'),  # 凡例のx位置をプロット領域の右端に
    updatemenus=updatemenus,  # ボタンを設置
)

# グラフの表示
fig = go.Figure(data=plot, layout=layout)