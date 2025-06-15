function addMessage() {
      let message = document.createElement('p');
      message.id = 'message';
      message.textContent = "Двойной бигмак и колу!";
      document.body.appendChild(message);
    }

    let button = document.getElementById('myButton');
    button.addEventListener('click', addMessage);