# 英小文字からなる文字列が与えられる
# 入力文字に最も多く出現する文字を求めるプログラム
# ただし該当する文字が複数ある場合は、そのうちアルファベット順で最も早いものを出力

import collections

input_line = input()

list_str = list(input_line)

dict = collections.Counter(list_str)

max_keys = [kv[0] for kv in dict.items() if kv[1] == max(dict.values())]
print(min(max_keys))
