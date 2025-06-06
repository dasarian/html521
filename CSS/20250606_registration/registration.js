function addVisitor() {
    const nameInput = document.getElementById('name');
    const ageInput = document.getElementById('age');
    const visitorList = document.getElementById('visitorList');

    const listItem = document.createElement('li');
    
    listItem.textContent = `Имя: ${name1.value}, Возраст: ${age.value}`;
    
    visitorList.appendChild(listItem);
  
    nameInput.value = '';
    ageInput.value = '';

    nameInput.focus();
}