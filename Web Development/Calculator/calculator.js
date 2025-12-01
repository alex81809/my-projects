// Calculator Logic
let input1 = '';
let operate = '';
let input2 = '';

// Number Input
function appendNumber(number) {
    input1 += number;
    document.getElementById('display').value = `${input2} ${operate} ${input1}`;
}

// Operation Input
function appendOperation(operation) {
    if (input1 === '') return;
    if (input2 !== '') {
        calculate();
    }
    operate = operation;
    input2 = input1;
    input1 = '';
    document.getElementById('display').value = `${input2} ${operate}`;
}

// Calculation
function calculate() {
    if (input2 === '' || input1 === '') return;
    let result;
    let prev = parseFloat(input2);
    let current = parseFloat(input1);

    switch (operate) {
        // addition
        case '+':
            result = prev + current;
            break;

        // subtraction
        case '-':
            result = prev - current;
            break;

        // multiplication
        case '*':
            result = prev * current;
            break;

        // division
        case '/':
            result = prev / current;
            break;
            return;
    }

    input1 = result.toString();
    operate = '';
    input2 = '';
    document.getElementById('display').value = input1;
}

// Reset Function
function clearDisplay() {
    input1 = '';
    input2 = '';
    operate = '';
    document.getElementById('display').value = '';
}
