import time

BASE_SLEEP = 1
FAST_PATH_SLEEP = BASE_SLEEP * 1e-3
SLOW_PATH_SLEEP = BASE_SLEEP * 3e-1


def foo(x: int, y: int, z: int):
    if x < 0:
        time.sleep(FAST_PATH_SLEEP)
        if y < 0:
            time.sleep(FAST_PATH_SLEEP)
            if z < 0:
                time.sleep(FAST_PATH_SLEEP)
            else:
                time.sleep(FAST_PATH_SLEEP)
        else:
            time.sleep(FAST_PATH_SLEEP)
            if z < 0:
                time.sleep(FAST_PATH_SLEEP)
            else:
                time.sleep(FAST_PATH_SLEEP)
    else:
        time.sleep(SLOW_PATH_SLEEP)
        if y < 0:
            time.sleep(SLOW_PATH_SLEEP)
            if z < 0:
                time.sleep(SLOW_PATH_SLEEP)
            else:
                time.sleep(SLOW_PATH_SLEEP)
        else:
            time.sleep(SLOW_PATH_SLEEP)
            if z < 0:
                time.sleep(SLOW_PATH_SLEEP)
            else:
                time.sleep(SLOW_PATH_SLEEP)
