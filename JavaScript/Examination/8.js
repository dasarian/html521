function generateList() {
            const input = document.querySelector('#numberInput');
            const list = document.querySelector('#numberList');
            const number = parseInt(input.value);
            
            list.innerHTML = ''; 
            
            if (!isNaN(number)) {
                for (let i = number; i >= 0; i--) {
                    const listItem = document.createElement('li');
                    listItem.textContent = i;
                    list.appendChild(listItem);
                }
                
                if (number === 5) {
                    console.log('Там 5');
                }
            }
        }