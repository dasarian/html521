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