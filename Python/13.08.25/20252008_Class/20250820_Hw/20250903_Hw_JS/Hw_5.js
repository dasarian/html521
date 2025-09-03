let price = prompt("Сколько стоит килограмм яблок?");

if (price > 1000) {
  console.log("Мне дорого");
} else if (price >= 100 && price <= 1000) {
  console.log("Мне 1 килограмм");
} else {
  console.log("Мне 5 кг");
}
