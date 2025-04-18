import helper
import heapq
import itertools


# Function to compute the heuristic value for a given state.
# It calculates the minimum distance to the nearest goal state. 
# The distance is defined as the number of bits that differ between the state and the goal.

def heuristic(state: str, legal_patterns: list) -> int:
    distances = []
    for pattern in legal_patterns:
        # For each bit, if pattern[i] is not 'X', compare it with state[i]
        dist = sum(1 for i in range(len(state)) if pattern[i] != 'X' and state[i] != pattern[i])
        distances.append(dist)
    return min(distances) if distances else float('inf')

def greedy(start: str, goals: list, illegal: list, limit: int) -> tuple:
    visited = set()
    order = []
    counter = itertools.count()  # for tie-breaking (older nodes have lower count)
    
    # Priority queue stores tuples: (priority, count, current_state, path)
    fringe = []
    h = heuristic(start, goals)
    heapq.heappush(fringe, (h, next(counter), start, [start]))
    
    while fringe:
        if len(order) >= limit:
            return 'SEARCH FAILED', order
        
        prio, _, current, path = heapq.heappop(fringe)
        
        # Skip if already expanded or if the state is illegal
        if current in visited or helper.is_match(current, illegal):
            continue
        
        visited.add(current)
        order.append(current)
        
        # Check if current state is a goal state (matches one of the legal patterns)
        if current in goals or helper.is_match(current, goals):
            return path, order
        
        # Generate children by flipping each bit (in order: leftmost first)
        for i in range(len(current)):
            child = helper.bit_flip(current, i)
            if child in visited or helper.is_match(child, illegal):
                continue
            new_h = heuristic(child, goals)
            heapq.heappush(fringe, (new_h, next(counter), child, path + [child]))
    
    return 'SEARCH FAILED', order
