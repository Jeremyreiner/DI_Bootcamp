/*EXERCISE 1*/
/*Find the word “Nemo”*/

/*Console.log a string as follows: "I found Nemo at [the position of the word Nemo]!".

Bonus : If you can’t find Nemo, console.log “I can’t find Nemo”.*/




let sentence = prompt("type a sentence using the word NEMO: ");

let id = sentence.indexOf("nemo")

if (id = sentence.includes("nemo")){
	let newSentence = prompt("i found nemo at " + id + "!")
}
else {
	let newSentence = prompt("I cant find nemo")
}

console.log(neSentence)






/*
Exercise 2 : Evaluation(2)
Instructions
Evaluate the code below. what would be the outcome if you run the code in the Javascript Console.
Answer the questions below then check them line by line in the console.
*/
    let c;
    console.log(c)		//: undefigned value


    let a = 34;
     console.log(a) 	//34


    let b = 21;			//a + b =  23
    a = 2;
    a + b

    console.log(a + b)	


    console.log(3 + 4 + '5'); 	//75

/*What will be the outcome of a + b?
What is the value of c?
Analyse the code below what will be the outcome?
console.log(3 + 4 + '5');*/



  



/*Exercise 3 : Ask For Numbers
Instructions
Ask the user for a string of numbers separated by commas, console.log the sum of the numbers.
Hint: use some string methods

Examples
"2,3"➞ 5

*/
let  str = prompt(parseInt("Enter in a string of numbers separated by comas: "))
let array = str.split (",")







/*
Exercise 4 : Boom
Instructions
Hint: if statement (tomorrow’s lesson)

Prompt the user for a number. Depending on the users number you will return a string of the word “Boom”. Follow the rules below:

If the number given is less than 2 : return “boom”
If the number given is bigger than 2 : the string should include n number of “o”s (n being the number given)
If the number given is evenly divisible by 2, add a exclamation mark to the end.
If the number given is evenly divisible by 5, return the string in ALL CAPS.
If the number given is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
Examples
4 ➞ "Boooom!"
There are 4 "o"s and 4 is divisible by 2 (exclamation mark included)
1 ➞ "boom"
1 is lower than 2, so we return "boom"*/

let num = prompt(parseInt("Enter in a number value: "))

