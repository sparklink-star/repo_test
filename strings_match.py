def match_strings(str1, str2):
    if str1 == str2:
        return "The strings match!"
    else:
        return "The strings do not match."

# Example usage:
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

result = match_strings(string1, string2)
print(result)
