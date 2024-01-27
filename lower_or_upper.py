# 入力文字の先頭の文字は大文字であり、それ以外の文字はすべて小文字である。
# 上記条件を満たすか判定するプログラム

def judge_upper_lower(str):
    for i in range(len(str)):
        if i == 0 and not str[i].isupper():
            return False

        if i != 0 and str[i].isupper():
            return False

    return True


input_line = input()
result = judge_upper_lower(input_line)

if result:
    print('Yes')
else:
    print('No')
