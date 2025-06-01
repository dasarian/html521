

const seconds = 5800;
const isMoreThanOneHour = seconds > 3600; // 1 hour = 3600 seconds
const isMoreThanTwoHours = seconds > 7200; // 2 hours = 7200 seconds

console.log(`Is 5800 seconds more than an hour? ${isMoreThanOneHour}`);
console.log(`Is 5800 seconds more than two hours? ${isMoreThanTwoHours}`);



const pricePerPiece = 230;
const quantity = 27;
const totalCost = pricePerPiece * quantity;

const is500Enough = 500 >= totalCost;
const is5000Enough = 5000 >= totalCost;
const is7000Enough = 7000 >= totalCost;

console.log(`Is 500 rubles enough? ${is500Enough}`);
console.log(`Is 5000 rubles enough? ${is5000Enough}`);
console.log(`Is 7000 rubles enough? ${is7000Enough}`);



const is5000EnoughButNot7000 = is5000Enough && !is7000Enough;

console.log(`Is it true that 5000 rubles will be enough, but 7000 will NOT be enough? ${is5000EnoughButNot7000}`);
