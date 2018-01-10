class BDT(object):

    def __init__(self,
                 head=None):
        self.head = head
        self.current_node = head
        self.params_set = False
