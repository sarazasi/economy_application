import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 2x2のサブプロットを作成
fig = make_subplots(rows=2, cols=2,
                    subplot_titles=(
                        "投資関数", "45度線", "貯蓄関数", "IS曲線"), 
                        vertical_spacing=0.2, 
                        horizontal_spacing=0.2)

# グラフ1
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]),
              row=1, col=1)
fig.update_yaxes(title_text="利子率 r", row=1, col=1)
fig.update_xaxes(title_text="投資 I", row=1, col=1)

# グラフ2
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[6, 7, 8]),
              row=1, col=2)
fig.update_yaxes(title_text="利子率 r", row=1, col=2)
fig.update_xaxes(title_text="国民所得 ", row=1, col=2)

# グラフ3
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[9, 10, 11]),
              row=2, col=1)
fig.update_yaxes(title_text="貯蓄 S", row=2, col=1)
fig.update_xaxes(title_text="投資 I", row=2, col=1)

# グラフ4
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[12, 13, 14]),
              row=2, col=2)
fig.update_yaxes(title_text="貯蓄 S", row=2, col=2)
fig.update_xaxes(title_text="国民所得", row=2, col=2)

# グラフ全体のレイアウトを更新
fig.update_layout(height=600, width=800, title_text="複数グラフのサンプル", 
                  margin=dict(l=50, r=50, t=50, b=50))
fig.show()
