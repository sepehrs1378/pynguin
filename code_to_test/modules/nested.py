def foo(a: int, b: int, c: int) -> int:
    x = 2
    y = 3
    z = 4
    if a + b < c:
        y = 3
        if c < 0:
            x = x * 3
        elif c > 1:
            if b > 3:
                x = 3
            else:
                x = x * y
        else:
            x = 4
    else:
        z = x + y
