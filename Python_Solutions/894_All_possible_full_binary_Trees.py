# # Definition for a binary tree node.
# #Solution 1:
# Step 2: Representing a Node
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def allPossibleFBT(n):
#     # Step 3: Base case
#     if n == 0:
#         return [None]  # None represents an empty tree

#     # Step 4: Recursive approach
#     trees = []
#     for i in range(1, n, 2):
#         left_trees = allPossibleFBT(i)  # All possible left subtrees
#         right_trees = allPossibleFBT(n - i - 1)  # All possible right subtrees

#         # Building all combinations of left and right subtrees
#         for left_tree in left_trees:
#             for right_tree in right_trees:
#                 root = TreeNode(0)  # Create the root node with value 0
#                 root.left = left_tree
#                 root.right = right_tree
#                 trees.append(root)

#     return trees

# # Test the function with n=7
# result = allPossibleFBT(7)
# print("List of possible full binary trees with 7 nodes:")
# for tree in result:
#     print(tree)

# #Solution 2:
# class TreeNode:
#      def __init__(self, val=0, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right


# class Solution:
#     def allPossibleFBT(self, n: int) -> list:
#         if n % 2 == 0:
#             return []

#         if n == 1:
#             return [TreeNode()]

#         trees = []
#         for i in range(1, n, 2):
#             left_subtrees = self.allPossibleFBT(i)
#             right_subtrees = self.allPossibleFBT(n - i - 1)

#             for left_tree in left_subtrees:
#                 for right_tree in right_subtrees:
#                     root = TreeNode()
#                     root.left = left_tree
#                     root.right = right_tree
#                     trees.append(root)

#         return trees

    
# # Create an instance of the Solution class
# solution = Solution()

# # Call the generate_full_binary_trees method with the desired number of nodes
# n = 5
# result_trees = solution.allPossibleFBT(n)

# print(result_trees)

#Solution 3:
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def allPossibleFBT(self, n: int):
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode()]

        trees = []
        for i in range(1, n, 2):
            left_subtrees = self.allPossibleFBT(i)
            right_subtrees = self.allPossibleFBT(n - i - 1)

            for left_tree in left_subtrees:
                for right_tree in right_subtrees:
                    root = TreeNode()
                    root.left = left_tree
                    root.right = right_tree
                    trees.append(root)
        print(trees)
        return trees
    
def print_tree(root, level=0, prefix="Root: "):
    if root is None:
        return

    indent = "    " * level
    print(indent + prefix + str(root.val))

    print_tree(root.left, level + 1, "Left: ")
    print_tree(root.right, level + 1, "Right: ")

# Example usage:
solution = Solution()
n = 7
result_trees = solution.allPossibleFBT(n)

for idx, root in enumerate(result_trees, 1):
    print(f"Tree {idx}:")
    print_tree(root)
    print()