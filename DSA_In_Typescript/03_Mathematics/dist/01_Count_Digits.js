function countDigits(num) {
    let count = 0;
    while (num > 0) {
        count += 1;
        num = Math.floor(num / 10);
    }
    return count;
}
console.log(countDigits(100));
