 let p = document.createElement('p')
        document.body.appendChild(p)
        p.textContent = 'Текст вашего абзаца'
        // Второй раз для переменной мы не пишем let!
        // Переменную можно переиспользовать
        p = document.createElement('p')
        document.body.appendChild(p)
        p.textContent = 'Текст другого абзаца'