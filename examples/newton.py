"""
xn+1 = xn - xn / f'xn

root 2
fx = x**2 - 2
"""

# 適当な初期値の設定
x = 5.0

while True:

    # ニュートン法による新しいxを求める
    x2 = x - (x * x - 2) / (x * 2)

    # 計算後の値が誤差の範囲内になったら計算終了
    if abs(x2 - x) < 0.0001:
        break

    # 計算後の値をxとして計算を繰り返す
    x = x2

# 計算結果の表示
print(x)
