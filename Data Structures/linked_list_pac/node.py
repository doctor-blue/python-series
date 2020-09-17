class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def to_string(self):
        if self.next_node is not None:
            return f"{self.value}-> {self.next_node.to_string()}"
        else:
            return f"{self.value}"
