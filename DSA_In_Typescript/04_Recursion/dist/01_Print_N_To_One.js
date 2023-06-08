class PrintNToOne {
    constructor() {
        this.result = [];
    }
    printNToOne_Recursively(n) {
        if (n === 0)
            return this.result;
        this.result.push(n);
        return this.printNToOne_Recursively(n - 1);
    }
}
console.log(new PrintNToOne().printNToOne_Recursively(5));
