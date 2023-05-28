const employee1 = { FullName: "Abdul Hathi", Age: 39 };
function fun1(a, b, c) {
  console.log("Message from fun1 and sum of params " + (a+b+c));
  console.log(`Employee information : ${this.FullName} - ${this.Age}`);
};

// Call method in javascript - Call method invoke the function and use this keyword to keyword get the object values.
fun1.call(employee1, 10, 20, 30);

// Apply method in javascript - Apply method to pass the arguments in array format
fun1.apply(employee1, [1,2,31]);

// Bind method in javascript - hold bind call return value in a variable and call the function with arguments
const empObjFunction = fun1.bind(employee1);
empObjFunction(100,200,300);