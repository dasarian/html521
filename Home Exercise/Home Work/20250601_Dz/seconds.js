let seconds = 45; 
let totalSeconds = seconds + 580;

// Calculate the number of minutes and the remaining seconds
let minutes = Math.floor(totalSeconds / 60); // Get the total minutes
let remainingSeconds = totalSeconds % 60;    // Get the remaining seconds

console.log(`Total time is ${minutes} minutes and ${remainingSeconds} seconds.`);



Правда ли, что 5800 секунд больше часа? Больше 2х часов?

const seconds = 5800;
const isMoreThanOneHour = seconds > 3600; // 1 hour = 3600 seconds
const isMoreThanTwoHours = seconds > 7200; // 2 hours = 7200 seconds

console.log(`Is 5800 seconds more than an hour? ${isMoreThanOneHour}`);
console.log(`Is 5800 seconds more than two hours? ${isMoreThanTwoHours}`);


Правда ли, что если цена составляет 230 рублей за штуку
    и купили 27 штук, то хватит 500 рублей? 5000 рублей? 7000 рублей?

const pricePerPiece = 230;
const quantity = 27;
const totalCost = pricePerPiece * quantity;

const is500Enough = 500 >= totalCost;
const is5000Enough = 5000 >= totalCost;
const is7000Enough = 7000 >= totalCost;

console.log(`Is 500 rubles enough? ${is500Enough}`);
console.log(`Is 5000 rubles enough? ${is5000Enough}`);
console.log(`Is 7000 rubles enough? ${is7000Enough}`);


Правда ли, что 5000 рублей хватит, а 7000 НЕ хватит 

const is5000EnoughButNot7000 = is5000Enough && !is7000Enough;

console.log(`Is it true that 5000 rubles will be enough, but 7000 will NOT be enough? ${is5000EnoughButNot7000}`);
