
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def find_middle(self):
        middle = self.head
        end = self.head
        while end.next != None and end.next.next != None:
            end = end.next.next
            middle = middle.next
        return middle


    # def iterate_list(node):
    #     while node is not None:
    #         print(node.value)
    #         node = node.next


    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # wrap the given value in a ListNode
        new_node = ListNode(value, None, None)
        self.length += 1
        # handle if list has a head
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # handle if list has no head
        else:
            self.head = new_node
            self.tail = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)

        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1

        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            self.head = new_node
        self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):

        value = node.value
        self.delete(node)
        self.add_to_head(value)


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):

        # if list is empty
        if not self.head:
            print("you got nothing on me!")
            return
        
        self.length -= 1

        # if list has just one item
        if self.head == self.tail:
            self.head = None
            self.tail = None

     # we have at least two nodes, and the node we want to delete is the head
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        
        # we have at least two nodes, and the node we want to delete is the tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None

        else:
            node.delete()

######################################################################################

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
          self.max_nodes = limit
          self.current_nodes = 0

          self.dll = DoublyLinkedList()
          self.dict = {}


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
   

    def get(self, key):
          if key not in self.dict:
            return None
          
          node = self.dll.head
          while node is not None:
                if key == node.value[0]:
                  self.dll.move_to_front(node)
                  break
                node = node.next

          return self.dict[key]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, val):
        # if key is already stored, overwrite old value
        if key in self.dict:
            # overwrite in dictionary
            self.dict[key] = val
            # overwrite in dll
            node = self.dll.head
            while node is not None:
                if key == node.value[0]:
                    node.value[1] = val
                    # move to head of dll
                    self.dll.move_to_front(node)
                    break
                node = node.next

        else:
            # handle case where we are already full
            if self.current_nodes == self.max_nodes:
                # delete something (LRU)
                node = self.dll.tail
                old_key = node.value[0]
                self.dll.remove_from_tail()

                del self.dict[old_key]    #OR self.dll.pop[old_key]
                self.current_nodes -= 1
                
            # if key isn't store and we are not full, just add to cache
            if key not in self.dict:
                self.dict[key] = val
                self.dll.add_to_head([key, val])

                self.current_nodes += 1

      


         
