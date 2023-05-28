// Difference between let, var scope

function userDetails(lastName) {
  if (lastName) {
    console.log(varSalary);
    // console.log(letAge);
    var varSalary = 100000.00;
    let letAge = 39;
    console.log(letAge);
  }
  console.log(varSalary);
  // console.log(letAge);
}
userDetails("Abdul Hathi");

// fun1 with var name
var myName = "Abdul"
const fun1 = () => {
  
}

const fun2 = () => {
  try {
    console.log(myName);
  } catch(ex) {
    console.log(ex)
  }
}
fun2()