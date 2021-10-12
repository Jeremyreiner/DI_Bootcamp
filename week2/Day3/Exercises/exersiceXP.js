// Exercise 1 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

// ---------------------------
// let colors = ["blue", "red", "green", "yellow"]
// // // console.log(colors)

// for (i = 0; i < colors.length; i++) {
//     console.log("my #" + [i + 1] + "is" + colors[i]);
 
// }


// // // let colors = ["blue", "red", "green", "yellow"]
// let choices = ["st", "nd", "rd", "th"]

// for (s = 0; s < choices.length; s++) {
//     console.log("my" + [s + 1] + choices[s] )
// }
// // console.log("my" +  [s+1] + choices[s] +"is" + colors[i])
//
// ------------------------------------------------------------------
// Exercise 2 : List Of People
// Instructions
// let people = ["Greg", "Mary", "Devon", "James"]
// Write code to remove “Greg” from the people array.
// Write code to replace “James” to “Jason”.

// Write code to add your name to the end of the people array.
// Using a loop, iterate through the people array and console.log each person.

// Using a loop, iterate through the people array and after you console.log “Jason” exit the loop.
// Write code to make a copy of the people array using slice. The copy should NOT include “Mary” or your name.
// Write code that console.logs Mary’s index. take a look at indexOf on google.
// Write code that gives the indexOf “Foo” (this should return -1). Why does it return -1
// Create a variable called last which value is the last element of the array.

// Hint: What is the relationship between the index of the last element in the array and the length of the array?

//------------------------------------------------------------------
// const people = ["Greg", "Mary", "Devon", "James"];
// people.shift()
// people[2] = "Jason"
// people.push("jeremy")
// console.log(people)
// for (i = 0; i < people[2]; i++) {

//     // console.log("jason")
// }
// const people1 = people.slice(1, 3); 

// let last = people[3];
// console.log(last)
// // console.log(people.indexOf("mary"))
// // console.log(people.indexOf("foo")) //element not located in array index







// -----------------------------------------------------------------------------
// Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number, while the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?
// Hint : Check the data type you receive from the prompt (ie. typeof method)
//----------------------------------------------------------------


// let num = parseInt(prompt("Please enter a number: "));

// while (num < 10 ) {
//  num  = parseInt(prompt("enter another number: "))
// }
// console.log(num)








// --------------------------------------------------------
// Exercise 4 : Attendance
// Instructions
// Given the object above where the key is the students name and the value is the country they are from.

// Prompt the student for their name :
// If the name is in the object, console.log the name of the student and the country they come from.
// example: "Hi! I'm [name], and I'm from [country]."
// Hint: Look up the statement if ... in
// If the name is not in the object, console.log: "Hi! I'm a guest."
//---------------------------------------------------------------------------------



// let guestList = {
//   randy: "Germany",
//   karla: "France",
//   wendy: "Japan",
//   norman: "England",
//   sam: "Argentina",
// }

// let entered_name = prompt("What is your name? ");

// //["randy", "karla"...]
// let all_guest_names = Object.keys(guestList)

// // Determine if the entered_name exists in all_guest_names
// // https://masteringjs.io/tutorials/fundamentals/foreach-break

// all_guest_names.every(guest_name => {
//   let match = false;
//   if (entered_name === guest_name){
//     match = true; 
//     return false; // Exists the .every() loop
//   }
//   else(
//     return true;
//   )
// })

// if (match){
//   console.log(`Hi! I'm  ${guest_name}, and I'm from ${guestList[guest_name]}`)
// }
// else(
//   console.log("Hi! I'm a guest.")
// )



// 

//










// --------------------------------------------------------------
// Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Console.log the keys. (using a for loop).
// Console.log the values. (using a for loop).

// ------------------------------------
// let family = {
//   dad: "randy",
//   mom: "jules",
//   son: "hayden"
// }
// do {
//   console.log(Object.keys(family))

//   console.log(Object.values(family))
//   break;
// }
// while(family)






// ------------------------------------------------------------------------
// Exercise 6
// Instructions
// Given the object above, console.log “my name is Rudolf the raindeer”
// ------------------------------------



// let details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'raindeer'
// }
// let array = Object.keys(details)

// // let array2 = Object.values(details)
// // console.log(array2)

// console.log(`${array[0]} ${details['my']} ${array[1]} ${details['is']} ${array[2]} ${details['the']}`);



// let concat = array.concat(array2)
// // console.log(array)
// // console.log(array2)

// console.log(concat)









// ----------------------------------------------------------------------------
// Exercise 7 : Secret Group
// Instructions
// 
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society.


let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
console.log(names)
let str1 = names[0].charAt(0)
let str2 = names[1].charAt(0)
let str3 = names[2].charAt(0)
let str4 = names[3].charAt(0)
let str5 = names[4].charAt(0)
let str6 = names[5].charAt(0)
let first_letter = str1 + str2 + str3 +str4 +str5 + str6
// console.log(password)
let array = first_letter.split("")
// console.log(array)
let orderP = array.sort();
console.log(orderP)
// console.log(array)
let society_name_array = array.sort();
console.log(society_name_array)
let society_name = society_name_array.toString()
 society_name = society_name.replace(/,/g, "")
console.log(society_name)


