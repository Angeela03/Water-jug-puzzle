from search import iterative_deepening_search
from Water_jug import WaterJug
from math import gcd as bltin_gcd
import sys
import os.path
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
initial_state = (0, 0)

# because m has to be<=15 and n has to be <=3
list_m = [m for m in range(1, 50)]
list_n = [n for n in range(1,5)]
solution = None


def solve():
    """
    this function considers 10 random values for m and n and returns the solutions for all the values
    between (1 and max(m))
    """
    count = 0
    while count <= 10:
        m_choice = np.random.choice(list_m)
        n_choice = np.random.choice(list_n)

        # m should be be equal to n
        if m_choice != n_choice:
            if bltin_gcd(m_choice, n_choice) == 1:
                count = count + 1
                for i in range(1, m_choice + 1):
                    print(m_choice, n_choice, i)
                    puzzle = WaterJug(initial_state, m_choice, n_choice, i)
                    ans = iterative_deepening_search(puzzle)
                    print(ans.path())

solve()
