def are_anagrams(str1, str2):
    # If the lengths of the strings are not the same, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Create a dictionary to count character frequencies
    count = {}

    # Count characters for the first string
    for char in str1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Subtract the count for characters in the second string
    for char in str2:
        if char in count:
            count[char] -= 1
        else:
            # If the char is not in count, str1 does not have it, hence they aren't anagrams
            return False

    # Ensure all counts are zero - that each char's count has been fully balanced between the two strings
    for char in count:
        if count[char] != 0:
            return False

    return True


# Example usage
s1 = "listen"
s2 = "silent"
print(are_anagrams(s1, s2))  # Output: True
