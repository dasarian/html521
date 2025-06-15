document.getElementById('submitButton').addEventListener('click', function() {
const orderValue = document.getElementById('orderInput').value;
const orderDisplay = document.getElementById('orderDisplay');
const orderParagraph = document.createElement('p');
orderParagraph.textContent = orderValue;
orderDisplay.appendChild(orderParagraph);
});
                                                                           