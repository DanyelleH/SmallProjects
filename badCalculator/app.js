let allResult =[]; //Result are saved here after moving on to add another value.
let add = false;
let subtract=false;
let multiply = false;
let divide = false;
document.querySelector('#one').addEventListener('click',toDisplay);
document.querySelector('#two').addEventListener('click', toDisplay);
document.querySelector('#three').addEventListener('click',toDisplay);
document.querySelector('#four').addEventListener('click', toDisplay);
document.querySelector('#five').addEventListener('click', toDisplay);
document.querySelector('#six').addEventListener('click',  toDisplay);
document.querySelector('#seven').addEventListener("click", toDisplay);
document.querySelector("#eight").addEventListener("click", toDisplay);
document.querySelector('#nine').addEventListener("click", toDisplay);
document.querySelector("#zero").addEventListener("click", toDisplay);
document.querySelector("#add").addEventListener("click", addition);
document.querySelector("#subtract").addEventListener("click", difference);
document.querySelector("#divide").addEventListener("click",quotient);
document.querySelector("#multiply").addEventListener("click", product);
document.querySelector("#clear").addEventListener("click",clearAll);
document.querySelector("#equals").addEventListener("click", equalsFunction);


function toDisplay() {
  let currentValue = document.querySelector(".Display").innerText 
// every time a value is inputted into the calculator, it is added to the inner text of the display class.
  let value = this.innerText
  document.querySelector(".Display").innerText = currentValue + value
}



function addition(){
  allResult.push(document.querySelector(".Display").innerText)
  //push whatever value is showing on the disply to the allValues list.
  document.querySelector(".Display").innerText = '';
  // clear the value from the screen after it is stored in allValues
  add=true; // tracks what function is currently being utilized.
  //**enter function to do calculations */
  }

function difference() {
  allResult.push(document.querySelector(".Display").innerText)
  document.querySelector(".Display").innerText = ''
  subtract=true
  }


function quotient() {
  allResult.push(document.querySelector(".Display").innerText)
  document.querySelector(".Display").innerText = ''
  divide = true
  }

function product(){
  allResult.push(document.querySelector(".Display").innerText)
  document.querySelector(".Display").innerText = ''
  multiply = true
  }


function clearAll(){
  document.querySelector(".Display").innerText='';
  allResult=[];
  add=subtract=divide=multiple=false;
}

function equalsFunction() {
  const secondNumber = document.querySelector(".Display").innerText
  if (add) {
    let result = Number(allResult[0]) + Number(secondNumber)
    document.querySelector(".Display").innerText = Number(result)
    allResult = [result];
    add=false
  }
  if (subtract){
    let result = Number(allResult[0]) - Number(secondNumber)
    document.querySelector(".Display").innerText = Number(result)
    allResult = [result];
    subtract=false
  }
  if(divide) {
    let result = Number(allResult[0]) / Number(secondNumber)
    document.querySelector(".Display").innerText = Number(result)
    allResult = [result];
    divide=false
  }
  if (multiply) {
    let result = Number(allResult[0]) * Number(secondNumber);
    document.querySelector(".Display").innerText = Number(result)
    allResult = [result];
    multiply = false
  }
}