function bargain(sellerPrice, buyerPrice) {
    while (sellerPrice > buyerPrice) {
        sellerPrice -= 500;
        buyerPrice += 600;
    }
    return sellerPrice;
}

const initialSellerPrice = 10000;
const initialBuyerPrice = 4000;
const finalPrice = bargain(initialSellerPrice, initialBuyerPrice);
console.log(`The bouquet will be purchased for: ${finalPrice}`);