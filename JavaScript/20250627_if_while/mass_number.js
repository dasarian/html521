//             0  1  2  3  4  5  6  7  8  9           
const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
let i = 1
while(i < 10) { 
    array[i] *= 100;
    console.log(array[i])
    i += 2
}