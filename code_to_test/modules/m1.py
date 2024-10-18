def func(x: int, y: int) -> int:
    if x > 0:
        if y > 10:
            return 0
        elif 0 < y <= 10:
            return 1
        else:
            return 2
    elif -20 < x <= 0:
        return 3
    else:
        return 4
