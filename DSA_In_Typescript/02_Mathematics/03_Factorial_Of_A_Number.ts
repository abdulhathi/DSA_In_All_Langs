// Iterative
function factorial_Iterative(num: number): number {
    let factorial: number = 1;
    for (let i: number = 2; i <= num; i++) {
        factorial = factorial * i
    }   
    return factorial;
}

console.log(factorial_Iterative(5));
console.log(factorial_Iterative(100));

// Recursive
function factorial_Recursive(num: number): number {
    if (num === 1)
        return 1;
    return num * factorial_Recursive(num - 1);
}

console.log(factorial_Iterative(5))