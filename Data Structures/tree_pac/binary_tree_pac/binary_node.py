class BinaryNode:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value

    # For binary search tree
    def min(self):
        if self.left_child is None:
            return self
        else:
            return self.left_child.min()

    def to_string(self):
        return self.diagram(self)

    def diagram(self, node, top="", root="", bottom=""):
        if node is not None:
            if node.left_child is None and node.right_child is None:
                return f"{root}{node.value}\n"
            else:
                return self.diagram(node.right_child, f"{top} ", f"{top}┌──", f"{top}│ ") \
                       + root + f"{node.value}\n" \
                       + self.diagram(node.left_child, f"{bottom}│ ", f"{bottom}└──", f"{bottom} ")
        return f"{root}null\n"

    def travel_in_order(self, visit):
        if self.left_child is not None:
            self.left_child.travel_in_order(visit)
        visit(self.value)
        if self.right_child is not None:
            self.right_child.travel_in_order(visit)

    def travel_pre_order(self, visit):
        if self.left_child is not None:
            self.left_child.travel_pre_order(visit)
        if self.right_child is not None:
            self.right_child.travel_pre_order(visit)
        visit(self.value)

    def travel_post_order(self, visit):
        visit(self.value)
        if self.left_child is not None:
            self.left_child.travel_post_order(visit)
        if self.right_child is not None:
            self.right_child.travel_post_order(visit)
