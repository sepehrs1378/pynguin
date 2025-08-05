#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2024 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
"""Provides a random test generator, that creates random test suites."""

from __future__ import annotations

import logging

import pynguin.ga.testsuitechromosome as tsc
import pynguin.ga.testcasechromosome as tcc
import pynguin.ga.algorithms.archive as arch

from pynguin.ga.algorithms.generationalgorithm import GenerationAlgorithm


class RandomTestSuiteSearchAlgorithm(GenerationAlgorithm[arch.CoverageArchive, tsc.TestSuiteChromosome]):
    """Create random test suites."""

    _logger = logging.getLogger(__name__)

    def generate_tests(self) -> tsc.TestSuiteChromosome:  # noqa: D102
        self.before_search_start()
        solution = self._get_random_test_suite()
        self.before_first_search_iteration(solution)
        while self.resources_left() and solution.get_fitness() != 0.0:
            candidate = self._chromosome_factory.get_chromosome()
            if candidate.get_fitness() < solution.get_fitness():
                solution = candidate
            self.after_search_iteration(solution)
        self.after_search_finish()
        return solution

    def _get_random_test_suite(self) -> tsc.TestSuiteChromosome:
        return self._chromosome_factory.get_chromosome()


class RandomTestCaseSearchAlgorithm(GenerationAlgorithm[arch.CoverageArchive, tcc.TestCaseChromosome]):
    """Creates random test suites based on test-case chromosomes."""

    _logger = logging.getLogger(__name__)

    def generate_tests(self) -> tsc.TestSuiteChromosome:  # noqa: D102
        self.before_search_start()
        solution = self._get_random_test_case()
        self._archive.update([solution])
        test_suite = self.create_test_suite(self._archive.solutions)
        self.before_first_search_iteration(test_suite)
        while self.resources_left() and test_suite.get_fitness() != 0.0:
            candidate = self._chromosome_factory.get_chromosome()
            self._archive.update([candidate])
            test_suite = self.create_test_suite(self._archive.solutions)
            self.after_search_iteration(test_suite)
        self.after_search_finish()
        return self.create_test_suite(self._archive.solutions)

    def _get_random_test_case(self) -> tcc.TestCaseChromosome:
        return self._chromosome_factory.get_chromosome()
