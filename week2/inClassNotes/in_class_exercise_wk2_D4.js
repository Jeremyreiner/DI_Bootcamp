// //--------------------------------------Day 4 ------------------------------------------------------------

// // // I want to go through the colors array, and print each letter of each color
// // colors.join(" , ")
// // // 1. Do I need one or more loops?
// // two loops. need to cycle through the array, and then through the array items
// // // 2. Which type of loop is needed?
// // for loop needs to go through the array
// // // 3. What is the logic inside the loop?
// // split the array item to a string and seperate by comas, the item is inside "colors"
// let colors = ["blue", "red", "yellow", "lightblue"];

// //the first for loop goes over the array 
// for (let index = 0; index < colors.length; index++ ){
//     console.log("in the for loop: ")
//     console.log("index: ", index);
//     console.log("color: ", colors[index]);
//     console.log("color length: ", colors[index].length)
//     //the second loop whil go over each color
//     for (let index_letter = 0; index_letter < colors[index].length; index_letter++){

//         console.log(`in the nested loop for:  ${colors[index][index_letter]}`);
        
    
//     }


// // }
// //----------------------------------------------------------------------------------------------------




// //the first for loop goes over the array 
// for (let index = 0; index < colors.length; index++ ){
//     console.log("in the for loop: ")
//     console.log("index: ", index);
//     console.log("color: ", colors[index]);
//     console.log("color length: ", colors[index].length)
//     //the second loop whil go over each color
//     for (let index_letter = 0; index_letter < colors[index].length; index_letter++){

//         console.log(`in the nested loop for:  ${colors[index][index_letter]}`);
        
//     }
// }
// //-------------------------------------building a function-------------------------------------
// // declaring a function (argument)

//     function 

// // invoking/ calling a function (syntax )

//     function name_of_function( "parameter" ){
//             console.log(`Welcome ${parameter}`)
//     }

// name_of_function("username " ) //<-- is equal to parameter
// //----------------------------------------------------------------------------------------------

//            // --parameters-------//
// function myPet (name, color, breed){
//     console.log(` ${name} is the name of my pet and her color is ${color}, she is a ${breed}`)
    
// }   //--------Parameters--------//
// myPet("Shasta", "brown", "mut")

// //----------------------------------------------------------------------------------------------

// let age = 27 //global scope
// let colors = ["blue", "green", "yellow"]


// function aboutMe (){
//     //localscope
//     let ageDoubled = age * 2    //doesnt exhists in global scope//
//     for(let color of colors){
//         // console.log(`my favorite color is ${colors[0]}, my age doubled is ${age*2}`) //only exhists in local scope but not the global scope
//         return ageDoubled;          // aboutMe = ageDoubled
//                                     // ageDoubled = age * 2
//         //if the variable ageDoubled is now the result of the function
//         //the function is now equal to the result
//     }
// }


// console.log(aboutMe()) //global scope
// //to use the return function you need to call the function in the console.log
// // because return makes the function = the return

// // ---------------------------------------------------------------------------

// function futureDate (year){
//     let newDate = year + 10
//     return newDate;
// }
// let dateSoon = futureDate(2000);

// console.log(`The year in ten years will be ${dateSoon}`)

// //--------------------------------------------------------------------------------

// let prices = [20, 12, 30];
// function pricesWithTaxes (){
//     // 1. go inside the array
//     // 2. get each price , multiply by 1.17
//     for (let i = 0; i<prices.length; i++){
//         prices[i] *= 1.17;
//     }
// }
// pricesWithTaxes();
// function getSum (currencyConversion) {
//     let sum = 0;
//     for (let i = 0; i<prices.length; i++){
//         sum += prices[i];
//     }
//     // sum of all the meals
//     sum = sum*currencyConversion;
//     return sum;
// }
// // 1. function that gives us the amount of tip we need to give
// // 2. sum * 0.1
// function getAmountTip (){
//     let question = parseFloat(prompt("what is the currency conversion"));
//     let sumMeal = getSum(question)
//     let tip = (sumMeal*0.1).toFixed(2)
//     // 1; return the value
//     return tip;
// }
// // take the tip and divide it by the number of meals
// function getAmountTipPerPerson () {
//     // 2. create a new variable,
//     // make it equal to the value returned by the function
//     let generalTip = getAmountTip();
//     let tipPerPerson = (generalTip/prices.length).toFixed(2);
//     console.log(tipPerPerson)
// }
// getAmountTipPerPerson()


//-----------------------------------------------------DAY 5------------------------------------------------------------------

function testNumber(number){
    if (number === 0) {
        //return stops the execution of the function within the if / else loop
        return;
    }
    else {
        console.log("The number is : ", number)
    }
    //nothing tells the code to stop outside of the if/ else loop
    console.log("outside the IF statement")
}
//will return the first console log within the if, as well as the console log outside of the if statement
testNumber(2)

for (i = 0; i <= 2; i++){
    if (i==1){
        console.log("problem")
        //break will force to leave the if loop
        break;
        ////will continue the code within the loop the opposite of break;
        //continue;
    }
    else{
        console.log("great")
    }
    console.log("test")
}
//------------------first loop
//------------------i=0
//------------------i<=2
//------------------0= "great"
//------------------"test"
//------------------
//------------------second loop
//------------------i=1
//------------------i<=2
//------------------1= "problem"
//------------------"test"

//the for loop will run i == 0  and continue the if loop, once i ==1,
// the break will force the loop to break.
// console.log leaves at 1 = "problem"
