function checkInput() {
    const input = document.getElementById('userInput');
    const output = document.getElementById('output');
    const text = input.value.toLowerCase().trim();
    
    const now = new Date();
    const options = {
        day: 'numeric',
        month: 'long',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    };
    const timeString = now.toLocaleDateString('ru-RU', options);
    
    let message = '';
    if (text === 'хорошо') {
        message = 'Всё будет хорошо';
    } else if (text === 'нормально') {
        message = 'Всё будет нормально';
    } else {
        message = 'Пожалуйста, введите "хорошо" или "нормально"';
    }
    
    const fullMessage = `${timeString} ${message}`;
    
    console.log(fullMessage);
    
    const messageElement = document.createElement('div');
    messageElement.className = 'message';
    messageElement.textContent = fullMessage;
    output.insertBefore(messageElement, output.firstChild);
    
    input.value = '';
}