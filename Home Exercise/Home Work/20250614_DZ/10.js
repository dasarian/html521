function calculateAge() {
      let birthYearInput = document.getElementById("birthYear");
      let birthYear = birthYearInput.valueAsNumber;
      let currentYear = new Date().getFullYear();
      let age = currentYear - birthYear;

      let ageResultParagraph = document.getElementById("ageResult");
      ageResultParagraph.textContent = "Your age: " + age;
    }