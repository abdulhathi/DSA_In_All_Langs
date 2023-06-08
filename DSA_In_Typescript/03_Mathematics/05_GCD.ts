class GreatestCommonDevisor {
    gcd(a: number, b: number): number {
        if (b === 0)
            return a
        return this.gcd(b, a % b)
    }
}
console.log(new GreatestCommonDevisor().gcd(4, 6))