
// Count trailing zeros by multiple of five.
// TIME : O(logn), SPACE : O(1)
const countTrailingZeros = (num) => {
    let count = 0;
    for (let i = 5; i <= num; i *= 5) {
        count = count + Math.floor(num / i)
    }
    return count
}

console.log(countTrailingZeros(251));