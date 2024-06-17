const strInput = document.getElementById('number');
const convertBtn = document.getElementById('convert-btn');
const output = document.getElementById('output');

const checkUserInput = () => {
    const userInput = parseInt(strInput.value);
    if (isNaN(userInput)) {
        output.textContent = "Please enter a valid number";
        return;
    }
    if (userInput < 0) {
        output.textContent = "Please enter a number greater than or equal to 1";
        return;
    }
    if (userInput >= 4000) {
        output.textContent = "Please enter a number less than or equal to 3999";
        return;
    }
    output.textContent = `Your number ${userInput} converts to ${convertToRoman(userInput)}` ;
    strInput.value="";
};

const convertToRoman = (num) => {
    const romanNumerals = [
        { value: 1000, numeral: 'M' },
        { value: 900, numeral: 'CM' },
        { value: 500, numeral: 'D' },
        { value: 400, numeral: 'CD' },
        { value: 100, numeral: 'C' },
        { value: 90, numeral: 'XC' },
        { value: 50, numeral: 'L' },
        { value: 40, numeral: 'XL' },
        { value: 10, numeral: 'X' },
        { value: 9, numeral: 'IX' },
        { value: 5, numeral: 'V' },
        { value: 4, numeral: 'IV' },
        { value: 1, numeral: 'I' }
    ]
    let romanValue = ''
    for(let i = 0; i<romanNumerals.length; i++){
        while(num>=romanNumerals[i].value){
            romanValue += romanNumerals[i].numeral;
            num -= romanNumerals[i].value;
        }
    }
    return romanValue;

};

convertBtn.addEventListener('click', checkUserInput);
strInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        checkUserInput();
    }
});
