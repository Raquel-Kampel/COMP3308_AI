import helper
from collections import deque

# Function to perform bfs search algorithm.
# It starts from a given state and explores neighboring states by flipping bits.
# It performs a layer by layer seach until a goal state is found or the node expansion limit is reached.
def bfs(start: str, goals: list, illegal: list, limit: int) -> tuple:

    visited = set()
    fringe = deque([(start, [start])])
    order = []
    
    while(fringe):
                
        current, path = fringe.popleft()

        if current not in visited:
            visited.add(current)
            order.append(current)

        # If goal is fond return the path and traversal order
        if current in goals or helper.is_match(current, goals):
            return path, order

        # If limit is exceeded and goal is not found, return search failed
        # and the order it took
        if len(order) >= limit:
            return 'SEARCH FAILED', order

        # Expanfing the children by flipping the bits in order   
        for i in range(len(current)):
            child = helper.bit_flip(current, i)
            if child in visited or helper.is_match(child, illegal):
                continue
            fringe.append((child, path+[child]))
    
    # If there are no more children to expand and a goal is not found
    # return a search failed and the order it took
    return 'SEARCH FAILED', order

