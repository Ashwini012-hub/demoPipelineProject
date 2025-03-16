def length_of_longest_substring(s):
    char_index_map = {}
    max_length = 0
    start = 0

    # Enumerate over the characters in the string, with index and character
    for index, char in enumerate(s):
        # If the character is already in the dictionary and the last occurrence is inside the current window
        if char in char_index_map and char_index_map[char] >= start:
            # Move the start to the position right after the last occurrence of the character
            start = char_index_map[char] + 1
        # Update or add the character's last seen index
        char_index_map[char] = index
        # Calculate the length of the current substring and update max_length accordingly
        max_length = max(max_length, index - start + 1)

    return max_length

# Example usage
input_string = "babad"
print("Input string:", input_string)
print("Length of the longest substring without repeating characters:", length_of_longest_substring(input_string))


def longest_substring_without_repetation(s):
    # n = len(s)
    # if n == 0:
    #     return ""
    global sub_without_repeat
    longest = s[0]  # Start by considering the first character as the longest palindrome

    # Generate all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s)+ 1):  # end is exclusive
            substring = s[i:j]
            # remove duplicates from substring
            sub_without_repeat = set(substring)
            if len(sub_without_repeat) > len(longest):
                longest = sub_without_repeat

    return len(longest)


# Example usage
input_string = "babad"
print("Input string:", input_string)
print("Longest palindromic substring:", longest_substring_without_repetation(input_string))