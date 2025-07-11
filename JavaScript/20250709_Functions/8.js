function addRow() {
      let name = document.getElementById("name").value;
      let price = parseFloat(document.getElementById("price").value);
      let quantity = parseInt(document.getElementById("quantity").value);
      let sum = price * quantity;

      if (isNaN(price) || isNaN(quantity) || name.trim() === "") {
        alert("Пожалуйста, введите корректные значения для всех полей.");
        return;
      }


      let table = document.getElementById("myTable").getElementsByTagName('tbody')[0];
      let newRow = table.insertRow(table.rows.length);
      let cell1 = newRow.insertCell(0);
      let cell2 = newRow.insertCell(1);
      let cell3 = newRow.insertCell(2);
      let cell4 = newRow.insertCell(3);

      cell1.innerHTML = name;
      cell2.innerHTML = price.toFixed(2);
      cell3.innerHTML = quantity;
      cell4.innerHTML = sum.toFixed(2);

    
      document.getElementById("name").value = "";
      document.getElementById("price").value = "";
      document.getElementById("quantity").value = "";
    }