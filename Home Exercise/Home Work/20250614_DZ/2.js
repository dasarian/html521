    window.addEventListener(
 'load',
 (event) => {
    let ol = document.createElement('ol')
document.body.appendChild(ol)
let li = document.createElement('li')
ol.appendChild(li)
li.textContent = 'Текст элемента списка'
li = document.createElement('li')
ol.appendChild(li)
li.textContent = 'Текст второго элемента списка'
    }
);