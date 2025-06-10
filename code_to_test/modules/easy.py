from typing import Literal


def func(s: Literal["dog", "cat", "mouse"]) -> int:
    if s == "horse":
        return 1
    else:
        return 2
