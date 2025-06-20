(() => {
  const itemPrice = 4500;
  const walletAmount = 6000;

  const checkFunds = (price, amount) => {
    return amount >= price ? "достаточно" : "мало";
  };

  const result = checkFunds(itemPrice, walletAmount);

  console.log(result);
})();