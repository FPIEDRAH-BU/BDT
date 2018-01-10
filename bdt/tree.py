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



