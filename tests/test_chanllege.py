import unittest
from challenge import counter


class EasyTestCase(unittest.TestCase):
    def test_easy_input(self):
        # Todo: make sure that your program returns 2 given the string 'Mo'
        pass

    def test_easy_input_two(self):
        # Todo: make sure that your program returns 8 given the string 'Mohammad'
        pass


class MediumTestCase(unittest.TestCase):
    def test_medium_input(self):
        # Todo: make sure that the program raises an exception whenever there is any non-english charts. Ex. !@#$%^.
        pass

    def test_medium_input_two(self):
        # Todo: make sure that your program does not count paces. It should only count english alpha.
        pass


class HardTestCase(unittest.TestCase):
    def test_hard_input(self):
        # Todo: make sure that the program raises an exception whenever an empty string is given.
        pass

    def test_hard_input_two(self):
        # Todo: make sure that your program does not accept a None input.
        pass


if __name__ == '__main__':
    unittest.main()
