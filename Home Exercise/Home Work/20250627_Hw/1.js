/**
 *  Найти номер, на котором расположена буква P
 */
const imya = `TOP`
let bukva_nomer = 0
while (bukva_nomer < imya.length) {
 // imya - вся строка
 // imya[bukva_nomer] - буква под номером bukva_nomer
 if (imya[bukva_nomer] == 'P') {
        console.log ('P расположено на позиции ', bukva_nomer)
 }
    bukva_nomer  ++
}