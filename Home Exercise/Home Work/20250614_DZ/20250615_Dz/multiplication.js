function start(){
document.getElementById('checkButton').addEventListener
            const num1 = parseInt(document.getElementById('num1').value);
            const num2 = parseInt(document.getElementById('num2').value);
            const expectedProduct = num1 * num2;
            const userAnswer = parseInt(document.getElementById('userInput').value);

            if (userAnswer === expectedProduct) {
                console.log("yes, correct");
            } else {
                console.log(`no, incorrect, ${expectedProduct} is needed`);
            }
        };