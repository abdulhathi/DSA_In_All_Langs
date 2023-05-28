// Currying funtions is a function allows to receive multiple functions as multiple argument in sequence manner.

const multiArgFunction = (a, b, c) => a + b + c
console.log(multiArgFunction(1,2,3));

// Currying function
const curryUnaryFunction = (a) => (b) => (c) => a + b + c
console.log(curryUnaryFunction(1))
console.log(curryUnaryFunction(1)(2))
console.log(curryUnaryFunction(1)(2)(3))