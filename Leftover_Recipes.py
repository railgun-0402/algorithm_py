import sys

# 材料個数
N = int(input())
# 各材料の質量
Q = list(map(int, input().split()))
# 材料Aの質量
A = list(map(int, input().split()))
# 材料Bの質量
B = list(map(int, input().split()))

# 最大公約数
max_div = 0

# 最大公約数の要素数
iso = 0

for i in range(len(Q) + 1):
    if i == 0:
        weight1, weight2 = map(int, sys.stdin.readline().split())
    else:
        cook1, cook2 = map(int, sys.stdin.readline().split())
        A.append(cook1)
        B.append(cook2)


def max(count, max_count):
    if max_count < count:
        return count
    else:
        return max_count


for i in range(len(A)):
    div = Q[i] / A[i]
    max_div = max(div, max_div)
    div2 = Q[i] / B[i]
    max_div, iso = max(div2, max_div)


print(max_div)
