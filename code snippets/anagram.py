
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    # Convert strings to lists and sort them
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Compare sorted lists
    return sorted_str1 == sorted_str2


