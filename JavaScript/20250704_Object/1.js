let arr = [2, 4, 6, 8, 333, 55, 77];
let brr = [2, 4, 6, 8, 333, 55, 77];

let areEqual = arr.length == brr.length;

if (areEqual) {
    let i = 0 
    while ((i <arr.length) && (arr[i] == brr [i])) {
        i++
    }
    areEqual = i == arr.length

}
console.log(areEqual);