// Exercise 1 : Is_Blank
// Instructions
// Write a program to check whether a string is blank or not.

// console.log(isBlank('')); --> true
// console.log(isBlank('abc')); --> false
//---------------------------------------------------------------

// let myString = "";
// if (myString != ""){
//     console.log("False")
// }else{
//     console.log("True")
// }

//----------------------------------------------------------------------------------------------
// Exercise 2 : Abbrev_name
// Instructions
// Write a JavaScript function to convert a string into an abbreviated form.

// console.log(abbrevName("Robin Singh")); --> "Robin S."
//----------------------------------------------------------------------------------------------

// let myString = "Robin Singh";
// function abbreviated (){
//     //splits the string from the space
//     let namesList = myString.split(" ");
//     //the first word equals the first indexed item from the list and the 0th index of the first word is the first letter
//     let firstLetter = namesList[1][0];
//     console.log(namesList[0] + " " + firstLetter + ".")
// }
// abbreviated()





//---------------------------------------------------------------------------------------
// Exercise 3 : SwapCase
// Instructions
// Write a JavaScript function which takes a string as an argument and swaps the case of each character.
// For example :

// if you input 'The Quick Brown Fox' 
// the output should be 'tHE qUICK bROWN fOX'.
//------------------------------------------------------------------------------------------

// let inputString = 'The Quick Brown Fox';
// let letter;
// let newString = "";
// let newLetter;
// for (let i = 0; i < inputString.length; i++){
//     //letter is index of the inputString
//     letter = inputString[i];
//     // if the letter is equal in type or value to uppercase letters
//     if (letter === letter.toUpperCase()) {
//         //we create a new string and change uppercase to lower case and add it to a new string
//         newLetter = letter.toLowerCase();
//         //we create a new string and add a newLetter to it. creating a new string with reversed letters
//         newString = newString + newLetter;
//     }
//     //if the letter is equal in type/value to lowercase letters
//     else if (letter === letter.toLowerCase()){
//         //we create a new string and change lowercase to uppercase and add it to a new string
//         newLetter = letter.toUpperCase();
//         //we create a new string and add a newLetter to it. creating a new string with reversed letters
//         newString = newString + newLetter;
        
//     }else{
//         //if not upper or lower case make a space
//         newString = newString + " ";
//     }
// }
// console.log(newString);


//-----------------------------------------------------------------------
// Exercise 4 : Omnipresent Value
// Instructions
// Create a function that determines whether an argument is omnipresent for a given array.
// A value is omnipresent if it exists in every subarray inside the main array.
// To illustrate:

// [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]]
// // 3 exists in every element inside this array, so is omnipresent.
// Examples

// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1) ➞ true
// isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6) ➞ false
// ----------------------------------------------------------------------------
// function isOmnipresent(array, argument){
//     for(let i = 0; i < array.length; i++){
//         //sub array = new array, array[i] is an array within a array
//         let subArray = array[i];
//         //inArray new variable equals the subArray and includes the parameter argument
//         let inArray = subArray.includes(argument);
//         //if inArray is not true
//         if (inArray != true){
//             return "false";
//         }
//     }
//     return "true";
    
// }
// let array = [[3, 4], [8, 3, 2], [3], [9, 3], [5, 3], [4, 3]];
// let argument = 3;
// console.log(isOmnipresent(array, argument));