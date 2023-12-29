import sys

# 1行目から2つの整数を受け取る
n, m = map(int, sys.stdin.readline().split())

# 2行目から複数の整数をリストとして受け取る
numbers = list(map(int, sys.stdin.readline().split()))

print(n)
print(m)
print(numbers)

result = 0

# n問出題で、m点以下の配点を足し合わせる
for i in range(n):
    if numbers[i] <= m:
        result += numbers[i]

print(result)
