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


def test_iterator_true():
    true_node = Node(
        'True Node'
    )

    false_node = Node(
        'False Node'
    )

    head_node = Node(
        'Head Node',
        lambda var: var < 10,
        true_child=true_node,
        false_child=false_node
    )

    tree = BDT(
        head_node
    )

    tree.set_parameters({
        'var': 5
    })

    real_path = []
    path = ['Head Node',
            'True Node']
    for node in tree:
        real_path.append(node.name)

    assert path == real_path


def test_iterator_false():
    true_node = Node(
        'True Node'
    )

    false_node = Node(
        'False Node'
    )

    head_node = Node(
        'Head Node',
        lambda var: var < 10,
        true_child=true_node,
        false_child=false_node
    )

    tree = BDT(
        head_node
    )

    tree.set_parameters({
        'var': 100
    })

    real_path = []
    path = ['Head Node',
            'False Node']
    for node in tree:
        real_path.append(node.name)

    assert path == real_path


def test_iterator_error():
    true_node = Node(
        'True Node'
    )

    false_node = Node(
        'False Node'
    )

    head_node = Node(
        'Head Node',
        lambda var: var < 10,
        true_child=true_node,
        false_child=false_node
    )

    tree = BDT(
        head_node
    )

    with pytest.raises(UnboundLocalError):
        for node in tree:
            pass
