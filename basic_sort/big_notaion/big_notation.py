def func_log(n):
    if n <= 1:
        return
    else:
        print(n)
        func_log(n/2)


# O(n)の例
def func_n(numbers):
    for num in numbers:
        print(num)


# O(n * log(n))の例
def n_log(n):
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <= 1:
        return
    n_log(n/2)


# O(n**2)
def func_2(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()

func_2([1,2,3,4,5])