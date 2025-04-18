import re 

# Helper function to change the bit at the specified index
def bit_flip(bit_str, i):
    bits = list(bit_str)
    bits[i] = '1' if bits[i] == '0' else '0'
    return ''.join(bits)

# Helper funciton to determine if a string matches the value in the list
# including matching with 'X', where 'X' is a placeholder for '0' or '1'
def is_match(value: str, values:list):
    if value in values:
        return True
    
    for _ in values:
        if 'X' in _:
            bit = '^' + _.replace('X', '[01]') + '$'
            if re.fullmatch(bit, value):
                return True
        else:
            continue
    return False

