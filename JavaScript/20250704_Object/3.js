let my_car = {
    speed: 97,         // km /h
    color: 'red',
}
let your_car = {
    speed: 97,         // km /h
    color: 'red',
}
let areEqual = true;
for (let same in my_car) {
    if (my_car[same] !== your_car[same]) {
        areEqual = false;
        break;
    }
}

console.log(areEqual);
