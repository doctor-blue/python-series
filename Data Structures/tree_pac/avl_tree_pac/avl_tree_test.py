from tree_pac.avl_tree_pac.avl_tree import AVLTree

tree = AVLTree()

for i in range(10, 24):
    tree.insert(i)

print(tree.to_string())

print(tree.root.height)
