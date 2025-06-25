/**
 * 1. Создать ряд
 * 2. Прикрепить ряд к таблице
 * 3. Создать ячейку
 * 4. Прикрепить ячейку к РЯДУ
 * 5. В ячейке написа 2*2=4
 */
// 1. Создать ряд
let tr = document.createElement('tr')  // Внутри название элемента, который мы создаем
// 2. Прикрепить ряд к таблице
// КУДА присоединяем ЧТО
multbl.appendChild(   tr)
// к таблице по айдишнику присоединяем свежесозданный ряд
const max_num = 9
header.setAttribute('colspan', max_num)
let index = 1
while (index <= max_num ) {
// повторять, пока не достигнем 9
// 3. Создать ячейку
let td = document.createElement('td')
// 4. Прикрепить ячейку к РЯДУ
tr.appendChild(td)
td.textContent = index
index ++
}