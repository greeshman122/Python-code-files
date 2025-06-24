def find_all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substr = s[i:j]
            substrings.append(substr)
    return substrings

# Example usage
string = "greeshman"
all_substrings = find_all_substrings(string)
print("All substrings:")
for substr in all_substrings:
    print(substr)
