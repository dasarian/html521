function findSmallestNumber(a, b, c) {
    if (a <= b && a <= c) {
        return a;
    } else if (b <= a && b <= c) {
        return b;
    } else {
        return c;
    }
}
console.log(findSmallestNumber(5, 2, 9)); 
console.log(findSmallestNumber(-1, -5, 0)); 
console.log(findSmallestNumber(10, 10, 8)); 
