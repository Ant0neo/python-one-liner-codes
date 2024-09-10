'''
calculate the net income and identify
who earns more after tax.
'''

## Dependencies
import numpy as np

## Data: yearly salary in ($1000) [2017, 2018, 2019]
alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]

salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])

## One-liner
mul_income = (salaries * taxation)
max_income = (salaries - mul_income)

## Result
print("Salaries:\n",salaries)
print("Salaries with tax:\n",mul_income)
print("Maximum Income:\n",max_income)
print(np.max(max_income))

print(f"Floor Division of 8/3 is {8//3} and its Qoutent is {8/3}.")