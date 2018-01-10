import pytest

from bdt.tree import BDT
from bdt.node import Node


def test_len_null():
    tree = BDT(
        None
    )

    assert len(tree) == 0


def test_len():
    true_node = Node(
        'True Node'
    )

    false_node = Node(
        'False Node'
    )

    head_node = Node(
        'Head Node',
        lambda x: x < 10,
        true_child=true_node,
        false_child=false_node
    )

    tree = BDT(
        head_node
    )

    assert len(tree) == 3
