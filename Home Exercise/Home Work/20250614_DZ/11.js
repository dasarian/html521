function checkSum() {
      let num1 = document.getElementById("num1").valueAsNumber;
      let num2 = document.getElementById("num2").valueAsNumber;
      let sumInput = document.getElementById("sumInput").valueAsNumber;
      let resultElement = document.getElementById("result");

      let isSumCorrect = (num1 + num2) == sumInput; 
      resultElement.textContent = isSumCorrect; 
    }