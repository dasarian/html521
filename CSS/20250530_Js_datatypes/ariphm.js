/**
 * отработка арифметических орераторов
 * создайте переменную и задайте ей любое числовое значение
 * ИСПОЛЬЗУЕМ АРИФМЕТИКУ в 2 раза
 * Вычтите 10
 * Возьмите остаток от деления на 8
 * Возведите в третью степень
 * Увеличьте на 1 инкрементом
 * Выведите результат
 */

let operator=1000;
console.log('создали переменную', operator);
operator*=2;
console.log('Увеличи вдвое', operator)
operator-=10;
console.log("вычли 10", operator);
let rest_operator=operator%8;
console.log("результат присвоили новой переменной", rest_operator);
rest_operator**=3;
console.log("возвели в 3 степень", rest_operator);
rest_operator++;
console.log("выполнили инкремент ", rest_operator);