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
# Original runtime would be O(n^2) because of the nested loops

bst = BinarySearchTree('asdfasdf')
for name_1 in names_1:
    bst.insert(name_1)
for name_2 in names_2:
    if bst.contains(name_2) == True:
        duplicates.append(name_2)
    



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

new_start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

str_dupes = set(names_1) & set(names_2)
str_duplicates = str_dupes

new_end_time = time.time()
print (f"{len(str_duplicates)} duplicates:\n\n{', '.join(str_duplicates)}\n\n")
print (f"runtime: {new_end_time - new_start_time} seconds")