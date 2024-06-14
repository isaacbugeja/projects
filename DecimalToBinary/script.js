const numberInput = document.getElementById('number-input');
const convertBtn = document.getElementById('convert-btn');
const result = document.getElementById('result');
const animationContainer = document.getElementById('animation-container');

const checkUserInput = () => { /*If statement that checks if numberInput is NOT true (aka empty) OR parseInt of numberInput is Not a Number (isNaN) OR if parseInt(numberInput) is less than 0*/
    const inputInt = parseInt(numberInput.value);
    if (!numberInput.value || isNaN(inputInt) || inputInt < 0) {
        window.alert("Please provide a decimal number greater than or equal to 0"); /*Create alert window*/
        return;
    }
    result.textContent = decimalToBinary(inputInt); /**/
    numberInput.value = ""; /*This is to clear the numberInput field when conversion has happened*/

};

const decimalToBinary = (input) => {

    if (input === 0 || input === 1) {
        return String(input);
    }
    else {
        return decimalToBinary(Math.floor(input / 2)) + (input % 2);
    }
};

/**Event Listeners */

convertBtn.addEventListener("click", checkUserInput);

numberInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        checkUserInput();
    }
});