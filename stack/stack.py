from linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# - Should have the methods: `push`, `pop`, and `len`.
#   - `push` adds an item to the top of the stack.
#   - `pop` removes and returns the element at the top of the stack
#   - `len` returns the number of elements in the stack.


# arrays for data structure
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         return self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop()

# linked list for data structure
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.storage.get_length()

    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_tail()


new_stack = Stack()
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
print(new_stack.__len__())
new_stack.pop()
print(new_stack.__len__())
