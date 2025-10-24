def f1(x: int) -> int:
    i = 0
    while x > 1:
        # x //= 2
        # i += 1
        if i >= 4:
            i = 4
    return i


# def f2(x: int) -> int:
#     y = x * 2
#     res = 0
#     while res != 4:
#         y *= 2
#         res = f1(y)
#         if res == 4:
#             return 313
#     return res
