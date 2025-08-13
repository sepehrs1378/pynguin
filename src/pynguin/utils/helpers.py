from typing import Any
import json


def print_dict(d: dict[str, Any]) -> None:
    print(json.dumps(d))
