import sys

n, m = map(int, sys.stdin.readline().split())
inputs = []

for i in range(n):
    if i == 0:
        continue

    s = int(input())
    inputs.append(s)

# 縦軸はm
# 横はmから2行目以降の値を引いていく
x_width = m
for i in range(len(inputs)):
    x_width += (m - inputs[i])

result = m * x_width
print(result)
