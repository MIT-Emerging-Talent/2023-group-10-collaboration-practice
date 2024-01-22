def mergesort_v1(L):
    '''It takes an arry like list as input and sort it in acending order.
    Input: an array
    Output: a sorted array
    L: is a list'''
    if len(L) <= 1:
        return L

    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]

    left = mergesort_v1(left)
    right = mergesort_v1(right)

    return merge_v1(left, right)

def merge_v1(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def mergesort_v2(L):
    if len(L) <= 1:
        return L

    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]

    left = mergesort_v2(left)
    right = mergesort_v2(right)

    return merge_v2(left, right)

def merge_v2(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result