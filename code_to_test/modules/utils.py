def find_element_index(l: list[int], x: int) -> int:
    if not l:
        return -1
    for i, e in enumerate(l):
        if e == x:
            return i
    return -1
