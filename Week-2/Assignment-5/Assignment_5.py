def binary_search_first(numbers, target):
    length = len(numbers)
    if length == 0:
        return -1
    if length == 1 and numbers[0] != target:
        return -1
    left = 0
    right = length - 1
    while left <= right:
        mid = (right + left)//2
        # print(right)
        # print(mid)
        # print(left)
        # print()
        if mid == left:
            return mid + 1
        if target == numbers[mid]:
            while mid > 0 and numbers[mid - 1] == target:
                mid -= 1
            return mid
        if target > numbers[mid]:
            left = mid
        else:
            right = mid
    return -1


# should print 1 (the index of the target number ‘2’)
print('-----------')
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2))
# should print 2 (the index of the ‘first’ target number ‘5’ shows up)
print('-----------')
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))
# should print 2 (since it can’t find number 3, return the index of ‘the smallest number larger than 3', that is, the index of the ‘first’ number 5)
print('-----------')
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3))
print(binary_search_first([2, 4, 6], 3))
