// Create a HTML file for your calculator and a JS file for the calculator’s functionality.
// You must create 3 functions in the js file:
// number(num)
// operator(operator)
// equal()
// Hint : you can use the eval() method to help with your calculations.
// Before coding, take your time to understand all the parts to the exercise and their process. You can write it down somewhere if it helps (recommended).
// Bonus : create the RESET and CLEAR buttons.
//-----------------------------------------------------------------------------------------------
//return a number with plus x
let currentValue = "";
function number(num){
    //will show number in string
    currentValue = currentValue + num.toString();
    //returns final value of number punch
    document.getElementById("result").value = currentValue;
}

//return a operator to the variables
let finalOperator = "";
let firstVal = "";
function operator(oper){
    if (oper === "."){
        //update currentValue number with a decimal at the end
        currentValue = currentValue + ".";
    }else{
        //only shows current number that is currently needed
        firstVal = currentValue;
        //take first value number plus operator. 
        finalOperator = oper;
        //currentValue resets the property to nothing after an operator is used
        currentValue = "";
        //inside of html doc find the element with an id value ""
        document.getElementById("result").value = "";
    }
    
}

//to combine the number and operator values
let secondVal = "";
function equal(operator){
    //only shows current number that is currently needed
    secondVal = currentValue;
    //if the value entered was not a number dont do anything
    if (isNaN(parseFloat(secondVal)) || isNaN(parseFloat(firstVal))){
    }
    else{
        // do the operation
        console.log(firstVal);
        console.log(finalOperator);
        console.log(secondVal);
        if (finalOperator === "+"){
            //inside of html doc find the element with an id value ""
            document.getElementById("result").value = parseFloat(firstVal) + parseFloat(secondVal);
        }
        else if (finalOperator === "-"){
            //inside of html doc find the element with an id value ""
            document.getElementById("result").value = parseFloat(firstVal) - parseFloat(secondVal);
        }
        else if (finalOperator === "*"){
            //inside of html doc find the element with an id value ""
            document.getElementById("result").value = parseFloat(firstVal) * parseFloat(secondVal);
        }
        else if (finalOperator === "/"){
            //inside of html doc find the element with an id value ""
            document.getElementById("result").value = parseFloat(firstVal) / parseFloat(secondVal);
        }
    }
}
//resets all values to starting point.
function reset(){
    //resets original variable back to ""
    finalOperator = "";
    firstVal = "";
    currentValue = "";
    secondVal = "";
    console.log("inside reset")
    //inside of html doc find the element with an id value ""
    document.getElementById("result").value = "";
}

//will clear screen at the point of time.
function clears(){
    console.log("Inside clear");
    currentValue = "";
    //inside of html doc find the element with an id value ""
    document.getElementById("result").value = "";
}
