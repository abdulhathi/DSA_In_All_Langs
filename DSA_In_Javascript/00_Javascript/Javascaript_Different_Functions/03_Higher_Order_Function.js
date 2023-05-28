// Receive a function in the parameter and return the function. Either or Both operations are called as Higher Order function.

const firstOrderFunc = () => "This is the first order function";

const higherOrderFunc = (firstOrderFunc) => firstOrderFunc();

console.log(higherOrderFunc(firstOrderFunc));