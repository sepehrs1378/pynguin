#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2022 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#

# Automatically generated by Pynguin.
import pytest
import queue_example as module_0


def test_case_0():
    int_0 = 1256
    queue_0 = module_0.Queue(int_0)
    assert queue_0.max == 1256
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert len(queue_0.data) == 1256
    bool_0 = queue_0.full()
    assert bool_0 is False


def test_case_1():
    int_0 = -2944
    with pytest.raises(AssertionError):
        module_0.Queue(int_0)


def test_case_2():
    int_0 = -726
    int_1 = 2505
    queue_0 = module_0.Queue(int_1)
    assert queue_0.max == 2505
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert len(queue_0.data) == 2505
    bool_0 = queue_0.enqueue(int_0)
    assert bool_0 is True
    assert queue_0.tail == 1
    assert queue_0.size == 1
    with pytest.raises(AssertionError):
        module_0.Queue(int_0)


def test_case_3():
    int_0 = 2423
    queue_0 = module_0.Queue(int_0)
    assert queue_0.max == 2423
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert len(queue_0.data) == 2423
    none_type_0 = queue_0.dequeue()
    assert none_type_0 is None
    bool_0 = queue_0.full()
    assert bool_0 is False
    with pytest.raises(AssertionError):
        module_0.Queue(bool_0)


def test_case_4():
    int_0 = 1001
    queue_0 = module_0.Queue(int_0)
    assert queue_0.max == 1001
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert len(queue_0.data) == 1001
    int_1 = 649
    queue_1 = module_0.Queue(int_1)
    assert queue_1.max == 649
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    assert len(queue_1.data) == 649
    int_2 = 3263
    queue_2 = module_0.Queue(int_2)
    assert queue_2.max == 3263
    assert queue_2.head == 0
    assert queue_2.tail == 0
    assert queue_2.size == 0
    assert len(queue_2.data) == 3263
    bool_0 = queue_2.full()
    assert bool_0 is False
    int_3 = 2010
    bool_1 = queue_1.enqueue(int_3)
    assert bool_1 is True
    assert queue_1.tail == 1
    assert queue_1.size == 1
    int_4 = queue_1.dequeue()
    assert int_4 == 2010
    assert queue_1.head == 1
    assert queue_1.size == 0
    bool_2 = queue_0.full()
    assert bool_2 is False
    bool_3 = queue_1.full()
    assert bool_3 is False
    bool_4 = queue_1.enqueue(int_3)
    assert bool_4 is True
    assert queue_1.tail == 2
    assert queue_1.size == 1
    none_type_0 = queue_2.dequeue()
    assert none_type_0 is None


def test_case_5():
    int_0 = 1235
    queue_0 = module_0.Queue(int_0)
    assert queue_0.max == 1235
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert len(queue_0.data) == 1235
    queue_1 = module_0.Queue(int_0)
    assert queue_1.max == 1235
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    assert len(queue_1.data) == 1235
    bool_0 = queue_1.empty()
    assert bool_0 is False
    int_1 = 4904
    int_2 = 3504
    bool_1 = queue_0.empty()
    assert bool_1 is False
    queue_2 = module_0.Queue(int_2)
    assert queue_2.max == 3504
    assert queue_2.head == 0
    assert queue_2.tail == 0
    assert queue_2.size == 0
    assert len(queue_2.data) == 3504
    bool_2 = queue_2.enqueue(int_1)
    assert bool_2 is True
    assert queue_2.tail == 1
    assert queue_2.size == 1


def test_case_6():
    int_0 = 1187
    queue_0 = module_0.Queue(int_0)
    assert queue_0.max == 1187
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert len(queue_0.data) == 1187
    bool_0 = queue_0.empty()
    assert bool_0 is False
    bool_1 = queue_0.enqueue(int_0)
    assert bool_1 is True
    assert queue_0.tail == 1
    assert queue_0.size == 1
    queue_1 = module_0.Queue(bool_1)
    assert queue_1.max is True
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    assert len(queue_1.data) == 1
    bool_2 = queue_1.full()
    assert bool_2 is False
    int_1 = 1441
    bool_3 = queue_1.enqueue(int_1)
    assert bool_3 is True
    assert queue_1.size == 1
    bool_4 = queue_1.full()
    assert bool_4 is True
    int_2 = 1080
    queue_2 = module_0.Queue(int_2)
    assert queue_2.max == 1080
    assert queue_2.head == 0
    assert queue_2.tail == 0
    assert queue_2.size == 0
    assert len(queue_2.data) == 1080
    bool_5 = queue_1.full()
    assert bool_5 is True
    queue_3 = module_0.Queue(bool_5)
    assert queue_3.max is True
    assert queue_3.head == 0
    assert queue_3.tail == 0
    assert queue_3.size == 0
    assert len(queue_3.data) == 1
    bool_6 = queue_3.empty()
    assert bool_6 is False
    bool_7 = queue_1.enqueue(bool_2)
    assert bool_7 is False
    bool_8 = queue_1.empty()
    assert bool_8 is True
    none_type_0 = queue_2.dequeue()
    assert none_type_0 is None
    none_type_1 = queue_3.dequeue()
    assert none_type_1 is None
    queue_4 = module_0.Queue(bool_4)
    assert queue_4.max is True
    assert queue_4.head == 0
    assert queue_4.tail == 0
    assert queue_4.size == 0
    assert len(queue_4.data) == 1
    bool_9 = queue_4.empty()
    assert bool_9 is False
    int_3 = 2245
    bool_10 = queue_2.empty()
    assert bool_10 is False
    bool_11 = queue_3.empty()
    assert bool_11 is False
    bool_12 = queue_0.full()
    assert bool_12 is False
    queue_5 = module_0.Queue(int_3)
    assert queue_5.max == 2245
    assert queue_5.head == 0
    assert queue_5.tail == 0
    assert queue_5.size == 0
    assert len(queue_5.data) == 2245
    int_4 = queue_0.dequeue()
    assert int_4 == 1187
    assert queue_0.head == 1
    assert queue_0.size == 0
    bool_13 = queue_3.empty()
    assert bool_13 is False
    none_type_2 = queue_4.dequeue()
    assert none_type_2 is None
    int_5 = 481
    queue_6 = module_0.Queue(int_5)
    assert queue_6.max == 481
    assert queue_6.head == 0
    assert queue_6.tail == 0
    assert queue_6.size == 0
    assert len(queue_6.data) == 481
    none_type_3 = queue_3.dequeue()
    assert none_type_3 is None
    bool_14 = queue_6.enqueue(bool_4)
    assert bool_14 is True
    assert queue_6.tail == 1
    assert queue_6.size == 1
    none_type_4 = queue_3.dequeue()
    assert none_type_4 is None
    bool_15 = queue_0.empty()
    assert bool_15 is False
    bool_16 = queue_3.full()
    assert bool_16 is False


def test_case_7():
    int_0 = 1187
    queue_0 = module_0.Queue(int_0)
    assert queue_0.max == 1187
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert len(queue_0.data) == 1187
    bool_0 = queue_0.empty()
    assert bool_0 is False
    bool_1 = queue_0.enqueue(int_0)
    assert bool_1 is True
    assert queue_0.tail == 1
    assert queue_0.size == 1
    queue_1 = module_0.Queue(bool_1)
    assert queue_1.max is True
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    assert len(queue_1.data) == 1
    bool_2 = queue_1.full()
    assert bool_2 is False
    int_1 = 1441
    bool_3 = queue_1.enqueue(int_1)
    assert bool_3 is True
    assert queue_1.size == 1
    bool_4 = queue_1.full()
    assert bool_4 is True
    int_2 = 1080
    queue_2 = module_0.Queue(int_2)
    assert queue_2.max == 1080
    assert queue_2.head == 0
    assert queue_2.tail == 0
    assert queue_2.size == 0
    assert len(queue_2.data) == 1080
    int_3 = queue_1.dequeue()
    assert int_3 == 1441
    assert queue_1.size == 0
    int_4 = queue_0.dequeue()
    assert int_4 == 1187
    assert queue_0.head == 1
    assert queue_0.size == 0
    bool_5 = queue_2.full()
    assert bool_5 is False
    bool_6 = queue_1.enqueue(bool_0)
    assert bool_6 is True
    assert queue_1.size == 1
    int_5 = -30
    with pytest.raises(AssertionError):
        module_0.Queue(int_5)
