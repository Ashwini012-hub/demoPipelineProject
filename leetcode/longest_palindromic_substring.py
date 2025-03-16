def longest_palindromic_substring(s):
    # n = len(s)
    # if n == 0:
    #     return ""

    longest_palindrome = s[0]  # Start by considering the first character as the longest palindrome

    # Generate all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s)):  # end is exclusive
            substring = s[i:j]
            # Check if the current substring is a palindrome
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring

    return longest_palindrome


# Example usage
input_string = "babad"
print("Input string:", input_string)
print("Longest palindromic substring:", longest_palindromic_substring(input_string))