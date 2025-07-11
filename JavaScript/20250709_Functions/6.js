function removeElementById(id) {
            const element = document.getElementById(id);
            if (element) {
                element.remove();
                console.log(`Элемент с id "${id}" был удалён.`);
            } else {
                console.log(`Элемент с id "${id}" не найден.`);
            }
        }

        removeElementById("element2");