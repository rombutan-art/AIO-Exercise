"2. Count the number of characters in a string and store them in a dictionary data structure"

"""
    This function count number of characters.
    Input: string.
    Output: dictionary.
"""


def count_chars(string):
    char_count = {}
    for char in string:
        # Check condition that only alphabetic characters are counted
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


if __name__ == "__main__":
    # Input a word and counts characters
    user_input = input("Enter a word: ")
    char_counts = count_chars(user_input)
    print(char_counts)

# Test case
test_case_1 = 'too much'
expected_1 = {'t': 1, 'o': 2, 'm': 1, 'u': 1, 'c': 1, 'h': 1}
assert count_chars(
    test_case_1) == expected_1, f"Test case 1 failed: {count_chars(test_case_1)} != {expected_1}"

