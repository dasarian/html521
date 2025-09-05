function checkPrice() {
            const price = parseFloat(document.getElementById('applePrice').value);
            if (isNaN(price) || price <= 0) {
                document.getElementById('result').textContent = "Пожалуйста, введите корректную цену.";
                return;
            }
            let message;
            if (price > 1000) {
                message = "Мне дорого";
            } else if (price >= 100) {
                message = "Мне 1 килограмм";
            } else {
                message = "Мне 5 кг";
            }
            document.getElementById('result').textContent = message;
        }