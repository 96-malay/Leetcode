"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""


def text(self, s):
    s1 = []
    for c in s:
        if s1 and c == '#':
            s1.pop()
        elif c != '#':
            s1.append(c)
    return s1


def backspaceCompare(self, s: str, t: str) -> bool:
    return self.text(s) == self.text(t)
