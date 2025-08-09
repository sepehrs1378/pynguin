def check_triangle(a: int, b: int, c: int) -> bool:
    if a >= b + c:
        return False
    elif b >= a + c:
        return False
    elif c >= a + b:
        return False
    else:
        return True
    
    if 1 == 2:
        return False
