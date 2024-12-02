str = "bicefogu$jbbbjjj%3233"
vowels = ['a', 'e', 'i', 'o', 'u']

vowels_count = {}
consonants_count = {}
non_alpha_chars = {}

for j in str:
    if j in vowels:
        vowels_count[j] = vowels_count.get(j, 0) + 1
    elif j.isalpha():
        consonants_count[j] = consonants_count.get(j, 0) + 1
    else:
        non_alpha_chars[j] = non_alpha_chars.get(j, 0) + 1
print("Vowels count:", vowels_count)
print("Consonants count:", consonants_count)
print("Non Alpha count:", non_alpha_chars)
