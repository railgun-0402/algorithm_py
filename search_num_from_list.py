# 出力値(リストの長さ)
lines = int(input())

lists = []
for i in range(lines):
    height_strs = input().split()
    heights = [int(s) for s in height_strs]
    lists.append(heights)


def find_larger_neighbors(matrix):
    result = []

    # 列・行の長さ
    rows, cols = len(matrix), len(matrix[0])

    # 二重配列の要素を全て確認
    for i in range(rows):
        for j in range(cols):
            current_value = matrix[i][j]
            neighbors = []

            # 上下左右の値を配列で取得する(neighbors)が、index range errorを避ける必要がある
            # 例えば一番上の場合、その上の要素を取り出そうとするとindex errorとなるので場合分けする
            if i > 0:
                neighbors.append(matrix[i - 1][j])  # 最上行ではない場合
            if i < rows - 1:
                neighbors.append(matrix[i + 1][j])  # 最下行ではない場合
            if j > 0:
                neighbors.append(matrix[i][j - 1])  # 最左列ではない場合
            if j < cols - 1:
                neighbors.append(matrix[i][j + 1])  # 最右列ではない場合

            # 値が上下左右全ての値よりも大きければ、trueを返し結果出力リストに加える(同等値は除く)
            if all(current_value > neighbor for neighbor in neighbors):
                result.append(current_value)

    return result


result = find_larger_neighbors(lists)
res = sorted(result, reverse=True)

# 結果の出力
for a in res:
    print(a)
