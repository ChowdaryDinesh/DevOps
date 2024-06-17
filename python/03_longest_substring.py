"""
    Given a string, find the length of the longest substring
    without repeating characters.
"""

def longest_substring(s: str):
    d_len = dict()
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if len(set(s[i:j])) == len(s[i:j]):
                d_len[s[i:j]] = len(s[i:j])
    print(d_len)
    return max(d_len, key=d_len.get)
def length_of_longest_substring(s: str) -> int:
    char_index_map = {}
    start = max_length = 0
    
    for i, char in enumerate(s):
        if char in char_index_map and start <= char_index_map[char]:
            start = char_index_map[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        
        char_index_map[char] = i
    
    return max_length


print(longest_substring("abcabcdbb"))
print(length_of_longest_substring("abcabcdbb"))    