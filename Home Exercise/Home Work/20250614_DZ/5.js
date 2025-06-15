window.addEventListener(
 'load',
 (event) => {
// Переменная с датой рождения
  let birthdayDate = "29 октября 1988 года"; 

  // заголовок
  let h = document.createElement("h");
  document.body.appendChild(h);
  h.textContent = "День моего рождения";

  // абзац
  let p = document.createElement("p");
  document.body.appendChild(p);
  p.textContent = `Мой день рождения: ${birthdayDate}.`;
  
}
);