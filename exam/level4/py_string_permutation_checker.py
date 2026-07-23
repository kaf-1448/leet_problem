def string_permutation_checker(s1: str, s2: str) -> bool:

    count = {}

    clean_s1 = s1.replace(' ', '')
    clean_s2 = s2.replace(' ', '')

    if len(clean_s1) != len(clean_s2):
        return False

    for ch in clean_s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in clean_s2:

        if count.get(ch, 0) == 0:
            return False

        count[ch] -= 1

    return True


print(string_permutation_checker("abc", "bca"))
print(string_permutation_checker("abc", "def"))
print(string_permutation_checker("listen", "silent"))
print(string_permutation_checker("hello", "bello"))
print(string_permutation_checker("", ""))
print(string_permutation_checker("a", ""))
print(string_permutation_checker("Abc", "abc"))
print(string_permutation_checker("a gentleman", "elegant man"))
