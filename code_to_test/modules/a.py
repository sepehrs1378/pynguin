def order(x: int, y: int, z: int) -> str:
    if x > y > z:
        return "x > y > z"
    elif y > x > z:
        return "y > x > z"
    elif x > z > y:
        return "x > z > y"
    elif y > z > x:
        return "y > z > x"
    elif z > x > y:
        return "z > x > y"
    else:
        return "z > y > x"
