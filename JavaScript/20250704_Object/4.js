let my_car = {
    speed: 97,         // km /h
    color: 'red',
}
let bus = {
    speed: 43,         // km /h
    color: 'red',
}
let areEqual = true;
for (let same in my_car) {
    if (my_car[same] !== bus[same]) {
        areEqual = false;
        break;
    }
}

console.log(areEqual);
