class Node(object):

    def __init__(self,
                 name,
                 bool_function=None,
                 true_child=None,
                 false_child=None):
        self.name = name
        self.function = bool_function
        self.true_child = true_child
        self.false_child = false_child

    def is_leaf(self):
        if not (self.true_child and self.false_child):
            return True

        return False

    def run_function(self,
                     **kwargs):
        if not self.function:
            return True

        return self.function(**kwargs)
