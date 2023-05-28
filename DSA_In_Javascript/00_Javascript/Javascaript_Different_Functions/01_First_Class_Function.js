// The function can treat any other variables

const param = (message) => console.log(message);

const funWithfuncAsParam = (func) => func("Hi how are you.")

funWithfuncAsParam(param);

// The function return an another function

const myFunction = () => {
  const returnFunc = () => {
    console.log("Message from return function");
  }
  return returnFunc;
}

const res = myFunction();
res();

const obj = {
  Name: "Abdul",
  Age: 29
}

console.log(obj);