"""Coding Challenge Skeleton #1
This counter function purpose is to count how many english letters does your name contain.
After writing your tests, develop the counter function as needed to pass all your tests.

"""


def counter(name):
    # Todo: implement me
    name = name.replace(" ", "")
    if len(name) == 0:
        raise Exception("Please input your name")
    if isinstance(name, str) and name.isalpha():
        return len(name)
    else:
        raise TypeError("Name must be a single string with only alphabets")

