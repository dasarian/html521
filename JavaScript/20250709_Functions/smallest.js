function findSmallestNumber() {
    let smallest = arguments[0];
    for (let i = 1; i < arguments.length; i++) {
        if (arguments[i] < smallest) {
            smallest = arguments[i];
        }
    }
    return smallest;
}

console.log(findSmallestNumber(5, 2, 9, 1, 7)); 
