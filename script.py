from typing import Any
import os
import traceback
from concurrent.futures import ThreadPoolExecutor
import subprocess
import time
import argparse


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
        "NONE",  # TODO!: comment this?
        "-v",
        "--algorithm",
        "DYNAMOSA",
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
    parser = argparse.ArgumentParser(description="A script to run and get results.")
    parser.add_argument("--branch", type=str, help="Branch", required=True, choices=["dev", "algo"])
    parser.add_argument("--module", type=str, help="Module", required=True, choices=["banking", "matrix"])
    parser.add_argument("--population", type=int, help="Population", required=True)
    parser.add_argument("--total-runs", type=int, help="Total runs", required=True)
    parser.add_argument("--batch", type=int, help="Batch", required=True)
    parser.add_argument("--max-search-time", type=int, help="Max search time", required=True)
    args = parser.parse_args()

    setup_environment()

    with ThreadPoolExecutor(max_workers=args.batch) as executor:
        executor.map(
            lambda i: run_pynguin(
                flags={
                    "population": str(args.population),
                    "module-name": args.module,
                    "maximum-search-time": str(args.max_search_time),
                },
                output_file=f"results/raw/{args.branch}_{args.module}_{i}",
            ),
            range(1, args.total_runs + 1),
        )


if __name__ == "__main__":
    main()
