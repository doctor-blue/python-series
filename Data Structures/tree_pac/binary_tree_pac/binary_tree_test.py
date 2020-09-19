from tree_pac.binary_tree_pac.binary_node import BinaryNode


one = BinaryNode(1)

zero = BinaryNode(0)

three = BinaryNode(3)

five = BinaryNode(5)

eight = BinaryNode(8)
ten = BinaryNode(10)

one.left_child = zero
one.right_child = three

zero.right_child = five
zero.left_child = ten

three.right_child = eight


tree = one

print(tree.to_string())

print("==========")
print("Travel in order")
tree.travel_in_order(lambda x: print(x))

print("==========")
print("Travel pre order")
tree.travel_pre_order(lambda x: print(x))

print("==========")
print("Travel post order")
tree.travel_post_order(lambda x: print(x))

