class AVLTreeNode:
    def __init__(self, value):
        self.left_child = None
        self.right_child = None
        self.value = value
        self.height = 1

    @property
    def left_height(self):
        if self.left_child is None:
            return -1
        else:
            return self.left_child.height

    @property
    def right_height(self):
        if self.right_child is None:
            return -1
        else:
            return self.right_child.height

    @property
    def balance_factor(self):
        return self.left_height - self.right_height


class AVLTree:
    def __init__(self):
        self.root = None

    def to_string(self):
        if isinstance(self.root, AVLTreeNode):
            return self.diagram(self.root)
        else:
            return "empty"

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _get_height(self, root):
        if root is None:
            return 0
        else:
            return root.height

    def find(self, value):
        current_node = self.root
        while current_node is not None:
            if current_node.value is value:
                return current_node
            if current_node.value < value:
                current_node = current_node.right_child
            else:
                current_node = current_node.left_child
        return None

    def diagram(self, node, top="", root="", bottom=""):
        if node is not None:
            if node.left_child is None and node.right_child is None:
                return f"{root}{node.value}\n"
            else:
                return self.diagram(node.right_child, f"{top} ", f"{top}┌──", f"{top}│ ") \
                       + root + f"{node.value}\n" \
                       + self.diagram(node.left_child, f"{bottom}│ ", f"{bottom}└──", f"{bottom} ")
        return f"{root}null\n"

    def left_rotate(self, node):
        pivot = node.right_child
        node.right_child = pivot.left_child

        pivot.left_child = node

        node.height = max(self._get_height(node.left_child), self._get_height(node.right_child)) + 1
        pivot.height = max(self._get_height(pivot.left_child), self._get_height(pivot.right_child)) + 1
        return pivot

    def right_rotate(self, node):
        pivot = node.left_child
        node.left_child = pivot.right_child

        pivot.right_child = node

        node.height = max(self._get_height(node.left_child), self._get_height(node.right_child)) + 1
        pivot.height = max(self._get_height(pivot.left_child), self._get_height(pivot.right_child)) + 1
        return pivot

    def right_left_rotate(self, node):
        if isinstance(node, AVLTreeNode):
            if node.right_child is None:
                return node
            right_child = node.right_child
            node.right_child = self.right_rotate(right_child)
            return self.left_rotate(node)

    def left_right_rotate(self, node):
        if isinstance(node, AVLTreeNode):
            if node.left_child is None:
                return node
            left_child = node.left_child
            node.left_child = self.right_rotate(left_child)
            return self.left_rotate(node)

    def balanced(self, node):
        if node is not None:
            if node.balance_factor == 2:
                if node.left_child is not None:
                    if node.left_child.balance_factor == -1:
                        return self.left_right_rotate(node)
                    else:
                        return self.right_rotate(node)
                else:
                    return self.right_rotate(node)

            elif node.balance_factor == -2:
                if node.left_child is not None:
                    if node.left_child.balance_factor == 1:
                        return self.right_left_rotate(node)
                    else:
                        return self.left_rotate(node)
                else:
                    return self.left_rotate(node)
            else:
                return node

    def _insert(self, node, value):
        if isinstance(node, AVLTreeNode):
            if value < node.value:
                node.left_child = self._insert(node.left_child, value)
            else:
                node.right_child = self._insert(node.right_child, value)
            balanced_node = self.balanced(node)
            if balanced_node is not None:
                left_height = balanced_node.left_height
                right_height = balanced_node.right_height

                if right_height is None:
                    right_height = 0
                if left_height is None:
                    left_height = 0
                balanced_node.height = max(left_height, right_height) + 1
            else:
                balanced_node = AVLTreeNode(value)
            return balanced_node
        else:
            return AVLTreeNode(value)
