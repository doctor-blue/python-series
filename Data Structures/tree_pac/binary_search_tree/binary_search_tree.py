from tree_pac.binary_tree_pac.binary_node import BinaryNode


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.root = BinaryNode(value)

    def to_string(self):
        if isinstance(self.root, BinaryNode):
            return self.root.to_string()
        else:
            return "empty"

    def insert(self, value):
        self.root = self.insert_node(self.root, value)

    def insert_node(self, node, value):
        if node is None:
            return BinaryNode(value)

        if node.value > value:
            node.left_child = self.insert_node(node.left_child, value)
        else:
            node.right_child = self.insert_node(node.right_child, value)
        return node

    def find(self, value):
        current_node = self.root
        while current_node is not None:
            if current_node.value is value:
                return True
            if current_node.value < value:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return False

    def remove(self, value):
        self.root = self.remove_node(self.root, value)

    def remove_node(self, node, value):
        if node is not None:

            if node.value is value:

                if node.left_child is None and node.right_child is None:
                    return None
                if node.left_child is None:
                    return node.right_child
                if node.right_child is None:
                    return node.left_child

                if node.right_child.min() is not None:
                    node.value = node.right_child.min().value

                node.right_child = self.remove_node(node.right_child, node.value)
            elif node.value > value:
                node.left_child = self.remove_node(node.left_child, value)
            else:
                node.right_child = self.remove_node(node.right_child, value)
            return node
        else:
            return None
