// Create a structured HTML file linked to a JS file

// 1. Write a JavaScript for loop that will iterate from 0 to 15. For each iteration, it will check if the current number is odd or even, and display a message to the screen.

// Sample Output: //"0 is even" //"1 is odd" //"2 is even"

// for (let i = 0; i <  15; num++){
//     if( i%2 === 0){
//         console.log(`${i} is even` )
//     }
//        else {
//         console.log(`${i} is odd`)
//     }

//     }

// --------------------------------------------------------------------------------------------------------

    // let shopping = [
    //     {
    //     apple: 2,
    //     banana: 4,
    //     melon: 10
    // },
    // {
    //     mango: 6,
    //     orange: 1,
    //     pear: 13
    // }
    // ]
    // console.log(shopping)

    // for (let index=0; index <= shopping.length; index ++){
    //     console.log(shopping[index])
    // }
// ----------------------------------------------------------------------------------------------

// let shopping = ["apple", "pear", "melon", "banana"];
// 1. Loop over this array, and add to the array the word in plural ("s" at the end) of every fruit

// let shopping = ["apple", "pear", "melon", "banana"];

// for (let index = 0; index < shopping.length; index++){
    // shopping[index] = shopping[i] + "s"          is the same thing
//     shopping[index] += "s"
  
// }
// console.log  has to be outside of the scope because you only want to return the final edit of the for loop
// console.log(shopping)

// ----------------------------------------------

let prices = [22, 45 ,55 ,66 ,77]
let sum = 0;

for (let i = 0; i < prices.length; i++){
    sum += prices[i]
// 1st loop
// i=0
// i<4 => truesum
// sum += 22
// sum = 22
// 2nd loop
// i=22
// i < 4 => true
// 22 += 45
// sum = 67
//3rd loop adds 55... etc
    // }
    console.log(sum)



    //---------------------------using for of iside less in arrays-------------------------------

// let colors = ["blue", "yello", "red"]
//in a for in loop
//using an array
// for (let index of colors){

//     console.log(index);
//     console.log(colors[index])
// }
//--------or this also works for finding an element from an array
// for (let element of colors){
//     console.log(element);
// }





// ----------using for in if using objects---------
// let person ={
    //element: "value"


//     fname:"jon",
//     lname: "doe"
// }


// for(let element in person){
//     console.log(person[element])
// }


// ------------------while loops----------

let count = 3
while (count < 10) {
    console.log(count);
    count += 2
}