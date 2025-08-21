class Human {
    #firstname                   // приватное поле
    #birthday                    // поле
    constructor(newname, dt) {  // метод
        // аргументы, они же - параметры. При описании - формальные
        this.#firstname = newname  // 'Вася'
        this.#birthday = dt        // new Date(2000, 5, 2)
    }
    get name() {  // getter - обращение без круглых скобок!
        return this.#firstname
    }
    get birthday() {
        // return this.#birthday  // НЕБЕЗОПАСНО! Доступ к модификации даты по частям!
        return new Date(
            this.#birthday.getFullYear(),
            this.#birthday.getMonth(),
            this.#birthday.getDate()
        )
    }
    set birthday(new_bd) {
        if ((new_bd < new Date()) && (new_bd > new Date(1800, 0, 1))) {
            this.#birthday = new_bd
        } else {
            console.error('Неверная дата рождения: ', new_bd)
        }
    }
}

let man = new Human('Вася', new Date(1990, 2, 4))
// при вызове любой функции, даже метода, мы передаем ФАКТИЧЕСКИЕ параметры
let girl = new Human('Ася', new Date(1993, 6, 4))
let boy = new Human('Дима', new Date(2019, 10, 18))
// girl.#firstname = 'Миша' - нельзя! Поле приватное!
console.log(girl.name)
girl.birthday = new Date(2020, 5, 6)  // Молча ничего не делает!
console.log(girl.birthday)
girl.birthday.setMonth(0)
console.log(girl.birthday)

girl.birthday = new Date(2028, 8, 8)

console.log(girl.birthday)

/**
 * Написать класс Машина с конструктором и двумя полями: марка и количество колес.
 * Марка должна быть только на чтение, а сеттер количества колес не должен давать
 * присвоить меньше 4 колес, больше 20 и нечетное число.
 */
class Car {
    #brand
    #wheels
    constructor(brand, wheels) {
        this.#brand = brand
        this.wheels = wheels  // да, в конструкторе тоже удобно использовать свой сеттер!
    }
    get brand() {
        return this.#brand
    }
    get wheels() {
        return this.#wheels
    }
    /**
     * @param {number} new_wheels
     */
    set wheels(new_wheels) {
        if (new_wheels >= 4 && new_wheels <= 20) {
            if (new_wheels % 2 === 0) {
                this.#wheels = new_wheels
            } else {
                console.error("Количество колес должно быть четным, а не ", new_wheels)
            }
        } else {
            console.error("Количество колес должно быть от 4 до 20, а не ", new_wheels)
        }
    }
}

let c = new Car('Lada', 4)
console.log(c.brand, c.wheels)