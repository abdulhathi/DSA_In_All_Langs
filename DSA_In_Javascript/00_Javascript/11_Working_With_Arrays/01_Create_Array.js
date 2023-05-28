// Create array using [] (squar bracket)
const names = ["Abdul", "Aysha", "Afsar"];
console.log(names)


// Create array using Array() constructor
const myNames = new Array();
const myNames1 = new Array(["Abdul", "Aysha"]);
const myNames2 = new Array();
console.log(myNames2);

// Create array using spread operator
const arr = [...Array(5)];
console.log(arr);

// Create array using Array.fill
const arr1 = new Array(5).fill()
console.log(arr1);