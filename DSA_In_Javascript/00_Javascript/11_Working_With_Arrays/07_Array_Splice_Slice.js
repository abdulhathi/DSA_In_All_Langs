const arr = ["Abdul", "Amira", "Afsar", "Aysha", "Afraz"]

// Splice cut the array from the specified index to the lenght and return it. And original array is from 0 to specified index - 1
const res = arr.splice(2);
console.log(res);
console.log(arr);

// Slice method return a new array with the sliced index specified

const countries = ["India", "USA", "Dubai", "Thailand", "Saudi Arabia"];
const sliced = countries.slice(3);
console.log(sliced, countries);