/** расстояния на машине 53 км
 * расстояния на пешком 60 км
 * скорость пешком 5 кмч
 * скорость на машине 20 кмч
 * Занятия начинаются в 19.05 вечером
 */


let Distance1 = 53; //Километра на машине
let Distance2 = 60; //км пешком.
let work = 19.5; //Занятия начинаются
let speed = 5;
let speed2 = 20;
let result = Distance1 / speed2 
let result3 = work - result
let result2 = Distance2 / speed
let result4 =  work - result2 
console.log('Километра на машине: ', result, ' часа.', 'выйти дома:',result3, ' часов.' );
console.log('км на пешком: ', result2, ' часов.','выйти дома:',result4, ' часов.');


