# count vowels and consonants
def count_vowels_consonants(s: str):
    vowels = 'aeiouAEIOU'
    num_vowels = sum(1 for char in s if char in vowels)
    num_cons = sum(1 for char in s if char.isalpha() and char not in vowels)
    nums = sum(1 for char in s if char.isnumeric())
    return num_vowels, num_cons, nums


def count_consonants_between_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    vowel_indices = []
    count = 0
    d = []
    # Collect indices of vowels in the string
    for i, char in enumerate(s):
        if char in vowels:
            vowel_indices.append(i)
    for i in range(0, len(vowel_indices)-1):
        d.append(vowel_indices[i+1] - vowel_indices[i])
    return max(d) - 1

print(count_vowels_consonants("di1esoe"))
print(count_consonants_between_vowels("di1esoe"))