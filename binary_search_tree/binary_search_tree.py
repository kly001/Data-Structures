"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the incoming value is less than our current node's value
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        if target == self.value:
            return True
        if target < self.value:
            # go left if it is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if it is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self): # recursive version
        # we'll keep going right until there are no more nodes on the right side
        if not self.right:
            return self.value
        return self.right.get_max()

    def iterative_get_max(self):
        current_max = self.value
        current = self
    # traverse our structure
        while current is not None:
            if current.value > current_max:
                current_max = current.value
    # update our current_max variable with the value
            current = current.right
        return current_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn): # recursive version
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    def iterative_for_each(self, fn):
        stack = []
        stack.append(self)
        while  len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            
            fn(current.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # node = self.value
        if self.left is not None:
            self.left.in_order_print(self.left)
            print(node.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
            pass
        # make a queue
        # enqueue the node
        # as long as the queue is not empty,
        # dequeue from the front; this is the current node
        # enqueue the kids of the current node in the queue
     


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

    
        # make a stack
        # push the node on the stack
        # as long as the stack is not empty,
        # pop off the stack, this is our current node
        # put the kids on the stack; check that they are not none

        stack = []
        stack.append(node)

        while len(stack) != 0:
            node = stack.pop()
            print(node.value)

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)





    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
