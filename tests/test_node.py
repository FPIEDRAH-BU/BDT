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
    )

    assert node.run_function() == True


def test_node_leaf():
    node = Node(
        'Test Node',
    )

    assert node.is_leaf() == True


def test_node_no_leaf():
    true_node = Node(
        'True Node'
    )

    false_node = Node(
        'False Node'
    )

    head_node = Node(
        'Head Node',
        lambda x: x < 25,
        true_child=true_node,
        false_child=false_node
    )

    assert head_node.is_leaf() == False
