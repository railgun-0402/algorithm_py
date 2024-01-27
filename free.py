#
# def generate_combinations(n):
#     result = []
#
#     for x in range(n + 1):
#         for y in range(n + 1):
#             for z in range(n + 1):
#                 if x + y + z <= n:
#                     result.append((x, y, z))
#
#     return result
#
#
# # Nの入力
# N = int(input("非負整数 N を入力してください: "))
#
# # 結果の生成
# combinations = generate_combinations(N)
#
# # 結果の出力
# for combo in combinations:
#     print(*combo)

def create_dragon(N):
    # Initialize the grid with zeros
    grid = [[0]*N for _ in range(N)]

    # Set the initial position to the center of the grid
    x, y = N//2-1, N//2-1

    # Set the initial part number
    part = 1

    # Directions for moving in the grid (right, down, left, up)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Start filling the grid
    for step in range(1, N):
        for _ in range(2):
            dx, dy = directions[step % 4]
            for _ in range(step):
                if part <= N*N-1:
                    grid[x][y] = part
                    part += 1
                x, y = x + dx, y + dy
    grid[x][y] = part

    # Print the grid
    for row in grid:
        print(*row)


N = int(input())
create_dragon(N)
