/*Instructions
let me = ["my","favorite","color","is","blue"]
Write some simple Javascript code that will join all the items in the array above, and console.log the result.
*/
/*let me = ["my","favorite","color","is","blue"] ;
let str = me.join(' ')
//console.log(str)
console.log(me.join(' '))*/

/*Exercise 2 : Mixup
Instructions
Create 2 variables. The values should be strings. For example:
let str1 = "mix" let str2 = "pod"
Slice out and swap the first 2 characters of the 2 strings from part 1.
Create a third variable where the value is the concatenation of the two strings from the part 1 (separated by a space).
Finally console.log the new concatenated string.
Some Examples*/

let str1 = "mix"
let str2 = "pod" 
let str1new = str1.slice(2)
let str2new = str2.slice(2)
let str3 = "mi" + str2new
let str4 = "po" + str1new

console.log( str4 + " " + str3)

/*let newWord should be equal to 'pox mid'*/

/*let firstWord = "Hello"
let secondWord = "World"*/
/*let thirdWord should be equal to 'Worlo Helld'*/


let firstWord = "Hello"
let secondWord = "World"
let firstWord2 = firstWord.slice(4)
let secondWord2 = secondWord.slice(4)
let str1 = "worl" + firstWord2
let str2 = "hel" + secondWord2
console.log( str1 + " " + str2)




/*
Exercise 3 : Calculator
Instructions
Make a Calculator. Follow the instructions:*/

/*Prompt the user for the first number.
Store the first number in a variable called num1.
Prompt the user for the second number.
Store the second number in a variable called num2.
Create an Alert where the value is the SUM of num1 and num2.
BONUS: Make a program that can subtract, multiply, and also divide!*/

//Prompt the user for the first number.
let num1 = parseInt(prompt("What is your first number: "))

//Prompt the user for the second number
let num2 = parseInt(prompt("What is your second number: "))




 //sum the two numbers
let sum = num1 + num2;
let subtract = num1 - num2;
let divide = num1 / num2;
let multiply = num1 * num2;
let res;

let operator = prompt("which operation do you want: ")
 if(operator == "+"){
 	operator = sum;
 	 res = ("the sum of " + num1 + "and " + num2 + "is: " + sum)
 }
 else if(operator == "-"){
 	operator = subtract;
 	 res = ("the subtraction of" + num1 + "and" + num2 + "is: " + subtract)

 }
 else if(operator == "/" ){
 	operator = divide;
 	 res = ("the division of" + num1 + "and" + num2 + "is: " + divide)

 }
 else if(operator == "*") {
 	operator = multiply;
 	 res = ("the multiplication of" + num1 + "and" + num2 + "is: " + multiply)

 }
 else{
 	"You have entered incorrect operator.. Try again"
 }


prompt(res)
//alert the user of the result



//Make a program that can subtract, multiply, and also divide!


console.log()
