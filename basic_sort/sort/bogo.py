import random
from typing import List


def in_order(numbers: list) -> bool:
    # all 全ての判定がTrueであれば、()の中の結果もTrueになる
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))


# こんな書き方もある
def in_order_back(numbers: list) -> bool:
    for i in range(len(numbers)-1):
        # 順序通り並んでいない
        if numbers[i] > numbers[i + 1]:
            return False
    return True


def bogo_sort(numbers: List[int]) -> List[int]:
    while not in_order(numbers):
        # Falseの間はずっと繰り返す地獄の所業
        random.shuffle(numbers)
    return numbers


if __name__ == '__main__':
    lists = [random.randint(0, 1000) for _ in range(10)]
    # 時間がかかる(ランダムなので何とも言えないが、30s近くかかる時もある)
    print(bogo_sort(lists))

