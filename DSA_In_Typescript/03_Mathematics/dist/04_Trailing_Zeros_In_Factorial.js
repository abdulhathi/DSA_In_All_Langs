// Find trailing zeros using 5
class TrailingZeors {
    count(fact) {
        let count = 0;
        while (fact % 5 === 0) {
            fact = Math.floor(fact / 5);
            count += fact;
        }
        return count;
    }
}
const trailingZeros = new TrailingZeors();
console.log(trailingZeros.count(5));
console.log(trailingZeros.count(10));
console.log(trailingZeros.count(100));
