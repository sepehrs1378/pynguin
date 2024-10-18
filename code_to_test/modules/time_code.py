import time

SLEEP = 1e-2


def get_user_info(username: str, id_: str) -> str:
    if username != "":
        return f"I am {username}"
    elif id_ != "":
        return f"No name but ID={id_}"
    else:
        # Simulate getting info from server
        time.sleep(SLEEP)
        return "Got info from server"
