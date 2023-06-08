
class TrailingZeors {
    // Find trailing zeros using 5
    count(fact: number): number {
        let count: number = 0
        while (fact % 5 === 0) {
            fact = Math.floor(fact / 5)
            count += fact
        }
        return count;
    }

    // Find trailing zeros using multiple of 5
    countMultipleOfFive(fact: number): number {
        let count: number = 0;
        for (let i: number = 5; i <= fact; i *= 5) {
            count = count + Math.floor(fact / i)
        }
        return count
    }
}

const trailingZeros = new TrailingZeors();
console.log(trailingZeros.count(5));
console.log(trailingZeros.count(10));
console.log(trailingZeros.count(100));