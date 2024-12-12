import time


def is_none(x: int | None) -> int:
    if x is None:
        return -1
    elif x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return 3
