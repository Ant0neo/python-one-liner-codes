'''
replace specific items (in this case 'corrupted' items)
'''

## Data
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
'Safari', 'corrupted', 'Safari', 'corrupted',
'Chrome', 'corrupted', 'Firefox', 'corrupted']

print(f"Before:\n{visitors}")

## One-Liner
visitors[1::2] = visitors[::2]


## for loop equivalent
for x in range(len(visitors)):
    if x%2 != 0:
        visitors[x] = visitors[x-1]


## result
print(f"After:\n{visitors}")
