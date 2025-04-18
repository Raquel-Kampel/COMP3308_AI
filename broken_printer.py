import sys
import bfs
import dfs
import ids
import a_star
import hill_climb
import greedy


def broken_printer(char, filename):
    limit = 1000
    with open(filename, 'r') as file:
        lines = file.readlines()
        
        start = str(lines[0].strip())
        if not all(char in '01' for char in start) or len(start) <3 or len(start) >12:
            return 'SEARCH FAILED'
        goals = list(map(str, lines[1].strip().split(',')))
        illegal = list(map(str, lines[2].strip().split(','))) if len(lines) > 2 else []   
        
    match char:
        case 'B':
            res = bfs.bfs(start, goals, illegal, limit)
            print_values(res)
        case 'D':
            res = dfs.dfs(start, goals, illegal, limit)
            print_values(res)
        case 'I':
            res = ids.ids(start, goals, illegal, limit)
            print_values(res)
        case 'G':
            res = greedy.greedy(start, goals, illegal, limit)
            print_values(res)
        case 'A':
            res = a_star.astar(start, goals, illegal, limit)
            print_values(res)
        case 'H':
            res = hill_climb.hill_climb(start, goals, illegal, limit)
            print_values(res)
        case _:
            print("SEARCH FAILED")
    return ''

def print_values(res):
    if res[0] == 'SEARCH FAILED':
        print('SEARCH FAILED')
    else:
        print(','.join(map(str, res[0])))
    print(','.join(map(str, res[1])), end='')
    

if __name__ == '__main__':
    if len(sys.argv) < 3:
        # You can modify these values to test your code
        char = 'H'
        filename = 'example2.txt'
    else:
        char = sys.argv[1]
        filename = sys.argv[2]
    print(broken_printer(char, filename))
  
