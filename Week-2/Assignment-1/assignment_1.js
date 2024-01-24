function findMax(numbers) {
  const len = numbers.length;
  if (len === 0) {
    return -1;
  }
  let curMax = numbers[0];
  for (let i = 0; i < len; i++) {
    if (numbers[i] > curMax) {
      curMax = numbers[i];
    }
  }
  return curMax;
}

function findPosition(numbers, target) {
  const len = numbers.length;
  if (len === 0) {
    return -1;
  }
  for (let i = 0; i < len; i++) {
    if (numbers[i] === target) {
      return i;
    }
  }
  return -1;
}

// Test cases
console.log(findMax([1, 2, 4, 5])); // should print 5
console.log(findMax([5, 2, 7, 1, 6])); // should print 7
console.log(findPosition([5, 2, 7, 1, 6], 5)); // should print 0
console.log(findPosition([5, 2, 7, 1, 6], 7)); // should print 2
// should print 2 (the first one)
console.log(findPosition([5, 2, 7, 7, 7, 1, 6], 7));
console.log(findPosition([5, 2, 7, 1, 6], 8)); // should print -1
