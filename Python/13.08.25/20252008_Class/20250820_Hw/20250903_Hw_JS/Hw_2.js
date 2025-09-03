let kg = prompt("Please enter weight in kilograms: ");
kg = parseFloat(kg);

let tons = kg / 1000;
let grams = kg * 1000;

console.log(`Weight in tons: ${tons.toFixed(2)}`);
console.log(`Weight in grams: ${grams.toFixed(2)}`);