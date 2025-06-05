const exchangeRate = 0.87; // 1 Dollar = 0.87 Euros

function convertDollarsToEuros(dollars) {
    return dollars * exchangeRate;
}

// Example usage:
const dollars = 100;
const euros = convertDollarsToEuros(dollars);
console.log(`${dollars} dollars are ${euros} euros.`);