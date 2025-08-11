import time

SLEEP_MUL = 0.1


def foo(x: int, y: int, z: int):
    if x < 0:
        time.sleep(0.001 * SLEEP_MUL)
        if y < 0:
            time.sleep(0.001 * SLEEP_MUL)
            if z < 0:
                time.sleep(0.001 * SLEEP_MUL)
            else:
                time.sleep(0.001 * SLEEP_MUL)
        else:
            time.sleep(0.001 * SLEEP_MUL)
            if z < 0:
                time.sleep(0.001 * SLEEP_MUL)
            else:
                time.sleep(0.001 * SLEEP_MUL)
    else:
        time.sleep(1 * SLEEP_MUL)
        if y < 0:
            time.sleep(1 * SLEEP_MUL)
            if z < 0:
                time.sleep(1 * SLEEP_MUL)
            else:
                time.sleep(1 * SLEEP_MUL)
        else:
            time.sleep(1 * SLEEP_MUL)
            if z < 0:
                time.sleep(1 * SLEEP_MUL)
            else:
                time.sleep(1 * SLEEP_MUL)
