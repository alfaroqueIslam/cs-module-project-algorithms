from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)
            elif value >= self.value:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        else:
            return True

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left:
            self.left.for_each(fn)
        fn(self.value),
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print( self.value),
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        self.level = 1
        queue = deque([self])
        output = []
        current_level = self.level

        while len(queue)>0:

            current_node = queue.popleft()

            if(current_node.level >= current_level):
                output.append("\n")
                current_level += 1

            print(str(current_node.value))

            if current_node.left != None:
                current_node.left.level = current_level + 1 
                queue.append(current_node.left)
            


            if current_node.right != None:
                current_node.right.level = current_level + 1 
                queue.append(current_node.right)
 

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        self.level = 1
        stack = deque([self])
        current_level = self.level


        while len(stack)>0:

            current_node = stack.pop()

            if(current_node.level >= current_level):
                current_level += 1

            print(str(current_node.value))

            if current_node.left != None:
                current_node.left.level = current_level + 1 
                stack.append(current_node.left)
            


            if current_node.right != None:
                current_node.right.level = current_level + 1 
                stack.append(current_node.right)
        
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    c= 0
    l = 0
    BSTNode n = new BSTNode()
    for i in range(len(nums)):
        c = c + 1
        
        lst.append(max)

    return lst


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
