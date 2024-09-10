'''
flag the item if it contains the word 'anonymous'.
'''

## Data
txt = ['lambda functions are anonymous functions.',
'anonymous functions dont have a name.',
'functions are objects in Python.']

## One-Liner
mark = list(map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt))


## for loop equivalent with func helper
def funct(t):
    if 'anonymous' in t:
        return (True)
    else:
        return (False)
    

mark2 = []
for tx in txt:
    mark2.append((funct(tx),tx))

## result
print(f"Data:\n{txt}")
print(f"\nOne-liner:\n{mark}\n")
print(f"For loop equivalent:\n{mark2}")
