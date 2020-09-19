from tree_pac.binary_search_tree.binary_search_tree import BinarySearchTree

tree = BinarySearchTree(20)

nodes = [5, 21, 3, 31, 6, 8, 23]

for i in nodes:
    tree.insert(i)

print(tree.to_string())

print(tree.find(23))
tree.remove(5)

print(tree.to_string())
