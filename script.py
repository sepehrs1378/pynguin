from typing import Any
import os
import sys
import traceback

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
        "--seed",
        "1",
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
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")


def main():
    if len(sys.argv) == 1:
        algorithms = [
            "DYNAMOSA",
            "MOSA",
            "MIO",
            "RANDOM",
            "RANDOM_TEST_CASE_SEARCH",
            "RANDOM_TEST_SUITE_SEARCH",
            "WHOLE_SUITE",
        ]
    else:
        algorithms = sys.argv[1:]

    setup_environment()

    algorithms = [
        # "DYNAMOSA",
        # "MOSA",
        # "MIO",
        # "RANDOM",
        # "RANDOM_TEST_CASE_SEARCH",
        "RANDOM_TEST_SUITE_SEARCH",
        "WHOLE_SUITE",
    ]
    for algo in algorithms:
        if algo in {"RANDOM_TEST_SUITE_SEARCH", "WHOLE_SUITE"}:
            run_pynguin(
                flags={
                    "module-name": "banking",
                    "algorithm": algo,
                    "constraints": "EXECUTION_TIME",
                    "test-suite-execution-time-limit": "600_000_000",
                },
                output_file=f"results/raw/{algo}_time",
            )
            run_pynguin(
                flags={
                    "module-name": "matrix_calculus",
                    "algorithm": algo,
                    "constraints": "PEAK_MEMORY_USAGE",
                    "test-suite-memory-usage-limit": "9000",
                },
                output_file=f"results/raw/{algo}_mem",
            )
        else:
            run_pynguin(
                flags={
                    "module-name": "banking",
                    "algorithm": algo,
                    "constraints": "EXECUTION_TIME",
                    "test-case-execution-time-limit": "100_000_000",
                },
                output_file=f"results/raw/{algo}_time",
            )
            run_pynguin(
                flags={
                    "module-name": "matrix_calculus",
                    "algorithm": algo,
                    "constraints": "PEAK_MEMORY_USAGE",
                    "test-case-memory-usage-limit": "7500",
                },
                output_file=f"results/raw/{algo}_mem",
            )
        run_pynguin(
            flags={
                "module-name": "banking",
                "algorithm": algo,
            },
            output_file=f"results/raw/{algo}_no_time",
        )
        run_pynguin(
            flags={
                "module-name": "matrix_calculus",
                "algorithm": algo,
            },
            output_file=f"results/raw/{algo}_no_mem",
        )


if __name__ == "__main__":
    main()
