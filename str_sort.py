import sys
from itertools import combinations_with_replacement


def confirm(word1, word2):
    return sorted(word1) == sorted(word2)


count = int(input())

str_lists = []
result = 0
for i in range(count):
    str_lists.append(input())

tests = list(combinations_with_replacement(str_lists, 2))

for target in tests:

    renketu = target[0] + target[1]

    for k in range(count):
        if confirm(renketu, str_lists[k]):
            result += 1

print(result)
