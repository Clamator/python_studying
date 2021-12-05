import unittest
import FizzBuzz
from FizzBuzz import get_reply

class FizzBuzzTest(unittest.TestCase):

    def test_fizz(self):
        number = 6
        result = FizzBuzz.get_reply(number)
        self.assertEqual(result, 'Fizz')

    def test_buzz(self):
        number = 10
        result = FizzBuzz.get_reply(number)
        self.assertEqual(result, 'Buzz')

    def test_fizzbuzz(self):
        number = 15
        result = FizzBuzz.get_reply(number)
        self.assertEqual(result, 'FizzBuzz')

if __name__ == '__main__':
    unittest.main()