// Pure function
const arr = []
console.log(arr.push(5))

console.log(arr.concat([10]))
console.log(arr)

// Impure function
const impureFunc = (num) => {
  arr.push(num);
  return arr;
};
console.log(impureFunc(20))

const impureFunc1 = (num) => {
  const concatArr = arr.concat([num])
  return [arr, concatArr]
};
console.log(impureFunc1(21))

// Pure function
const pureFunc = (num) => (argNumsArr) => {
  return [arr, argNumsArr.concat([num])];
}
console.log(pureFunc(100)(arr));
