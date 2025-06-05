function start() {
    let walletMoney = 1500;
    let chocolatePrice = 8;
    let numberOfChocolates = Math.floor(walletMoney / chocolatePrice);
    let totalCost = numberOfChocolates * chocolatePrice;
    let leftamount = walletMoney - totalCost;

    console.log("Initial wallet money : "+walletMoney +" Rubols");
    console.log("Price per chocolate bar : "+chocolatePrice +" Rubols");

    console.log("Total chocolate buy : "+numberOfChocolates +" pieces");
    console.log("Change amount will be : "+totalCost +" Rubols");
    console.log("Left in wallet : "+leftamount +" Rubols");
}