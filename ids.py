import helper 
from collections import deque

# Function to perform dfs search algorithm.
# It starts from a given state and explores each branch within the depth-limit, 
# increasing hte depth-limit per iterationas until a goal state is found or
# the node expansion limit is reached.
def ids(start: str, goals: list, illegal: list, limit:int) -> tuple:

    order = []
    level = 0

    while True:
        # If limit is exceeded and goal is not found, return search failed
        # and the order it took
        if len(order) >= limit:
            return 'SEARCH FAILED', order

        path, current_order, success = ids_helper(start, goals, illegal, limit, level, len(order))
        order += current_order
        # If goal is fond return the path and traversal order
        if success:
            return path, order
        
        level += 1

# Helper function to perform the search for each depth limit
def ids_helper(start: str, goals: list, illegal: list, limit:int, level:int, count:int) -> tuple:

    visited = set()
    depth = 0
    fringe = deque([(start, [start], depth)])
    order = []

    while(fringe):
  
        current, path, depth = fringe.popleft()
        
        if depth > level:
            continue

        if current in visited or helper.is_match(current, illegal):
            continue

        visited.add(current)
        order.append(current)

        if current in goals or helper.is_match(current, goals):
            return path, order, True
        
        if count + len(order) >= limit:
            return None, order, False
        
        children_to_add = []
        # Expanfing the children by flipping the bits in order 
        for i in range(len(current)):
            child = helper.bit_flip(current, i)
            if child not in visited and not helper.is_match(child, illegal):
                children_to_add.append((child, path+[child], depth+1))
         # Ensuring children are added to the fringe in the correct order
        for child in reversed(children_to_add):
            fringe.appendleft(child)

    return None, order, False
