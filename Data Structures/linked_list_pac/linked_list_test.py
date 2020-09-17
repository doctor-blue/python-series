from linked_list_pac.linked_list import LinkedList

linked_list = LinkedList()

# Add to first
linked_list.add_to_first(12) \
    .add_to_first(30) \
    .add_to_first(50)

print(linked_list.to_string())

# Add to end
linked_list.add_to_end(-2).add_to_end("Halo")

print(linked_list.to_string())

# insert "Hello" String at index = 2
linked_list.insert("Hello", 2)

print(linked_list.to_string())

# pop
print(linked_list.pop())

# linked list after pop
print(linked_list.to_string())

# remove last index
print(linked_list.remove_last())

# linked list after remove
print(linked_list.to_string())

