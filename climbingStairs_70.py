"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Method: Dynamic Programming

"""


def climbStairs(n):
    one, two = 1, 1
    for i in range(n-1):
        temp = one
        one += two
        two = temp
    return one


print(climbStairs(5))
