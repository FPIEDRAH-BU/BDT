import pytest

from bdt.tree import BDT
from bdt.node import Node
from bdt.tools import tree_from_dict


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


def test_json_creation():
    tree_dict = {
        'head': 'Head Node',

        'variables': [
            'withd',
            'height'
        ],

        'nodes': [
            {
                'name': 'Head Node',
                'function': 'withd * height < 50',
                'true_child': 'True Node',
                'false_child': 'False Node'
            },
            {
                'name': 'True Node',
                'function': 'withd * height < 25',
                'true_child': 'True True Node',
                'false_child': 'True False Node'
            },
            {
                'name': 'False Node',
                'function': 'withd * height < 100',
                'true_child': 'False True Node',
                'false_child': 'False False Node'
            },
            {
                'name': 'True True Node',
                'function': 'None',
                'true_child': 'None',
                'false_child': 'None'
            },
            {
                'name': 'True False Node',
                'function': 'None',
                'true_child': 'None',
                'false_child': 'None',
            },
            {
                'name': 'False True Node',
                'function': 'None',
                'true_child': 'None',
                'false_child': 'None'
            },
            {
                'name': 'False False Node',
                'function': 'None',
                'true_child': 'None',
                'false_child': 'None'
            },
        ]
    }

    tree = tree_from_dict(tree_dict)

    assert len(tree) == len(tree_dict.get('nodes'))


def test_json_creation_bad_variables():
    tree_dict = {
        'head': 'Head Node',

        'variables': [
            'W',
            'H'
        ],

        'nodes': [
            {
                'name': 'Head Node',
                'function': 'withd * height < 50',
                'true_child': 'True Node',
                'false_child': 'False Node'
            },
            {
                'name': 'True Node',
                'function': 'withd * height < 25',
                'true_child': 'True True Node',
                'false_child': 'True False Node'
            },
            {
                'name': 'False Node',
                'function': 'withd * height < 100',
                'true_child': 'False True Node',
                'false_child': 'False False Node'
            },
            {
                'name': 'True True Node',
                'function': 'None',
                'true_child': 'None',
                'false_child': 'None'
            },
            {
                'name': 'True False Node',
                'function': 'None',
                'true_child': 'None',
                'false_child': 'None',
            },
            {
                'name': 'False True Node',
                'function': 'None',
                'true_child': 'None',
                'false_child': 'None'
            },
            {
                'name': 'False False Node',
                'function': 'None',
                'true_child': 'None',
                'false_child': 'None'
            },
        ]
    }

    with pytest.raises(ValueError):
        tree = tree_from_dict(tree_dict)
