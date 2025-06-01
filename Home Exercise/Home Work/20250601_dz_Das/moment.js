let seconds = 45; 
let totalSeconds = seconds + 580;

let minutes = Math.floor(totalSeconds / 60); 
let remainingSeconds = totalSeconds % 60;    

console.log(`Total time is ${minutes} minutes and ${remainingSeconds} seconds.`);
