# 2つの整数の和を返す関数
def add(a: int, b: int) -> int:
    return a + b


# 2つの整数の差を返す関数
def sub(a: int, b: int) -> int:
    return a - b


if __name__ == '__main__':
    y = add(a=3, b=4)

    print(y)

    y2 = sub(a=4, b=3)

    print(y2)
