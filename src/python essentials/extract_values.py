'''
extract the company/s that contains less than 9 value
'''

## Data
companies = {
'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}

## One-Liner
illegal = [x for x in companies if any(y<9 for y in companies[x].values())]

## for loop equivalent
illegal2 = []
for x in companies:
    if any(y<9 for y in companies[x].values()):
        illegal2.append(x)

## result
print(companies)
print(f"Data:\n{companies}")
print(f"\nOne-liner:\n{illegal}\n")
print(f"For loop equivalent (company/s that contains less than 9 value):\n{illegal2}")
