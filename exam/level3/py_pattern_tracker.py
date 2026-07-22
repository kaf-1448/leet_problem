# def pattern_tracker(text: str) -> int:
#     count = 0

#     for i in range(1, len(text)):

#         if ord(text[i]) >= 48 and ord(text[i]) <= 56:
#             if ord(text[i-1]) + 1 == ord(text[i]):
#                 count += 1

#     return count


def pattern_tracker(text: str) -> int:

    count = 0

    for i in range(1, len(text)):

        if text[i-1].isdigit() and text[i].isdigit():
            if int(text[i-1]) == int(text[i]) - 1:
                count += 1

    return count


# print(pattern_tracker("123456789"))
# print(pattern_tracker("123"))
# print(pattern_tracker("12a34"))
# print(pattern_tracker("987654321"))
# print(pattern_tracker("abc"))
print(pattern_tracker("1a2b3c4"))
print(pattern_tracker("112233"))
