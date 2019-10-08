# This file is part of Pynguin.
#
# Pynguin is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pynguin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pynguin.  If not, see <https://www.gnu.org/licenses/>.
"""Pynguin is an automated unit test generation framework for Python.

This module provides the main entry location for the program execution from the command
line.
"""
import argparse
import sys
from typing import List

import configargparse  # type: ignore

from pynguin import __version__
from pynguin.generator import Pynguin


def _create_argument_parser() -> argparse.ArgumentParser:
    parser = configargparse.ArgParser(
        default_config_files=["pynguin.conf"],
        description="""
        Pynguin is an automatic random unit test generation framework for Python.
        """,
    )

    parser.add_argument(
        "-c", "--config", is_config_file=True, help="Path to an optional config file."
    )

    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__
    )

    output = parser.add_mutually_exclusive_group()
    output.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        help="Make the output more verbose",
        action="store_true",
    )
    output.add_argument(
        "-q",
        "--quiet",
        dest="quiet",
        help="Omit all output from the shell.",
        action="store_true",
    )

    parser.add_argument(
        "--log-file", dest="log_file", help="Path to store the log file."
    )

    rtg_group = parser.add_argument_group(
        title="Random Test Generator",
        description="Parameters for the random test generation algorithm.",
    )
    rtg_group.add_argument(
        "--seed",
        type=int,
        dest="seed",
        help="A predefined seed value for the random number generator that is used.",
    )
    rtg_group.add_argument(
        "--project-path",
        dest="project_path",
        help="Path to the project the generator shall create tests for.",
    )
    rtg_group.add_argument(
        "--module_names",
        dest="module_names",
        action="append",
        help="A list of module names for that the generator shall create tests for.",
    )
    rtg_group.add_argument(
        "--measure-coverage",
        dest="measure_coverage",
        action="store_true",
        help="If set the achieved coverage will be measured during test generation.",
    )
    rtg_group.add_argument(
        "--coverage-filename",
        dest="coverage_filename",
        help="File name for storing the coverage information.",
    )
    rtg_group.add_argument(
        "--budget",
        dest="budget",
        type=int,
        help="Time budget (in seconds) that can be used for generating tests.",
    )
    rtg_group.add_argument(
        "--output-folder", dest="output_folder", help="Folder to store the output in."
    )

    return parser


def main(argv: List[str] = None) -> int:
    """Entry point of the Pynguin automatic unit test generation framework.

    :arg: argv List of command-line arguments
    :return: An integer representing the success of the program run.  0 means
    success, all non-zero exit codes indicate errors.
    """
    if argv is None:
        argv = sys.argv
    if len(argv) <= 1:
        argv.append("--help")
    parser = _create_argument_parser()
    generator = Pynguin(parser)
    return generator.run()


if __name__ == "__main__":
    sys.exit(main(sys.argv))