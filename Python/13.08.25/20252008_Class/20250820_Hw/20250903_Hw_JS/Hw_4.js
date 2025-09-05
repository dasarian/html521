function greetUser() {
    const name = document.getElementById('name').value;
    const birthYear = parseInt(document.getElementById('birthYear').value);
    const currentYear = new Date().getFullYear();
    const age = currentYear - birthYear;

let greeting;
if (age < 10) {
    greeting = `Привет, ${name}!`;
            } else if (age >= 10 && age <= 20) {
                greeting = `Здравствуйте, ${name}!`;
            } else {
                greeting = `Не подскажете, как вас по отчеству?`;
            }
            document.getElementById('greeting').textContent = greeting;
        }