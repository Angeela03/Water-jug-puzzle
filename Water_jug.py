from math import gcd as bltin_gcd
import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from search import Problem


class WaterJug(Problem):

    def __init__(self, initial, m, n, x, goal=None):
        Problem.__init__(self, initial, goal)
        self.m = m
        self.n = n
        self.x = x

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        state_m = state[0]
        state_n = state[1]
        act = []
        if state_m > 0:
            act.append("Empty m")
        if state_n > 0:
            act.append("Empty n")
        if state_m > 0 and state_n < self.n:
            act.append("Pour m to n")
        if state_n > 0 and state_m < self.m:
            act.append("Pour n to m")
        if state_m < self.m:
            act.append("Fill m")
        if state_n < self.n:
            act.append("Fill n")

        return act

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
        res_m = state[0]
        res_n = state[1]
        if action == "Fill m":
            return (self.m, res_n)
        elif action == "Fill n":
            return (res_m, self.n)
        elif action == "Empty m":
            return (0, res_n)
        elif action == "Empty n":
            return (res_m, 0)
        elif action == "Pour m to n":
            return (res_m - self.n + res_n, self.n) if res_n + res_m >= self.n else (0, res_n + res_m)
        elif action == "Pour n to m":
            return (res_n + res_m, 0) if res_n + res_m <= self.m else (self.m, res_n - self.m + res_m)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state[0] == self.x or state[1] == self.x

    def check_solvability(self, state, m, n):
        """ Checks if m and n are co-prime"""

        return bltin_gcd(m, n) == 1
