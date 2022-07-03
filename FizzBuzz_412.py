"""
Given an integer n, return a string array answer (1-indexed) where
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Note: This approach won't reduce the asymptotic complexity, but proves to be a neater solution when FizzBuzz comes with a twist. What if FizzBuzz is now FizzBuzzJazz i.e.
3 ---> "Fizz" , 5 ---> "Buzz", 7 ---> "Jazz"
"""


def fizzBuzz(n):
    op = []

    for i in range(1, n+1):
        temp = ''
        if i % 3 == 0:
            temp += "Fizz"
        if i % 5 == 0:
            temp += "Buzz"
        if temp == '':
            temp = str(i)
        op.append(temp)
    return op


print(fizzBuzz(15))
