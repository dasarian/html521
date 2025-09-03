const name = prompt("Введите ваше имя:");
const birthDateInput = prompt("Введите вашу дату рождения (в формате ГГГГ-ММ-ДД):");

const birthDate = new Date(birthDateInput);
const today = new Date();

let age = today.getFullYear() - birthDate.getFullYear();

if (today.getMonth() < birthDate.getMonth() || 
    (today.getMonth() === birthDate.getMonth() && today.getDate() < birthDate.getDate())) {
    age--;
}

if (age < 10) {
    alert(`Привет, ${name}!`);
} else if (age >= 10 && age < 20) {
    alert(`Здравствуйте, ${name}!`);
} else {
    const patronymic = prompt("Не могли бы вы назвать своё отчество?");
    alert(`Здравствуйте, ${name} ${patronymic}!`);
}