def binary_search_position(numbers, target):
  length=len(numbers)
  if length==0:
    return -1
  if length==1 and numbers[0]!=target:
    return -1
  left=0
  right=length-1
  while left<=right:
    mid=(right+left)//2
    # print(left)
    # print(right)
    # print(mid)
    # print()
    if target==numbers[mid]:
      return mid
    if target>numbers[mid]:
      left=mid
    else:
      right=mid
  return -1

print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3
