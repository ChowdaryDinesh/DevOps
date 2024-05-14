"""Problem 1:
    Find the index when Sum is greater than the input value.
    Explanation:
    1. Two inputs N and S are provided.
    2. Find out the prime numbers below N.
    3. Cylic over the prime Number list above, find the index at which sum > S.
    Example:
     1. N = 10 S = 25
     2. Prime Numbers below N = [2,3,5,7]
     3. Now sum 2+3+5+7 = 17, repeat the cycle again 17 + 2 + 3 + 5 = 27 > 25.
        At this index 2, sum is > S
     return 2
     Example 2:
        1. N = 10 S = 50
        2. Prime Numbers below N = [2,3,5,7]
        3. Now sum 2+3+5+7 = 17, repeat the cycle again 17 + 2 + 3 + 5 + 7 = 34
              repeat the cycle again 34 + 2 + 3 + 5 + 7 = 51 > 50.
        At this index 3, sum is > S
"""

def prime_numbers(n: int):
    """Function to find the prime numbers below N"""
    prime = list()
    prime.append(2)
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                prime.append(i)
    return prime

def find_index_sum(n: int, s: int):
    """Function to find the index when sum is greater than S"""
    prime = prime_numbers(n)
    sum = 0
    i = 0
    list_length = len(prime)
    while True:
        sum += prime[i]
        if sum > s:
            return i
        i += 1
        i = i % list_length

print(find_index_sum(10, 50))