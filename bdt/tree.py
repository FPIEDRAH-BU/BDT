def count(tree):
    if tree.head == None:
        return 0

    true_child = tree.head.true_child
    false_child = tree.head.false_child

    return 1 + count(BDT(true_child)) + count(BDT(false_child))


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

        if node.run_function(**self.params):
            self.current_node = node.true_child
        else:
            self.current_node = node.false_child

        return node

    def set_parameters(self,
                       params):
        self.params_set = True
        self.params = params
