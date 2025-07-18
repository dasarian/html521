function checkInput() {
    const inputText = document.getElementById('userInput').value;
    
    if (inputText === 'хорошо') {
        console.log('Всё будет хорошо');
    } else if (inputText === 'нормально') {
        console.log('Всё будет нормально');
    } else {
        console.log('Введите "хорошо" или "нормально"');
    }
}