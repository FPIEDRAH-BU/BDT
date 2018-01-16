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


class PandasNode(Node):

    def __init__(self,
                 name,
                 filter_function=None,
                 data_frame=None,
                 true_child=None,
                 false_child=None):
        super(PandasNode, self).__init__(name,
                                         filter_function,
                                         true_child,
                                         false_child)

        self.data_frame = data_frame

    def run_function(self):
        if not self.function:
            return True

        df = self.data_frame
        df['condition_bdt'] = self.function(df)

        true_child_frame = df.loc[df['condition_bdt'] == True]
        false_child_frame = df.loc[df['condition_bdt'] == False]

        return {
            'true_values': true_child_frame,
            'false_values': false_child_frame
        }

    def set_data_frame(self,
                       data_frame):
        self.data_frame = data_frame
