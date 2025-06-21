for (let i = 2; i <= 9; i++) {
    console.log(`3 * ${i} = ${3 * i}`);
}

/**
 * Цикл: напечатайте в консоль:
 
 * 3*2=6
 * 3*3=9
 * ...
 * 3*9=27

 * в столбик.

 */
const three      = 3;
let number1      = 2;
const max_number = 9;
while (number1 < max_number + 1) {
   console.log(three + '*' + number1 + '=' + (three * number1));  // 3*2.....9
   // 6 9 12      27
   number1 = number1 + 1;  // 3 4
}