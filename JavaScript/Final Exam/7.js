function checkInput() {
    const input = document.getElementById('userInput');
    const output = document.getElementById('output');
    const text = input.value.toLowerCase().trim();
    
    let message = '';
    
    if (text === 'хорошо') {
        message = 'Всё будет хорошо';
    } else if (text === 'нормально') {
        message = 'Всё будет нормально';
    } else {
        message = 'Пожалуйста, введите "хорошо" или "нормально"';
    }
    

    console.log(message);
    
   
    output.textContent = message;
    
    input.value = '';
}