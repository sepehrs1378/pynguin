#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2021 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#
"""Provides classes for handling fitness functions for branch coverage."""
from __future__ import annotations

from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Dict, List

from ordered_set import OrderedSet

import pynguin.coverage.controlflowdistance as cfd
import pynguin.ga.computations as ff

if TYPE_CHECKING:
    import pynguin.ga.testcasechromosome as tcc
    import pynguin.testcase.execution.testcaseexecutor as tce
    from pynguin.testcase.execution.executionresult import ExecutionResult
    from pynguin.testcase.execution.executiontracer import ExecutionTracer, KnownData

class AbstractCoverageGoal:
    """Abstract base class for coverage goals."""

    def __init__(
        self,
        code_object_id: int,
    ):
        self._code_object_id = code_object_id

    @property
    def code_object_id(self) -> int:
        """Provides the code object id where the target resides.

        Returns:
            The id of the targeted code object.
        """
        return self._code_object_id

    @abstractmethod
    def is_covered(self, result: ExecutionResult) -> bool:
        """Determine if this coverage goal was covered.

        Args:
            result: The execution result to check.

        Returns:
            True, if this goal is covered in the execution result
        """


class StatementCoverageGoal(AbstractCoverageGoal):
    """Line to be covered by the search as goal."""

    def __init__(
        self,
        code_object_id: int,
        line_number: int,
        file_name: str,
    ):
        super().__init__(code_object_id)
        self._line_number = line_number
        self._file_name = file_name

    def is_covered(self, result: ExecutionResult) -> bool:
        return (
            result.execution_trace.file_trackers[self._file_name] and
            self._line_number in result.execution_trace.file_trackers[self._file_name].visited_statements
        )

class AbstractBranchCoverageGoal(AbstractCoverageGoal):
    """Abstract base class for branch coverage goals."""

    def __init__(
        self,
        code_object_id: int,
        is_branchless_code_object: bool = False,
        is_branch: bool = False,
    ):
        super().__init__(code_object_id)
        assert (
            is_branchless_code_object ^ is_branch
        ), "Must be either branch-less code object or branch."
        self._is_branchless_code_object = is_branchless_code_object
        self._is_branch = is_branch

    @abstractmethod
    def get_distance(
        self, result: ExecutionResult, tracer: ExecutionTracer
    ) -> cfd.ControlFlowDistance:
        """Computes the control-flow distance of an execution result.

        Args:
            result: The execution result
            tracer: The execution tracer

        Returns:
            The control-flow distance
        """

    @property
    def is_branchless_code_object(self) -> bool:
        """Does this target a branch-less code object?

        Returns:
            True, if it targets a branch-less code object.
        """
        return self._is_branchless_code_object

    @property
    def is_branch(self) -> bool:
        """Does this target a certain execution of a predicate?

        Returns:
            True, if it targets an execution of a predicate.
        """
        return self._is_branch


class BranchlessCodeObjectGoal(AbstractBranchCoverageGoal):
    """Entry into a code object without branches."""

    def __init__(self, code_object_id: int):
        super().__init__(code_object_id=code_object_id, is_branchless_code_object=True)

    def get_distance(
        self, result: ExecutionResult, tracer: ExecutionTracer
    ) -> cfd.ControlFlowDistance:
        return cfd.get_root_control_flow_distance(result, self._code_object_id, tracer)

    def is_covered(self, result: ExecutionResult) -> bool:
        return self._code_object_id in result.execution_trace.executed_code_objects

    def __str__(self) -> str:
        return f"Branch-less Code-Object {self._code_object_id}"

    def __repr__(self) -> str:
        return f"BranchlessCodeObjectGoal({self._code_object_id})"

    def __hash__(self) -> int:
        return 31 + self._code_object_id

    def __eq__(self, other: Any) -> bool:
        if self is other:
            return True
        if not isinstance(other, BranchlessCodeObjectGoal):
            return False
        return self._code_object_id == other._code_object_id


class BranchGoal(AbstractBranchCoverageGoal):
    """The true/false evaluation of a jump condition."""

    def __init__(self, code_object_id: int, predicate_id: int, value: bool):
        super().__init__(code_object_id=code_object_id, is_branch=True)
        self._predicate_id = predicate_id
        self._value = value

    def get_distance(
        self, result: ExecutionResult, tracer: ExecutionTracer
    ) -> cfd.ControlFlowDistance:
        return cfd.get_non_root_control_flow_distance(
            result, self._predicate_id, self._value, tracer
        )

    def is_covered(self, result: ExecutionResult) -> bool:
        trace = result.execution_trace
        distances = trace.true_distances if self._value else trace.false_distances
        return (
            self._predicate_id in trace.executed_predicates
            and distances[self._predicate_id] == 0.0
        )

    @property
    def predicate_id(self) -> int:
        """Provides the predicate id of the targeted predicate.

        Returns:
            The id of the targeted predicate.
        """
        return self._predicate_id

    @property
    def value(self) -> bool:
        """Provides whether we target the True or False branch of the predicate.

        Returns:
            The targeted branch value.
        """
        return self._value

    def __str__(self) -> str:
        return f"{self._value} branch of predicate {self._predicate_id}"

    def __repr__(self) -> str:
        return f"BranchGoal(predicate_id={self._predicate_id}, " f"value={self._value})"

    def __hash__(self) -> int:
        prime = 31
        result = 1
        result = prime * result + self._predicate_id
        result = prime * result + int(self._value)
        return result

    def __eq__(self, other: Any) -> bool:
        if self is other:
            return True
        if not isinstance(other, BranchGoal):
            return False
        return self.predicate_id == other.predicate_id and self._value == other.value


class BranchGoalPool:
    """Convenience class that creates and provides all branch coverage related goals."""

    def __init__(self, known_data: KnownData):
        self._branchless_code_object_goals = self._compute_branchless_code_object_goals(
            known_data
        )
        self._predicate_to_branch_goals = self._compute_branch_goals(known_data)

    @property
    def branchless_code_object_goals(self) -> List[BranchlessCodeObjectGoal]:
        """Provide the goals for branch-less code objects.

        Returns:
            The goals for branch-less code objects.
        """
        return self._branchless_code_object_goals

    @property
    def branch_goals(self) -> List[BranchGoal]:
        """Provide the goals for branches.

        Returns:
            The goals for branches.
        """
        return [
            goal for goals in self._predicate_to_branch_goals.values() for goal in goals
        ]

    @property
    def branch_coverage_goals(self) -> OrderedSet[AbstractBranchCoverageGoal]:
        """Provide all goals related to branch coverage.

        Returns:
            All goals related to branch coverage.
        """
        goals: OrderedSet[AbstractBranchCoverageGoal] = OrderedSet(self.branch_goals)
        goals.update(self.branchless_code_object_goals)
        return goals

    @staticmethod
    def _compute_branchless_code_object_goals(
        known_data: KnownData,
    ) -> List[BranchlessCodeObjectGoal]:
        return [
            BranchlessCodeObjectGoal(code_object_id)
            for code_object_id in known_data.branch_less_code_objects
        ]

    @staticmethod
    def _compute_branch_goals(known_data: KnownData) -> Dict[int, List[BranchGoal]]:
        goal_map: Dict[int, List[BranchGoal]] = {}
        for predicate_id, meta in known_data.existing_predicates.items():
            entry: List[BranchGoal] = []
            goal_map[predicate_id] = entry
            entry.append(BranchGoal(meta.code_object_id, predicate_id, True))
            entry.append(BranchGoal(meta.code_object_id, predicate_id, False))
        return goal_map


class BranchCoverageTestFitness(ff.TestCaseFitnessFunction):
    """A branch coverage fitness implementation for test cases."""

    def __init__(
        self, executor: tce.TestCaseExecutor, goal: AbstractBranchCoverageGoal
    ):
        super().__init__(executor, goal.code_object_id)
        self._goal = goal

    def compute_fitness(self, individual: tcc.TestCaseChromosome) -> float:
        result = self._run_test_case_chromosome(individual)

        distance = self._goal.get_distance(result, self._executor.tracer)
        return distance.get_resulting_branch_fitness()

    def compute_is_covered(self, individual: tcc.TestCaseChromosome) -> bool:
        result = self._run_test_case_chromosome(individual)
        return self._goal.is_covered(result)

    def is_maximisation_function(self) -> bool:
        return False

    def __str__(self) -> str:
        return f"BranchCoverageTestFitness for {self._goal}"

    def __repr__(self) -> str:
        return (
            f"BranchCoverageTestFitness(executor={self._executor}, "
            f"goal={self._goal})"
        )

    @property
    def goal(self) -> AbstractBranchCoverageGoal:
        """Provides the branch-coverage goal of this fitness function.

        Returns:
            The attached branch-coverage goal
        """
        return self._goal


class StatementCoverageTestFitness(ff.TestCaseFitnessFunction):
    """A branch coverage fitness implementation for test cases."""

    def __init__(
        self, executor: tce.TestCaseExecutor, file_name: str, code_object_id: int
    ):
        super().__init__(executor, code_object_id)
        self._file_name = file_name

    def compute_fitness(self, individual: tcc.TestCaseChromosome) -> float:
        result = self._run_test_case_chromosome(individual)
        coverage = ff.compute_statement_coverage(result.execution_trace)
        return coverage

    def compute_is_covered(self, individual) -> bool:
        result = self._run_test_case_chromosome(individual)
        coverage = ff.compute_statement_coverage(result.execution_trace)
        return coverage == 1

    def is_maximisation_function(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"StatementCoverageTestFitness for {self._file_name}"

    def __repr__(self) -> str:
        return (
            f"StatementCoverageTestFitness(executor={self._executor}, "
            f"file={self._file_name})"
        )


def create_branch_coverage_fitness_functions(
    executor: tce.TestCaseExecutor, branch_goal_pool: BranchGoalPool
) -> OrderedSet[BranchCoverageTestFitness]:
    """Create fitness functions for each branch coverage goal.

    Args:
        executor: The test case executor for the fitness functions to use.
        branch_goal_pool: The pool that holds all branch goals.

    Returns:
        All branch coverage related fitness functions.
    """
    return OrderedSet(
        [
            BranchCoverageTestFitness(executor, goal)
            for goal in branch_goal_pool.branch_coverage_goals
        ]
    )
