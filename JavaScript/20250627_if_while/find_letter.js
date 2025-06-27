/**
 *  Найти номер, на котором расположена буква P
 */
function find_letter() {
    const imya = word.value// `TOP`
    const my_letter = letter.value  // 'P'
    console.log(imya)
    let bukva_nomer = 0
    // ЛОЖЬ && ЛОЖЬ   == ЛОЖЬ
    // ЛОЖЬ && ИСТИНА == ЛОЖЬ
    // ИСТИНА && ЛОЖЬ == ЛОЖЬ
    // ИСТИНА && ИСТИНА == ИСТИНА
    while ((bukva_nomer < imya.length) && (imya[bukva_nomer] != my_letter)) {
        bukva_nomer  ++
    }
    if (bukva_nomer == imya.length) {
        console.log (`${my_letter} в предложенном слове отсутствует!`)
    } else  {
        console.log (`${my_letter} расположено на позиции ${bukva_nomer}`)
    }
}