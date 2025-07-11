function createButtons(N) {
            const container = document.getElementById('buttonsContainer');

            for (let i = 1; i <= N; i++) {
                const button = document.createElement('button');
                button.textContent = `Кнопка ${i}`;
                button.onclick = function() {
                    alert(`Нажата кнопка ${i}`);
                };
                container.appendChild(button);
            }
        }
        createButtons(5);