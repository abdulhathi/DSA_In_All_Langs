// Time : O(n) Space : O(1)
const sumOfNNaturalNums = function(n) {
  let sum = 0
  for (let i = 1; i <= n; i++) {
    sum += i
  }
  return sum
}

console.log(sumOfNNaturalNums(5))

// Efficient approach 

const sumOfNNaturalNums1 = function(n) {
  return (n * (n+1)) / 2
}

console.log(sumOfNNaturalNums1(5))
console.log(sumOfNNaturalNums1(3))