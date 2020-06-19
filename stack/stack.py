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
#         return self.size

#     def push(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             self.size -= 1
#             return self.storage.pop()

# linked list for data structure
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        node = self.storage.remove_head()
        return node


new_stack = Stack()
new_stack.push(1)
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
print(new_stack.pop())
print(new_stack.__len__())
