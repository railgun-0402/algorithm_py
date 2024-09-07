import numpy as np
import matplotlib.pyplot as plt

# 30人分のデータ(身長(cm))
X = np.array([131, 132, 132, 133.5, 135, 142, 143.8, 144, 148, 149, 150, 152, 153, 157, 158, 158, 162, 164, 166, 169, 169.5, 170, 172, 173, 173, 176, 180, 184, 186, 190])

# Y：Xに対応する正解データ（体重 [kg]）
Y = np.array([31, 28, 35, 40, 31, 40, 42, 45, 50, 48, 56, 50, 51, 56, 65, 61, 66, 61.5, 69, 71, 63, 68, 80, 74, 76.5, 82, 68, 75, 92, 90])


# 標準化
def stand(x):
    m = x.mean() # 平均を計算
    s = x.std() # 標準偏差を計算

    # 標準化の式(x - データ平均を標準偏差で割る)
    x = (x - m) / s
    return x


# 正規化
def norm(x):
    min = x.min()
    max = x.max()

    # 正規化の式
    x = (x - min) / (max - min)

    return x


# X,Yをそれぞれ正規化
# X = norm(X)
# Y = norm(Y)

# X,Yをそれぞれ標準化
X = stand(X)
Y = stand(Y)

# 初期値を1として、パラメータ設定
a = 1
b = 1

# 繰り返し回数
iterations = 1000
# 学習率
alpha = 0.01
# データ数
m = X.shape[0]

# 目的関数の値を保存しておくためのリスト
cost = []

# 学習（指定した繰り返し回数だけパラメータを更新）
for iter in range(iterations):
    # 現在のパラメータで仮説を計算
    h = a * X + b

    # パラメータを更新
    a = a - (alpha / m) * ((h - Y) * X).sum()
    b = b - (alpha / m) * (h - Y).sum()

    # 更新後のパラメータで仮説と目的関数を計算
    h = a * X + b
    J = (1 / (2 * m)) * ((h - Y) ** 2).sum()

    # 学習によって目的関数の値がどう変化しているかを後で見れるよう、現在の目的関数の値をリストに保存
    cost.append(J)

# 学習した結果を表示
print("学習後のa: %f,"% a)
print("学習後のb: %f,"% b)
print("学習後の目的関数の値: %f,"% J)

# 目的関数の値の推移と仮説のグラフを並べて表示する
fig = plt.figure()
# 1つ目のグラフ
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(cost) # 目的関数の値を保存したリストをプロット
ax1.set_xlabel('Iteration')
ax1.set_ylabel('Cost')

# 2つ目のグラフ
ax2 = fig.add_subplot(1, 2, 2) # データと仮説を重ねてプロット
ax2.scatter(X, Y) # データをプロット
h = a*X+b # 最終的な仮説
ax2.plot(X, h, c='orange') # 仮説をプロット
ax2.legend((u'Data',u'Regression line')) # 凡例
ax2.set_xlabel('Height')
ax2.set_ylabel('Weight')

fig.tight_layout()
fig.show()
