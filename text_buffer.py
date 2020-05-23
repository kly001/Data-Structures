
# add to the front of a text buffer
#  add to the back of a text buffer
# delete from the back of a text buffer
# delete from the front of a text buffer

# join text buffers together

# add to the middle

# array vs DLL

# array: add to back O(1)
# array: add tofront 0(n)


import sys

sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class TextBuffer:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def __str__(self):
        string_to_return = ""
        

    def join(self, other_buffer):
        pass

    def append(self, string_to_add):
        
        for char in string_to_add:
            self.storage.add_to_tail(char)

    def prepend(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_head(char)

    def delete_from_front(self, string_to_add):
        self.storage.remove_from_head()

    def delete_from_back(self, string_to_add):
        pass