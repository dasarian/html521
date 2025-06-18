function compareValues() {
            // Get the values from the input fields
            const value1 = document.getElementById('input1').value;
            const value2 = document.getElementById('input2').value;

            // Compare the values
            if (value1 === value2) {
                console.log("equal!");
            } else {
                console.log("not equal!");
            }
        }