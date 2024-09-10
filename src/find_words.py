## Data
text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

## One-Liner
w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]

## for loop equivalent
z = []
for line in text.split('\n'):
    li = []
    for x in line.split():
        if len(x)>3:
            li.append(x)
    z.append(li)

## Result
print(f"test:\n{text}")
print(f"\nOne-liner (W):\n{w}\n")
print(f"For loop   equivalent (Z):\n{z}")