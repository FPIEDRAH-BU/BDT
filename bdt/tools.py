import re
import json

from boolexp import Expression

from bdt.node import Node
from bdt.tree import BDT


def validate_bool_string(bool_string, variables):
    if bool_string == 'None':
        return

    delimiters = [
        '; ',
        ', ',
        'and',
        'or',
        '==',
        '<=',
        '>=',
        '<',
        '>',
        '\*',
        '-',
        '\+',
        '\d+\.\d+',
        '\d+',
        ' '
    ]

    deli_regex = '|'.join(delimiters)
    print deli_regex
    bool_vars = list(set(re.split(deli_regex, bool_string)))
    bool_vars.remove('')

    print bool_vars
    print variables

    if not set(bool_vars) == set(variables):
        raise ValueError(""" The boolean function is malformed,
                             you should only have variables defined
                             in the variables array in the JSON""")


def bool_str_to_funct(bool_string):
    return lambda **kwargs: Expression(bool_string).evaluate(kwargs)


def tree_from_dict(tree_dict):
    nodes = dict()

    variables = tree_dict.get('variables')
    for node in tree_dict.get('nodes'):
        if not node.get('function') == 'None':
            validate_bool_string(node.get('function'),
                                 variables)

            nodes[node.get('name')] = Node(
                node.get('name'),
                bool_str_to_funct(node.get('function'))
            )
        else:
            nodes[node.get('name')] = Node(
                node.get('name'),
                None
            )

    for node in tree_dict.get('nodes'):
        father_node = nodes[node.get('name')]
        true_child_node = nodes.get(node.get('true_child'))
        false_child_node = nodes.get(node.get('false_child'))

        father_node.true_child = true_child_node
        father_node.false_child = false_child_node

    return BDT(
        nodes[tree_dict.get('head')]
    )


def tree_from_json(json):
    tree_dict = json.loads(json)
    return tree_from_dict(tree_dict)
