# Implementation of Shift-And algorithm 
# as described in "Flexible Pattern Matching In Strings" by Gonzalo Navarro and Mathieu Raffinot
# Names of variables have been kept same as text to make it easy to follow

def shiftAnd(pattern, text):
    
    if len(pattern) == 0 or len(text) == 0:
        raise ValueError("Pattern and Text must be > 1 in length")
    
    match_indexes = []
    
    m = len(pattern)
    B = {}
    for j in range(m):
        try:
            mask = B[pattern[j]]
        except KeyError:
            mask = 0
            
        B[pattern[j]] = mask | 1 << j
        
    D = 0
    for pos, char in enumerate(text):
        try:
            mask = B[char]
        except KeyError:
            mask = 0
            
        D = (D << 1 | 1) & mask
        
        if D & (1 << m-1):
            match_indexes.append(pos-m+1)
            
    return match_indexes
