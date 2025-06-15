window.addEventListener(
 'load',
 (event) => {
let h2_1 = document.createElement('h2');
h2_1.textContent = 'Заголовок 1';
document.body.appendChild(h2_1);

let p1 = document.createElement('p');
document.body.appendChild(p1);
p1.textContent = 'Текст вашего абзаца';

let h2_2 = document.createElement('h2');
h2_2.textContent = 'Заголовок 2';
document.body.appendChild(h2_2);

let p2 = document.createElement('p');
document.body.appendChild(p2);
p2.textContent = 'Текст другого абзаца';
 }
);