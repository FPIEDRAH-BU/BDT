import pytest

from bdt.node import Node


def test_bool_func_exec_true():
    node = Node(
        'Test Node',
        lambda h, w: h * w < 100,
    )

    assert node.run_function(h=1, w=10) == True


def test_bool_func_exec_false():
    node = Node(
        'Test Node',
        lambda h, w: h * w < 100,
    )

    assert node.run_function(h=10, w=10) == False


def test_bool_func_exec_none():
    node = Node(
        'Test Node',
        None
    )

    assert node.run_function() == True
