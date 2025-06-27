function check() {
    console.log(age.value)
    console.log(age.valueAsNumber)
    
    if (age.valueAsNumber >= 65) {
       console.log('Пенсиюнер')

    }
    if (age.valueAsNumber <= 18) {
       console.log('не работник')

    } else { 
        console.log('Работник')
    }
}