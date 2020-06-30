import math

def rabin_carp(a, b):
    # a - string to search 
    # b - string to search in 
    constants = get_mapping()
    m = len(a)
    n = len(b)
    # print(f"Length of string to search : {m}")
    # print(f"Length of string to search in {n}")
    original_rb_hash = get_rb_hash(a, n, constants)
    found = []
    i = 0
    j = m
    prev_s = b[i:j]
    prev_hash = get_rb_hash(prev_s, n, constants)
    if prev_s == a:
        found.append((i, j))
    i+=1
    j+=1
    while(j<=n):
        # print(f"i={i}, j={j}")
        prev_hash = get_rb_hash_next(b[i: j], n, b[i-1], b[j-1], prev_hash, constants)   
        if prev_hash == original_rb_hash and a == b[i:j]:
            found.append((i, j))
        # print(f"RB HASH for {b[i:j]} is {prev_hash}")
        i+=1
        j+=1
    print(f"Found {found}")    
    return found

def get_rb_hash(s, n, constants):
    sum_s = 0
    m = len(s)
    # print(f"Working on string {s}")
    s = s[::-1]
    for index, i in enumerate(s):
        sum_s += constants[i]*math.pow(n, index)
        # print(f"item under cursor {i} . value of sum_s = {sum_s}")
    return sum_s

def get_rb_hash_next(s, n, prev_char, next_char, prev_hash, constants):
    # print(f"Prev hash is {prev_hash}")
    prev_char_hash = constants[prev_char] * math.pow(n, len(s)-1)
    # print(f"{prev_char} hash is {prev_char_hash}")
    next_char_hash = constants[next_char] * math.pow(n, 0)
    # print(f"{next_char} hash = {next_char_hash}")
    new_hash = ((prev_hash - prev_char_hash)*n) + next_char_hash
    # print(f"New hash is {new_hash}")
    return new_hash


def get_mapping():
    x = "abcdefghijklmnopqrstuvwxyz"
    constants_for_hash = {alphabet: index+1 for index, alphabet in enumerate(x)}
    return constants_for_hash       


if __name__ == "__main__":
    b = "banana"
    a = "a"
    rabin_carp(a, b)
