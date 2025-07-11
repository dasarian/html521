function findSmallestNumber(a, b, c) {
    let smallest;
    if (a <= b && a <= c) {
        smallest = a;
    } else if (b <= a && b <= c) {
        smallest = b;
    } else {
        smallest = c;
    }
    return smallest;
}

console.log(findSmallestNumber(5, 2, 9)); 


