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

    def test_permutation_8(self):
        self.assertEqual(is_permutation("AbCdEf", "aBcDeF"), False, "Test case failed: Case sensitivity")

    def test_permutation_9(self):
        self.assertEqual(is_permutation("hello world", "dlrow olleh"), True, "Test case failed: Whitespace")

    def test_permutation_10(self):
        self.assertEqual(is_permutation("!@#$%^", "%^$#@!"), True, "Test case failed: Special characters")

    def test_permutation_11(self):
        self.assertEqual(is_permutation("a" * 1000000, "a" * 1000000), True, "Test case failed: Long strings")

    def test_permutation_12(self):
        self.assertEqual(is_permutation("café", "éfac"), True, "Test case failed: Unicode characters")


if __name__ == '__main__':
    unittest.main()
