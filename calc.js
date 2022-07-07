let completeButtons = document.getElementsByTagName("button");
let numbers = ["0","1","2","3","4","5","6","7","8","9","/","*","-","+","."];
let validnumbers = ["+", "-", "/", "*","."];
let onlyNumbersandOperation = [];
let elseNumbers = [];

  for (let x = 0; x < completeButtons.length; x++) {
    if (numbers.includes(completeButtons[x].textContent)) {
      onlyNumbersandOperation.push(completeButtons[x]);
    } else {
      elseNumbers.push(completeButtons[x]);
    }
  }

let current_command = "";
for (let x = 0; x < onlyNumbersandOperation.length; x++) {
  onlyNumbersandOperation[x].addEventListener("click", () => {
    let current_expression = onlyNumbersandOperation[x].textContent;
      current_command += current_expression;
      document.getElementById("display").value = eval(current_command);
      if (isNaN(current_command)) {
        current_command = eval(current_command);
  
      }
  });
}

for (let x = 0; x <= elseNumbers.length; x++) {
  elseNumbers[x].addEventListener("click", () => {
    if (elseNumbers[x].textContent == "C") {
      document.getElementById("display").value = "";
      current_command = "";
    } else {
      document.getElementById("display").value = eval(current_command);
  current_command = eval(current_command);
    }
  });
}

