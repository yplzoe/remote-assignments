def find_max(numbers):
    length = len(numbers)
    if length == 0:
        return None
    cur_max = numbers[0]
    for i in range(length):
        if numbers[i] > cur_max:
            cur_max = numbers[i]
    return cur_max


def find_position(numbers, target):
    length = len(numbers)
    if length == 0:
        return -1
    for i in range(length):
        if numbers[i] == target:
            return i
    return -1


# your code here
print(find_max([1, 2, 4, 5]))  # should print 5
print(find_max([5, 2, 7, 1, 6]))  # should print 7
print(find_position([5, 2, 7, 1, 6], 5))  # should print 0
print(find_position([5, 2, 7, 1, 6], 7))  # should print 2
# should print 2 (the first one)
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))
print(find_position([5, 2, 7, 1, 6], 8))  # should print -1
