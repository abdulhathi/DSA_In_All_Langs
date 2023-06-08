class GreatestCommonDevisor {
    gcd(a, b) {
        if (b === 0)
            return a;
        return this.gcd(b, a % b);
    }
}
console.log(new GreatestCommonDevisor().gcd(4, 6));
