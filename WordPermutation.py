def is_permutation(string1, string2):
    """
    :param string1: first string
    :param string2: second string
    :return: if string1 and string2 are permutation
    """
    if len(string1) != len(string2):
        return False

    char_counter_string1 = {}
    char_counter_string2 = {}

    for char in string1:
        char_counter_string1[char] = char_counter_string1.get(char, 0) + 1

    for char in string2:
        char_counter_string2[char] = char_counter_string2.get(char, 0) + 1

    return char_counter_string1 == char_counter_string2


# Test
result = is_permutation("haawbsc", "bsaawch")
print(F"\nResult ---> {result}")
