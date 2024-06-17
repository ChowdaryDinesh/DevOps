# palindrome

def is_palindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    return False

def is_palindrome_2(s: str) -> bool:
    if s ==  "".join(reversed(s)):
        return True
    return False

def is_palindrome_for(s: str) -> bool:
    rev_s = ""
    for i in s:
        rev_s = i + rev_s
    if rev_s == s:
        return True
    return False

# using while

def is_plaindrome_while(s: str) -> bool:
    first, last = 0, len(s)-1
    while first < last:
        if s[first] == s[last]:
            first +=1
            last -=1
        else: 
            return False
        return True

s = "sas"
print(is_palindrome(s))
print(is_palindrome_2(s))
print(is_palindrome_for(s))
print(is_plaindrome_while(s))