"""
A module for solving delete node in bst problem.
"""
# Definition for a binary tree node.
class TreeNode:
    """
    A class for work with treenodes.
    """
    def __init__(self, val=0, left=None, right=None):
        """
        Initializing variables.
        """
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    A class for solving delete a node in bst problem.
    """
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        A method for solving delete a node in bst problem.
        """
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root
