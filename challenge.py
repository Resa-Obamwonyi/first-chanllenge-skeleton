"""Coding Challenge #1
"""


def counter(name: str) -> int:
    name = name.replace(' ', '')
    if len(name) == 0:
        raise Exception("Please input your name.")
    if name.isalpha():
        return len(name)
    else:
        raise Exception("The string must contain english letters only.")


