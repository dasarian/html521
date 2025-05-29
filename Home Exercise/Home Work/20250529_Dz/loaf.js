/** Решить задачу. 
 * У меня осталось 2000 рублей. 
 * Когда я куплю туфельки за 750 рублей и 
 * 10 шоколадок за 83 рубля штука, 
 * сколько батонов хлеба можно будет купить на сдачу? Стоимость батона посмотреть в ближайшем магазине. 
 * примерно 50 руб 
 */


let total_money = 2000;
let shoes = 750;
let chocolate = 83;
let quantity_choco = 10;
let loaf_price = 50;
let chocolate_cost = chocolate * quantity_choco
let All_cost = shoes + chocolate_cost
let left_money = total_money - All_cost
let quantity_loaf = left_money / loaf_price

console.log ('Quantity of loaf : ', quantity_loaf, ' pcs.')

