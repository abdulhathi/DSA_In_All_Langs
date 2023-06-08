const result = [];
const printNToOne_Recursively = (n) => {
    if (n === 0)
        return result
    result.push(n)
    return printNToOne_Recursively(n-1)
}

console.log(printNToOne_Recursively(5))