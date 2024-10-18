def memory_func(x: int | None) -> int:
    if not isinstance(x, int) or x < 0:
        x = 20000
    l = [1 for _ in range(x)]
    return 1
