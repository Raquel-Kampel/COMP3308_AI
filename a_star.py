import helper
import heapq
import itertools

# Function to compute the heuristic value for a given state.
def heuristic(state: str, legal_patterns: list) -> int: 
    distances = []
    for pattern in legal_patterns:
        dist = sum(1 for i in range(len(state)) if pattern[i] != 'X' and state[i] != pattern[i])
        distances.append(dist)
    return min(distances) if distances else float('inf')

"""
Function to perform A* search algorithm.
It uses a priority queue to explore the most promising nodes first.
The heuristic function is used to estimate the cost to reach the goal.
g is the cost so far (number of steps), and f = g + h.
"""
def astar(start: str, goals: list, illegal: list, limit: int) -> tuple:
    visited = set()
    order = []
    counter = itertools.count()
    h = heuristic(start, goals)
    g = 0
    f = g + h
    fringe = []
    heapq.heappush(fringe, (f, next(counter), start, [start], g))
    
    while fringe:
        if len(order) > limit:
            return 'SEARCH FAILED', order
        
        f, _, current, path, g = heapq.heappop(fringe)
        
        if current in visited or helper.is_match(current, illegal):
            continue
        
        visited.add(current)
        order.append(current)
        
        if current in goals or helper.is_match(current, goals):
            return path, order
        
        # Expand children by flipping each bit (in ascending order)
        for i in range(len(current)):
            child = helper.bit_flip(current, i)
            if child in visited or helper.is_match(child, illegal):
                continue
            new_g = g + 1
            new_h = heuristic(child, goals)
            new_f = new_g + new_h
            heapq.heappush(fringe, (new_f, next(counter), child, path + [child], new_g))
    
    return 'SEARCH FAILED', order
