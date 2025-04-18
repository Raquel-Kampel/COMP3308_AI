import helper
import itertools

def heuristic(state: str, legal_patterns: list) -> int:
    """
    Compute the heuristic value for a given state.
    For each legal pattern (which may contain 'X'), compute the Hamming distance 
    ignoring positions where the legal pattern has 'X'. Return the minimum such distance.
    """
    distances = []
    for pattern in legal_patterns:
        # Calculate Hamming distance ignoring positions with 'X'
        dist = sum(1 for i in range(len(state)) if pattern[i] != 'X' and state[i] != pattern[i])
        distances.append(dist)
    return min(distances) if distances else float('inf')

# Function to perform hill climbing search algorithm.
# It starts from a given state and explores neighboring states by flipping bits.
# The search continues until a goal state is found or the node expansion limit is reached.
# The heuristic function is used to evaluate the states.
def hill_climb(start: str, goals: list, illegal: list, limit: int) -> tuple:
    visited = set()  # to avoid cycles
    order = []       # order of expanded nodes
    count = 0        # counter for expanded nodes
    
    current = start
    path = [start]
    current_h = heuristic(current, goals)
    
    # If the starting state is illegal, immediately fail.
    if helper.is_match(current, illegal):
        return 'SEARCH FAILED', order
    
    while True:
        # Check expansion limit
        if count >= limit:
            return 'SEARCH FAILED', order
        
        # Mark current as visited (if not already) and record expansion order.
        if current not in visited:
            visited.add(current)
            order.append(current)
            count += 1
        
        # Check if current state is a goal.
        if current in goals or helper.is_match(current, goals):
            return path, order
        
        # Generate children by flipping each bit (leftmost to rightmost)
        children = []
        for i in range(len(current)):
            child = helper.bit_flip(current, i)
            # Only consider child if it is not visited and not illegal.
            if child in visited or helper.is_match(child, illegal):
                continue
            children.append(child)
        
        # If no children are available, then hill climbing has reached a dead end.
        if not children:
            return 'SEARCH FAILED', order
        
        # Evaluate children to find one with strictly lower heuristic than current.
        best_child = None
        best_h = current_h
        for child in children:
            h_val = heuristic(child, goals)
            # Strict improvement: choose the child only if its evaluation is lower.
            if h_val < best_h:
                best_h = h_val
                best_child = child
        
        # If no child has a lower evaluation, then we've reached a local maximum.
        if best_child is None:
            return 'SEARCH FAILED', order
        
        # Move to the best child and update path and current evaluation.
        current = best_child
        path.append(current)
        current_h = best_h
