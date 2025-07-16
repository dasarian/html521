const tam = (buttonElement) => {
    const form = buttonElement.closest('body'); 
    const inputValue = form.querySelector('#numberInput').value;
    if (inputValue === '5') console.log('Там 5');
};