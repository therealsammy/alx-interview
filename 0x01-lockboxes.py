#!usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""

def canUnlockAll(boxes):
    """
    Checks if all the boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists, where each inner list represents a box and contains integers that are keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    visited = set()
    queue = [0]  # Starting with box 0

    while queue:
        current_box = queue.pop(0)
        visited.add(current_box)

        for key in boxes[current_box]:
            if key not in visited:
                queue.append(key)

    return len(visited) == n
