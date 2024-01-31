import unittest

from WordPermutation import is_permutation


class TestWordPermutation(unittest.TestCase):

    def test_permutation_1(self):
        self.assertEqual(is_permutation("haawbs", "bsaawch"), False,
                         "Test case 1 failed: The strings should not be permutations")

    def test_permutation_2(self):
        self.assertEqual(is_permutation("haawbsc", "bsaawch"), True,
                         "Test case 2 failed: The strings are not permutations")

    def test_permutation_3(self):
        self.assertEqual(is_permutation("", ""), True,
                         "Test case 3 failed: The strings are not permutations")

    def test_permutation_4(self):
        self.assertEqual(is_permutation("qwert", "trewq"), True,
                         "Test case 4 failed: The strings are not permutations")

    def test_permutation_5(self):
        self.assertEqual(is_permutation("111555599999", "951999551591"), True,
                         "Test case 5 failed: The strings are not permutations")

    def test_permutation_6(self):
        self.assertEqual(is_permutation("&&^%$^!*%", "^%&!$%^&*"), True,
                         "Test case 6 failed: The strings are not permutations")

    def test_permutation_7(self):
        self.assertEqual(is_permutation("", "h"), False,
                         "Test case 7 failed: The strings should not be permutations")


if __name__ == '__main__':
    unittest.main()
