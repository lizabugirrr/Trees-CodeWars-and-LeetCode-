"""
A module for solving binary tree traversal problem.
"""
class Node:
    """
    A class for binary tree traversal problem.
    """
    def __init__(self, data):
        """
        Initializing variables.
        """
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    """
    Method for pre order notation.
    """
    if node is None:
        return []
    result = [node.data]
    result.extend(pre_order(node.left))
    result.extend(pre_order(node.right))
    return result

def in_order(node):
    """
    Method for in order notation.
    """
    if node is None:
        return []
    result = []
    result.extend(in_order(node.left))
    result.append(node.data)
    result.extend(in_order(node.right))
    return result

def post_order(node):
    """
    Method for post order notation.
    """
    if node is None:
        return []
    result = []
    result.extend(post_order(node.left))
    result.extend(post_order(node.right))
    result.append(node.data)
    return result
