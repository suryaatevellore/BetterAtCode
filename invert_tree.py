from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert(self, a, b):  
        if (a is not None and b is None):
            b = TreeNode(a.val)
            a = "null"
        if (b is not None and a is None):
            a = TreeNode(b.val)
            b = "null"
        if (a in [None,"null"] or b in [None, "null"]):
            return True
        a.val, b.val = b.val, a.val
        return self.invert(a.left, b.right) and self.invert(a.right, b.left)

            
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        L = root.left
        R = root.right
        self.invert(L, R)
        return root

def make_a_full_tree(tree):
    # find the number of levels, max elements = summation_i(depth)
    # Return the closest number for 2
    from math import pow
    depth = len(tree) // 2
    max_elements = 0
    for i in range(depth+1):
        max_elements += pow(2, i)
    
    elements_needed_for_full_tree = int(max_elements) - len(tree)
    for i in range(elements_needed_for_full_tree):
        tree.append(None)
    
    print(f"Full tree is now {tree}")
    return tree

def arrange_tree(arr, root, i, n): 
    # Base case for recursion  
    if i < n: 
        temp = TreeNode(arr[i])  
        root = temp  
  
        # insert left child  
        root.left = arrange_tree(arr, root.left, 2 * i + 1, n)  
  
        # insert right child  
        root.right = arrange_tree(arr, root.right, 2 * i + 2, n) 
    return root  

def init_tree(tree: List):
    # Creates a tree from a List
    tree = make_a_full_tree(tree)
    root = None
    root = arrange_tree(tree, root, 0, len(tree))
    return root
    
def display_tree(root: TreeNode):
    if not root:
        return
    print(root.val, end=' ')
    display_tree(root.left)
    display_tree(root.right)

if __name__ == "__main__":
    tree = [1,2]
    root = init_tree(tree)
    s = Solution()
    temp = s.invertTree(root)
    display_tree(temp)
