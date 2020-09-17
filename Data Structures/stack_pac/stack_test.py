from stack_pac.stack import Stack
import stack_pac.stack as stack

# my_stack = Stack()

# my_stack.push(1).push(2).push(3)
#
# print(my_stack.to_string())
#
# popped_element = my_stack.pop()
# print(f'Popped = {popped_element}')

# print(my_stack.peek())
# print(my_stack.to_string())

fruits = ["Banana", "Papaya", "Apple", "Orange", "Cherry"]
my_stack = stack.create(fruits)

print(my_stack.to_string())

my_stack = stack.stack_of(1, 2, 6, 3, 8, 9)

print(my_stack.to_string())
