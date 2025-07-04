let arr = [2, 4, 6, 8, 333, 55, 77]
let crr = [2, 4, 66]
let areEqual = arr.length == crr.length;

if (areEqual) {
    let i = 0 
    while ((i <arr.length) && (arr[i] == crr [i])) {
        i++
    }
    areEqual = i == arr.length

}
console.log(areEqual);