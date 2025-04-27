"""
A module for solving sorting binary tree by levels problem.
"""
def tree_by_levels(node):
    """
    A function for solving sorting binary tree by levels problem.
    """
    if not node:
        return []
    result = []
    queue = [node]
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result
