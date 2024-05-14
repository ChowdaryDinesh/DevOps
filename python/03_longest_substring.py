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

print(longest_substring("abcabcdbb"))
    