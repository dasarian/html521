// Получаем текущую дату
window.addEventListener(
 'load',
 (event) => {        
let currentDate = new Date();

        // Извлекаем год, месяц и день
        const year = currentDate.getFullYear();
        const month = currentDate.getMonth() + 1; // Месяцы начинаются с 0
        const day = currentDate.getDate();

        // Создаем заголовок
        const header = document.createElement('h1');
        header.textContent = 'Сегодняшняя дата';

        // Создаем абзац
        const paragraph = document.createElement('p');
        paragraph.textContent = `${year}, ${month}, ${day}`;

        // Добавляем заголовок и абзац на страницу
        document.body.appendChild(header);
        document.body.appendChild(paragraph);
        }
);