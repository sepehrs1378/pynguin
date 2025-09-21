# def f1(x: int):
#     a = x + 2
#     if x > 0:
#         return 1
#     else:
#         f2()
#         return -1


# def f2(x: int):
#     b = x - 2
#     if x > 0:
#         f1()
#         return 1
#     else:
#         return -1


def f1(x: int):
    x = x * 2
    x = x / 2
    if x > 0:
        return 1
    else:
        return -1


def f2(x: int):
    f1()
    x = x + 2
    if x > 3:
        return 1
    else:
        return -1
