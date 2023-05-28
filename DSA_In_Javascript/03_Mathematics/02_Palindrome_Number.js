const palindromeNumber = function(num) {
  let revNum = 0, temp = num
  while (temp > 0) {
    revNum = (revNum * 10) + temp % 10
    temp = Math.floor(temp / 10)
  }
  return revNum === num
}

console.log(palindromeNumber(787))
console.log(palindromeNumber(78007))
console.log(palindromeNumber(780087))