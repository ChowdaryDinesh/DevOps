from collections import Counter
def first_non_repeating_char(s: str):
    char_count = Counter(s)
    for char in s:
        if char_count[char] == 1:
            return char

print(first_non_repeating_char("dinesh"))