# def string_sculptor(text: str) -> str:

#     text = text.lower()
#     update_s = ""
#     i = 0
#     y = 0

#     while i < len(text):

#         if text[i].isalpha() and y % 2 == 0:
#             update_s += text[i]
#             y += 1
#         elif text[i].isalpha() and y % 2 != 0:
#             update_s += text[i].upper()
#             y += 1
#         else:
#             update_s += text[i]

#         i += 1

#     return update_s

def string_sculptor(text: str) -> str:
    update_s = ""
    y = 0

    for ch in text.lower():

        if ch.isalpha():
            update_s += ch.upper() if y % 2 != 0 else ch
            y += 1
        else:
            update_s += ch

    return update_s


print(string_sculptor("hello"))
print(string_sculptor("Hello World"))
# print(string_sculptor("abc123def"))
# print(string_sculptor("Python3.9!"))
# print(string_sculptor("a b c"))
