const handleButtonClick = (button) => {
        
            const input = button.previousElementSibling;
            const messageList = button.nextElementSibling;

            if (input.value === '5') {
                console.log('Там 5');
                messageList.innerHTML = `<li>Я тоже вижу значение 5</li>`;
            } else {
                messageList.innerHTML = `<li>Вы ввели ${input.value}, а не 5</li>`;
            }
        };