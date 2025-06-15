window.addEventListener(
 'load',
 (event) => {
const table = document.createElement('table');
const row = document.createElement('tr');

    const cell1 = document.createElement('td');
    cell1.textContent = 'Ячейка 1';
    const cell2 = document.createElement('td');
    cell2.textContent = 'Ячейка 2';

    row.appendChild(cell1);
    row.appendChild(cell2);

    table.appendChild(row);

    document.getElementById('table-container').appendChild(table);
 }
);