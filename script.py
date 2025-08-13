from typing import Any
import os
import traceback
from concurrent.futures import ThreadPoolExecutor

import subprocess
import time


def setup_environment():
    """Set up environment variables and activate virtualenv"""
    env_vars = {"PYTHONPATH": "/home/sepehr/university/MS/thesis/pynguin/src/", "PYNGUIN_DANGER_AWARE": "1"}
    os.environ.update(env_vars)

    # Activate virtualenv
    activate_script = "venv/bin/activate"
    if not os.path.exists(activate_script):
        raise FileNotFoundError(f"Virtualenv activation script not found at {activate_script}")

    # Source the activation script in a shell
    activate_cmd = f"source {activate_script} && python3 -c 'import sys; print(sys.executable)'"
    result = subprocess.run(
        activate_cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    if result.returncode != 0:
        raise RuntimeError(f"Failed to activate virtualenv: {result.stderr}")

    print(f"Virtualenv activated. Python path: {result.stdout.strip()}")


def run_pynguin(flags: dict[str, Any], output_file: str) -> None:
    command = [
        "python3",
        "src/pynguin/__main__.py",
        "--project-path",
        "code_to_test/modules",
        "--output-path",
        "code_to_test/output",
        "--assertion-generation",
        "NONE",
        "-v",
        "--algorithm",
        "DYNAMOSA",
        # "--seed",
        # "1",
        "--maximum-search-time",
        "300",
    ]
    for flag, val in flags.items():
        command.extend([f"--{flag}", val])

    start_time = time.time()
    try:
        with open(output_file, "w") as f:
            result = subprocess.run(command, stdout=f, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Command failed with error:\n{result.stderr}")
        else:
            print(f"Pynguin completed successfully. Output saved to {output_file}")
    except Exception as e:
        traceback.print_exc()
    print(f"Execution time: {time.time() - start_time:.2f} seconds")


def main():
    if len(sys.argv) == 1:
        raise ValueError("Input `dev` or `algo`.")
    else:
        branch = "dev" if sys.argv[1] == "dev" else "algo"

    setup_environment()

    TOTAL_RUNS = 15
    BATCH = 5
    with ThreadPoolExecutor(max_workers=BATCH) as executor:
        executor.map(
            lambda i: run_pynguin(
                flags={
                    "population": "10",
                    "module-name": "banking",
                },
                output_file=f"results/raw/{branch}_banking_{i}",
            ),
            range(1, TOTAL_RUNS + 1),
        )


if __name__ == "__main__":
    main()
