const names = ["Abdul", "Aysha", "Afsar"];

// Iterate using the for loop
for (let i = 0; i < names.length; i++) {
  console.log(names[i]);
}

// Iterate using the for of loop
for (const [i, name] of names.entries()) {
  console.log(name, i);
}

// Iterate using foreach
names.forEach(name => console.log(name));
names.forEach((name, ind) => console.log(name, ind));