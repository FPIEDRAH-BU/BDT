import inspect


def count(tree):
    if tree.head == None:
        return 0

    true_child = tree.head.true_child
    false_child = tree.head.false_child

    return 1 + count(BDT(true_child)) + count(BDT(false_child))


def get_nodes(tree):
    if tree.head == None:
        return [None]

    if tree.head.is_leaf():
        return [tree.head]

    true_child = tree.head.true_child
    false_child = tree.head.false_child

    return get_nodes(BDT(true_child)) + get_nodes(BDT(false_child))


class BDT(object):

    def __init__(self,
                 head=None):
        self.head = head
        self.current_node = head
        self.params_set = False

    def __len__(self):
        return count(self)

    def __iter__(self):
        if not self.params_set:
            raise UnboundLocalError(""" You should set up parameters first
                                        use the set_parameters function. """)

        return self

    def next(self):
        node = self.current_node

        if not node:
            raise StopIteration

        if node.function is None:
            self.current_node = None
            return node

        arguments = inspect.getargspec(node.function).args
        filtered_params = {k: v for k, v in self.params.items() if k in arguments}

        if node.run_function(**filtered_params):
            self.current_node = node.true_child
        else:
            self.current_node = node.false_child

        return node

    def set_parameters(self,
                       params):
        self.params_set = True
        self.params = params


class PandasBDT(object):

    def __init__(self,
                 head=None):
        self.head = head

    def __len__(self):
        return count(self)

    def set_parameters(self,
                       data_frame):
        self.head.data_frame = data_frame
        self.data_frame = data_frame

    def get_leaves(self):
        print get_nodes(self)
        return [node for node in get_nodes(self) if node.is_leaf()]

    def execute(self,
                  node=None):
        if not node:
            node = self.head

        nodes = [node]
        while nodes:
            new_nodes = []
            for node in nodes:
                if not node.is_leaf():
                    data = node.run_function()

                    node.false_child.set_data_frame(
                        data['false_values']
                    )

                    node.true_child.set_data_frame(
                        data['true_values']
                    )

                    new_nodes.extend([
                        node.false_child,
                        node.true_child
                    ])

            nodes = new_nodes
