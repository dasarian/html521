function start () {
        const date = new Date();
        const minutes = date.getMinutes();
        const seconds = date.getSeconds();

        document.getElementById('firstNumber').value = minutes;
        document.getElementById('secondNumber').value = seconds;

        
            const firstNumber = parseInt(document.getElementById('firstNumber').value);
            const secondNumber = parseInt(document.getElementById('secondNumber').value);
            const userAnswer = parseInt(document.getElementById('userAnswer').value);
            const correctAnswer = firstNumber + secondNumber;

            const listItem = document.createElement('li');
            listItem.textContent = `${firstNumber} + ${secondNumber} = ${userAnswer} (правильный ответ: ${correctAnswer}, ${userAnswer === correctAnswer})`;
            document.getElementById('resultsList').appendChild(listItem);
        };