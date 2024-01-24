def count(input):
    output = {}
    for i in range(len(input)):
        if input[i] in output:
            output[input[i]] += 1
        else:
            output[input[i]] = 1
    return output


input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1))  # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}


def group_by_key(input):
    output = {}
    for i in range(len(input)):
        cur_key = input[i]['key']
        if cur_key in output:
            output[cur_key] += input[i]['value']
        else:
            output[cur_key] = input[i]['value']
    return output


input2 = [
    {'key': 'a', 'value': 3},
    {'key': 'b', 'value': 1},
    {'key': 'c', 'value': 2},
    {'key': 'a', 'value': 3},
    {'key': 'c', 'value': 5}
]
print(group_by_key(input2))  # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
