def is_permutation(string1, string2):
    """
    :param string1: first string
    :param string2: second string
    :return: if string1 and string2 are permutation
    """

    # Check if the lengths of the two strings are different
    if len(string1) != len(string2):
        return False

    # Initialize dictionaries to store character counts for each string
    char_counter_string1 = {}
    char_counter_string2 = {}

    # Count character occurrences in string1
    for char in string1:
        char_counter_string1[char] = char_counter_string1.get(char, 0) + 1

    # Count character occurrences in string2
    for char in string2:
        char_counter_string2[char] = char_counter_string2.get(char, 0) + 1

    # Check if the character counts are the same for both strings
    return char_counter_string1 == char_counter_string2


# Test
result = is_permutation("haawbsc", "bsaawch")
print(F"Result ---> {result}")
