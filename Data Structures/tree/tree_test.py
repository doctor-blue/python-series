from tree.tree_node import TreeNode

food = TreeNode("Food")

freshFood = TreeNode("Fresh food")

fastFood = TreeNode("Fast food")

vegetables = TreeNode("Vegetables")

spinach = TreeNode("Spinach")

eggplant = TreeNode("Eggplant")

broccoli = TreeNode("Broccoli")

meat = TreeNode("Meat")

chicken = TreeNode("Chicken")

turkey = TreeNode("Turkey")

burger = TreeNode("Burger")

pizza = TreeNode("Pizza")

food.add_node(fastFood)
food.add_node(freshFood)

fastFood.add_node(burger)
fastFood.add_node(pizza)

freshFood.add_node(vegetables)
freshFood.add_node(meat)

vegetables.add_node(spinach)
vegetables.add_node(eggplant)
vegetables.add_node(broccoli)

meat.add_node(chicken)
meat.add_node(turkey)

# food.for_each_depth_first(lambda x: print(x.value))
food.for_each_lever_order(lambda x: print(x.value))
print("==================")
print(food.search("Chicken"))
