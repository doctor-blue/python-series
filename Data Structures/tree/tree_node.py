from queue import Queue


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_node(self, child):
        if isinstance(child, TreeNode):
            self.children.insert(0, child)
        else:
            print("child is not a TreeNode")

    def for_each_depth_first(self, visit):
        visit(self)
        for i in self.children:
            if isinstance(i, TreeNode):
                i.for_each_depth_first(visit)

    def for_each_lever_order(self, visit):
        visit(self)
        queue = Queue()
        for i in self.children:
            if isinstance(i, TreeNode):
                queue.put_nowait(i)

        node = queue.get_nowait()
        while node is not None:
            if isinstance(node, TreeNode):
                visit(node)
                for i in node.children:
                    if isinstance(i, TreeNode):
                        queue.put_nowait(i)
                if queue.empty():
                    node = None
                else:
                    node = queue.get_nowait()

    def search(self, value):
        if self.value == value:
            return self

        queue = Queue()
        for i in self.children:
            if isinstance(i, TreeNode):
                queue.put_nowait(i)

        node = queue.get_nowait()
        while node is not None:
            if isinstance(node, TreeNode):
                if node.value == value:
                    return node
                for i in node.children:
                    if isinstance(i, TreeNode):
                        queue.put_nowait(i)
                if queue.empty():
                    node = None
                else:
                    node = queue.get_nowait()
        return None
