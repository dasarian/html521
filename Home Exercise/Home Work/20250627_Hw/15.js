// Дан массив упорядоченных чисел [2, 4, 6, 7, 8, 14, 16, 18] 
// найти, есть ли в массиве число 8 бинарным поиском

function search(){
const chislo = me.valueAsNumber

let arr = [2, 4, 6, 7, 8, 14, 16, 18]
let left = 0
let right = arr.length -1
let middle = -1
while (right - left > 1) {
   let middle = Math.floor((right+left) / 2) 
   if (chislo < arr[middle]) {
    right = middle -1
   } else {
    left = middle
   }
   console.log(left, right)
}
}
