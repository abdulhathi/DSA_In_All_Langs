// Time : O(n) Space : O(1)
const factorial = (num) => {
  let fact = 1
  while (num > 0) {
    fact *= num
    num -= 1
  }
  return fact
}

console.log(factorial(6))