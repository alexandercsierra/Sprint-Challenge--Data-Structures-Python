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



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = BinarySearchTree(value)
        if self.value == None:
            self.value = value
        elif self.value > value:
            if self.left == None:
                self.left = node
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right == None:
                self.right = node
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.left != None:
            if self.value > target:
                if self.left == target:
                    return True
                else:
                    return self.left.contains(target)
        if self.right != None:
            if self.value < target:
                if self.right == target:
                    return True
                else:
                    return self.right.contains(target)
        else:
            return False
            

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value != None:
            max = self.value
            if self.right != None:
                max = self.right.value
                return self.right.get_max()
            return max
        else: 
            return None

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
            if self.left != None:
                self.left.for_each(fn)
            fn(self.value)
            if self.right != None:
                self.right.for_each(fn)
            

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node.for_each(print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q = Queue()
        q.enqueue(node)
        while len(q) > 0:
            curr = q.dequeue()
            if curr.right != None:
                q.enqueue(curr.right)
            if curr.left != None: 
                q.enqueue(curr.left)
            print(curr.value)
            
        
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = []
        stack.append(node)
        while len(stack) > 0:
            curr = stack.pop()
            if curr.right != None:
                stack.append(curr.right)
            if curr.left != None:
                stack.append(curr.left)
            print(curr.value)

        #start with root node, add to stack
        #does it have a left node? add to stack
            #repeat until no more left nodes
            #no more left nodes? check right 
                #if right, add to stack




import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# bst = BinarySearchTree(names_1[0])
# for name_1 in names_1:
#     if bst.contains(name_1) == True:
#         duplicates.append(name_1)
#     else:
#         bst.insert(name_1)
# for name_2 in names_2:
#     if bst.contains(name_2) == True:
#         duplicates.append(name_2)
#     else:
#         bst.insert(name_2)

# bst = BinarySearchTree('asdfasdf')
# dupes = BinarySearchTree('flibbertygibbet')
# for name_1 in names_1:
#     if bst.contains(name_1) == True:
#         dupes.insert(name_1)
#     else:
#         bst.insert(name_1)
# for name_2 in names_2:
#     if bst.contains(name_2) == True:
#         dupes.insert(name_2)
#     else:
#         bst.insert(name_2)
    
    
# dupes.for_each(duplicates.append)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BinarySearchTree('asdfasdf')
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2) == True:
        duplicates.append(name_2)
    
    

end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
print('there were', len(duplicates), 'dupes')

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

