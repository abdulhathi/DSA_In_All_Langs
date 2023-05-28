const countries = ["India", "USA", "Dubai", "Thailand", "Saudi Arabia"];

const res = countries.map((v,i,arr) => {
  console.log(v);
  return `${v} - ${i}`
});

console.log(res);