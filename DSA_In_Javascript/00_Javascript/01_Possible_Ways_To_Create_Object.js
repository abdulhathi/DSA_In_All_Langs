// 1. Using Object constructor
const obj1 = new Object();

// 2. Using Object.Create method
const obj2 = Object.create(null);

// 3. Object literal syntax
const obj3 = {
  name: "Abdul",
  age: 39
}
console.log(obj3);

// 4. Function constructor to create an object
function Person(name, age) {
  this.name = name;
  this.age = age
}
const obj4 = new Person("Aysha", 33);
console.log(obj4);

// 5. Function constructor with prototype
function Employee() {};
Employee.prototype.name = "Abdul";
var employee = new Employee();
console.log(employee);

function func() {};
new func(x, y, z);