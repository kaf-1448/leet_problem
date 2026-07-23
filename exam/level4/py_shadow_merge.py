# def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
#     lists = list1 + list2
#     lists.sort()
#     return lists


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    i, j = 0, 0
    marged = []

    while i < len(list1) and j < len(list2):

        if list1[i] <= list2[j]:
            marged.append(list1[i])
            i += 1

        else:
            marged.append(list2[j])
            j += 1

    marged.extend(list1[i:])
    marged.extend(list2[j:])

    return marged


# print(shadow_merge([1, 3, 5], [2, 4, 6]))
# print(shadow_merge([1, 2, 3], [4, 5, 6]))
# print(shadow_merge([1], [2, 3, 4]))
# print(shadow_merge([], [1, 2, 3]))
print(shadow_merge([1, 1, 2], [1, 3, 3]))
