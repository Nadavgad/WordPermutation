import unittest
from WordPermutation import is_permutation


class TestWordPermutation(unittest.TestCase):

    def test_not_permutation_different_lengths(self):
        """
        Test for strings with different lengths which should not be considered permutations.
        """
        self.assertEqual(is_permutation("haawbs", "bsaawch"), False,
                         "Strings with different lengths should not be permutations")

    def test_permutation_same_characters(self):
        """
        Test for strings with the same characters which should be considered permutations.
        """
        self.assertEqual(is_permutation("haawbsc", "bsaawch"), True,
                         "Strings with the same characters should be permutations")

    def test_permutation_empty_strings(self):
        """
        Test for empty strings which should be considered permutations.
        """
        self.assertEqual(is_permutation("", ""), True,
                         "Empty strings should be considered permutations")

    def test_permutation_reversed_strings(self):
        """
        Test for reversed strings which should be considered permutations.
        """
        self.assertEqual(is_permutation("qwert", "trewq"), True,
                         "Reversed strings should be permutations")

    def test_permutation_numeric_strings(self):
        """
        Test for numeric strings with the same digits which should be considered permutations.
        """
        self.assertEqual(is_permutation("111555599999", "951999551591"), True,
                         "Numeric strings with same digits should be permutations")

    def test_permutation_special_characters(self):
        """
        Test for strings with special characters which should be considered permutations.
        """
        self.assertEqual(is_permutation("&&^%$^!*%", "^%&!$%^&*"), True,
                         "Strings with special characters should be permutations")

    def test_not_permutation_empty_and_nonempty(self):
        """
        Test for an empty string and a non-empty string which should not be considered permutations.
        """
        self.assertEqual(is_permutation("", "h"), False,
                         "Empty string and non-empty string should not be permutations")

    def test_not_permutation_case_sensitive(self):
        """
        Test for case-sensitive permutations which should not be considered permutations.
        """
        self.assertEqual(is_permutation("AbCdEf", "aBcDeF"), False,
                         "Permutations should be case-sensitive")

    def test_permutation_with_whitespace(self):
        """
        Test for strings with the same characters and different whitespace which should be permutations.
        """
        self.assertEqual(is_permutation("hello world", "dlrow olleh"), True,
                         "Strings with same characters and different whitespace should be permutations")

    def test_permutation_long_strings(self):
        """
        Test for long strings with the same characters which should be permutations.
        """
        self.assertEqual(is_permutation("a" * 1000000, "a" * 1000000), True,
                         "Long strings with same characters should be permutations")

    def test_permutation_with_unicode(self):
        """
        Test for strings with Unicode characters which should be permutations.
        """
        self.assertEqual(is_permutation("café", "éfac"), True,
                         "Strings with Unicode characters should be permutations")


if __name__ == '__main__':
    unittest.main()
