def anagram(s1: str, s2: str) -> bool:

    clean_s1 = s1.lower().replace(' ', '')
    clean_s2 = s2.lower().replace(' ', '')

    count = {}

    for ch in clean_s1:
        count[ch] = count.get(ch, 0) + 1

    for ch in clean_s2:

        if ch not in count:
            return False

        if ch in count and count[ch] == 0:
            return False

        count[ch] -= 1

    for val in count.values():

        if val != 0:
            return False

    return True


print(anagram("listen", "silent"))
print(anagram("Triangle", "Integral"))
print(anagram("Dormitory", "Dirty Room"))
print(anagram("hello", "world"))
print(anagram("", ""))
print(anagram("abca", "abc"))
print(anagram("aab", "abb"))
