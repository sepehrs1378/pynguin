#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2023 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#
from unittest import mock
from unittest.mock import MagicMock

import mutpy.controller

import pynguin.assertion.mutation_analysis.controller as c


class FooController(c.MutationController):
    pass


class FooMutController(mutpy.controller.MutationController):
    pass


def test_mutate_module():
    adapter = FooController()
    controller = FooMutController(
        MagicMock(), MagicMock(), MagicMock(), MagicMock(), MagicMock()
    )
    with mock.patch.object(controller, "mutate_module", MagicMock()) as mutated:
        with mock.patch.object(
            adapter, "_build_mutation_controller", mutated
        ) as mock_obj:
            adapter.target_loader = MagicMock()
            adapter.mutate_module()
            mock_obj.assert_called_once()
            mutated.assert_called_once()
