import pytest

import numpy as np
import pandas as pd

from bdt.node import Node
from bdt.node import PandasNode


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


def test_pandas_run_function():
    node = PandasNode(
        'Node',
        lambda df: df['vals'] > 5,
        pd.DataFrame(
            np.matrix(
                range(10)
            ).T,
            columns=['vals']
        ),
        None,
        None
    )

    data = node.run_function()

    assert (
        len(data['true_values'].index) == 4
        and len(data['false_values'].index) == 6
    ) == True
