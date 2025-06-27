window.addEventListener(
 'load',
 (event) => {
 // Здесь можно начинать пользоваться ресурсами страницы - они готовы
 // Создаём элемент:
 let my_button = document.createElement('button')
 my_button.textContent='я кнопка';
 // Прикрепляем его к телу страницы:
 document.body.appendChild(my_button);
 
 // Создаём элемент текста
 let my_text = document.createTextNode('текст ');
 // Прикрепляем её к телу страницы:
 document.body.appendChild(my_text);

 // Создаём абзац
 let my_p = document.createTextNode('p');
 my_p.textContent = 'Что-то на сложном'
 // Прикрепляем его к телу страницы:
 document.body.appendChild(my_p);
 

let ol = document.createElement('ol')
document.body.appendChild(ol)
let li = document.createElement('li')
ol.appendChild(li)
li.textContent = 'Пришёл посетитель'
let i = document.createElement('li')
ol.appendChild(i)
i.textContent = 'Пришёл посетитель'
let l = document.createElement('li')
ol.appendChild(l)
l.textContent = 'Пришёл посетитель'
 li = document.createElement('li')
ol.appendChild(li)
li.textContent = 'Пришёл посетитель'
 }
);