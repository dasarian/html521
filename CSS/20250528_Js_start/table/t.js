window.addEventListener(
 'load',
 (event) => {
let table = document.createElement('table');

let row = document.createElement('tr');

let cell1 = document.createElement('td');
cell1.textContent = 'Ячейка 1';

let cell2 = document.createElement('td');
cell2.textContent = 'Ячейка 2';

row.appendChild(cell1);
row.appendChild(cell2);

table.appendChild(row);

document.getElementById('table-container').appendChild(table);
}
);