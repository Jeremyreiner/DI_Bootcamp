// Instructions
// Part I

// Create a function called infoAboutMe() that takes no parameter.
// The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
// Call the function.
//-----------------------------------------------------------------------------------------


// function infoAboutMe(name, age, hobbies){
//     console.log(`Hello, im ${name} and im ${age}, in my spare time i like to go ${hobbies}`)
// }
// infoAboutMe("Jeremy", "27", "Skiing")


//--------------------------------------------------------------------------------------------
// Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
// The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
// Call the function twice with the following arguments:
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

//---------------------------------------------------------------------------------------------------
//Part II

// function infoAboutPerson(pName, pAge, pColor){
//     console.log(`${pName}, you are ${pAge}, and your favorite color is ${pColor}`)
// }
// infoAboutPerson("David", "45", "blue")
// infoAboutPerson("Josh", "12", "yellow")

//--------------------------------------------------------------------------------------------------------
// Part III

// Add a parameter personHobbies to the function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies).
// The function should
// console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
// console.log the person’s hobbies one by one (ie. loop through the array of hobbies).
// Call the function twice with the following arguments:
//----------------------------------------------------------------------------------------------------
// infoAboutPerson("David", 45, "blue", ["tennis", "painting"])
// infoAboutPerson("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"])

// function infoAboutPerson(personName, personAge, personFavoriteColor, personHobbies){
//     console.log(`Your name is ${personName}, you are ${personAge}, your favorite color is ${personFavoriteColor}, and your hobby is ${personHobbies}`)
//     for (let i=0; i < personHobbies.length; i++){
//         console.log(personHobbies[i])
//     }

// }


//-------------------------------------------------------------------------------------------------------------
// Exercise 2 : Keyless Car
// Instructions
// Ask the user for their age, and save the value to a variable.
// Create a function called checkDriverAge() that will notify the user if they are permitted to drive. They must be at least 18 to drive.
// if the user is too young, alert “Sorry, you are too young to drive this car. Powering off”
// if the user is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
// if the user just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”
// Call the function.
// Instead of using prompt to ask the user for their age, have the checkDriverAge() function accept an argument age.
//----------------------------------------------------------------------------------------------------------------




//function alerts driver if he can drive
// function checkDriversAge(age){
//     if (age < 18){
//     console.log(`Sorry, you are not old enough to drive this car. Powering off`)
//     }
//     else if(age > 18){
//         console.log("You are old enough to checkDriversAge, Powering onabort. Enjoy the ride!")
//     }
//     else{
//         console.log("Congratulations on your first year of driving. Enjoy the ride!")
//     }
// }
// checkDriversAge(15)

//------------------------------------------------------------------------------------------------------
// Exercise 3: Odd Or Even
// Instructions
// Create a function called checkNumber() that takes no parameter.
// In the function, loop through numbers 0 to 100.
// Add an if/else block
// If the number is even, console.log "the number <number> is even"
// Else, console.log "the number <number> is odd"
// Call the function
//-----------------------------------------------------------------------------------

// function checkNumber(num){
//     //loops through numbers 1-100
//     for(num = 0; num <= 100; num++)
//     //if the number is even pring the number is even
//     if (num % 2 == 0){
//         console.log(`The number ${num} is even`)
//     }
//     //else print the number is odd
//     else{
//         console.log(`The numver ${num} is odd`)
//     }

// }
// checkNumber(22)

//------------------------------------------------------------------------
// Exercise 4: Find The Numbers Divisible By 23
// Instructions
// Create a function call isDivisible() that takes no parameter.
// In the function, loop through numbers 0 to 500.
// Console.log all the numbers divisible by 23.
// At the end, console.log the sum of all numbers that are divisible by 23.

// Outcome : 0 23 46 69 92 115 138 161 184 207 230 253 276 299 322 345 368
// 391 414 437 460 483
// Sum : 5313
//------------------------------------------------------------------------------
// function isDivisible(){
//     //make sum a variable starting at 0
//     let sum = 0
//     //loops from num 0 - 500
//     for(i=0; i < 500; i++){
//     //if  i is divisible by 23 logs the number 
//         if(i % 23 ===0){
//             //console.log the resulting divisible numbers of 23
//             console.log(`${i}`)
//         //returns the total sum of i
//         sum += i
//         }
//     }
//     //returns sum to the value of the function name sum = isDivisible
//     return sum;

// }
// //console.log the results of the function
// console.log(isDivisible())


//-------------------------------------------------------------------------------------------

// Exercise 5 : Amazon Shopping
// Instructions

// Create a function called checkBasket().
// It should:
// prompt the user for an item
// let the user know if the item is in the basket
// Hint: Use the in keyword inside the conditional
//-------------------------------------------------------------------------------
// object
// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }

// function checkBasket(){
//     // Prompt the user for an item
//     let item = prompt("Select an item.");

//     // object. hasownproperty(property)----
//     if(amazonBasket.hasOwnProperty(item)){
//         console.log(`${item} is in the basket`)
//     }
//     else{
//         console.log(`Your ${item} is not in the basket`)
//     }
// }
// checkBasket()


//--------------------------------------------------------------------------------------------

// Exercise 6 : What’s In My Wallet ?
// Instructions
// Given a item price and an array representing the amount of change in your pocket, determine whether or not you can afford the item.
// Change will always be represented in the following order: quarters, dimes, nickels, pennies.
// Quarters  = 0.25
// Dimes = 0.10
// Nickels = 0.05
// Pennies = 0.01
// To illustrate:
// changeEnough([25, 20, 5, 0], 4.25) should return true, since having 25 quarters, 20 dimes, 5 nickels and 0 pennies gives 
//                                     you 6.25 + 2 + .25 + 0 = 8.50 which is bigger than 4.25 (the total amount due)
// pocketChange =[25, 20, 5, 0]    //4.25
//--------------------------------------------------------------------------------------------------
let pocketChange = [25, 20, 5, 0];
let totalPrice = 4.65

// Is it divisible by only quarters?
let changeLeftAfterQuarters = (totalPrice * 100) % 25;

// Is there any change left over?
if (changeLeftAfterQuarters != 0) {
    // Is it divisible by quarters and dimes?
    changeLeftAfterDimes = changeLeftAfterQuarters % 10;

    if (changeLeftAfterDimes != 0) {
        // Is it divisible by quarters and dimes and nickels?
        changeLeftAfterNickels = changeLeftAfterDimes % 5;

        if (changeLeftAfterNickels != 0) {
            // Is it divisible by quarters and dimes and nickles and pennys?
            changeLeftAfterPennys = changeLeftAfterNickels % 1;

            if (changeLeftAfterPennies != 0) {

                let quarterCount = (changeLeftAfterPennies * 100) / 1;


            } else {
                //do we have enough pennies?
                console.log("False")
            }
        } else {
            // Do we have enough nickles?
            let quarterCount = (changeLeftAfterNickels * 100) / 5;
            // Do we have enough?
            
            if (pocketChange[0] > nickelCount) {
                console.log("True")
            }
        }

    } else {
        // How many dimes is needed?
        let dimeCount = (changeLeftAfterDimes) / 10;

        // Do we have enough?
        if (pocketChange[0] > dimeCount) {
            console.log("True")
        }
    }

} else {
    // How many quarters does it need?
    let quarterCount = (totalPrice * 100) / 25;

    // Do we have enough?
    if (pocketChange[0] > quarterCount) {
        console.log("True")
    }
}

//-----------------------------------------------------------------------------------------
//Exercise 7 : Shopping List
//Instructions
// Add the stock and prices objects to your js file.
// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”.
// It means that you have 1 banana, 1 orange and 1 apple in your cart.
// Create a function called myBill() that takes no parameters.
// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock.
// If the item is in stock find out the price in the prices object.
// Call the myBill() function.
// Bonus: If the item is in stock, decrease the item’s stock by 1

//---------------------------------------------------------------------------------------------------
// let stock = {
//     "banana": 6,
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry": 1
// }
// console.log(stock)

// let prices = {
//     "banana": 4,
//     "apple": 2,
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry": 10
// }
// console.log(prices)
// let shoppingList = ["banana", "orange", "apple"];

// //go inside array and add by price item
// function myBill(myPrices) {
//     //variable starts at 0
//     let totalPrices = 0;
//     // Calculate how much all my items cost all together
//     for (i = 0; i < myPrices.length; i++) {
//         //total prices will adjust as i is put through the for loop
//         totalPrices = totalPrices + myPrices[i];
//     }
//     //return to function
//     return totalPrices;
// }
// // for each item in shoppingList, 
// let item;
// let price;
// //my prices items are added to array as ran through for loop
// let myPrices = [];
// for (i = 0; i < shoppingList.length; i++) {
//     //new variable item is equal to the index of shopping list
//     item = shoppingList[i];
//     //see if the item is in stock
//     if (stock[item] != 0) {
//         // Find out the price in the prices object.
//         price = prices[item];
//         //list of prices will be pushed into an array
//         myPrices.push(price);
//         // Decrease the stock of the item by 1
//         stock[item] = stock[item] - 1;
//     }
// }
// //my bill will be array of prices
// console.log(myBill(myPrices));
// console.log(stock)



//---------------------------------------------------------------------------------
// Exercise 8 : Tips
// Instructions
// John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

// The calculator has the following rules:
// 1. Tip 20% when the bill is less than $50,
// 2. Tip 15% when the bill is between $50 and $200,
// 3. Tip 10% if the bill is more than $200.

// Ask John for the amount of the bill.
// Create the program explained above.
// In the end, John would like to know:
// Tip amount.
// Final bill (bill + tip).
// (NOTE: To calculate 20% of a value, simply multiply it with 20/100 = 0.2)
// -----------------------------------------------------------------------------------------
// let bill = parseInt(prompt("what is the total bill?"))
// //calculate how much to tip
// function finalTip() {
//     let tip = (bill * 0.2).toFixed(2)
//     return parseInt(tip);
// }
// console.log(finalTip())
// //find total bill with tip
// function finalBill() {
//     let totalBill = (bill + finalTip())
//     return totalBill;
// }
// console.log(finalBill())
// //create an if statement for the price of the meals
// if (totalBill = 0, totalBill < 50, totalBill++) {
//     let tip = (bill * .2).toFixed(2)
//     console.log(finalBill())
// }
// //if the total bill is between 50-200 the bill will be multipled by .15
// else if (totalBill = 50, totalBill < 200, totalBill++) {
//     let tip = (bill * .15).toFixed(2)
//     console.log(finalBill())
// }
// else {
//     let tip = (bill * 10).toFixed(2)
//     console.log(finalBill())
// }



//------------------------------------------------------------------------------------------------------------

// Exercise 9 : Vacations Costs
// Instructions
// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.

//---------------------------------------
// function hotelCost() {
//     //creating new variable nights which is defined inside the do/ while loop
//     let nights;
//     //runs auto first time and second while the while loop is true
//     do {
//         //prompts user for variable nights
//         nights = parseInt(prompt("How many nights are you staying in the hotel? "))
//         //runs as long as night is not a number or promp is submitted empty
//     } while (isNaN(nights) == true || nights == "");
//     //total cost
//     let totalCost = nights *= 140;
//     // return (alert(`The total cost of your hotel is ${totalCost}`));

//     return totalCost
// }
// // hotelCost()


// //--------------------------
// // The function should return a different price depending on the location.
// // All other destination : 300$
// // If the user doesn’t answer or if the answer is not a string, ask again.
// // Define a function called planeRideCost().
// //---------------------------------------------------------
// function planeRideCost() {
//     let finalDestination = {
//         london: 183,
//         paris: 220,
//     }
//     // It should ask the user for their destination.
//     let destination = prompt("What is your end destination")
//     //if city in finalDestination is equal in value and type to destination prompt
//     if (destination.includes("london")) {
//         //console.log( prompted destination is (keys: value) $)
//         console.log(`${destination} is ${finalDestination[`london`]}$. `);
//         return finalDestination[`london`];
//     }
//     else if (destination.includes("paris")) {
//         //console.log( prompted destination is (keys: value) $)
//         console.log(`${destination} is ${finalDestination[`paris`]}$. `);
//         return finalDestination[`paris`];
//     }
//     else {
//         console.log(`${destination} is 300$.`)
//         return 300
//     }
// }
// // // planeRideCost()

// //----------------------------
// // Define a function called rentalCarCost().
// // It should ask the user for the number of days they would like to rent the car.
// // If the user doesn’t answer or if the answer is not a number, ask again.
// // Calculate the cost to rent the car. The car costs $40 everyday.
// // If the user rents a car for more than 10 days, they get a 5% discount.
// // The function should return the total price of the car rental.

// //--------------------

// function rentalCarCost() {
//     // let rentalLength = parseInt(prompt(`For how many days would you like to rent a car?`));
//     let rentalLength;
//     do {
//         rentalLength = parseInt(prompt(`For how many days would you like to rent a car?`));
//     } while (isNaN(rentalLength) == true || rentalLength == "");

//     let rentalCost = rentalLength * 40;
//     let discountCost = rentalCost * .05;
//     let totalCost = rentalCost - discountCost;
//     //if the rentalLength isnt a number OR the rentalLength is less than 10
//     if (rentalLength < 10) {
//         //and re-adjust the rental cost inside the local scope
//         rentalCost = rentalLength *= 40;
//         console.log(`Your rental cost will be ${rentalCost}`);
//     }
//     //if the rentalLength is not a number OR the rentalLength is greater than 10
//     else if (rentalLength > 10) {
//         rentalCost = rentalLength *= 40;
//         // updated discount 
//         discountCost = rentalLength *= .05;
//         //new total cost
//         totalCost = rentalCost - discountCost;
//         //if the rentalLength is not a number
//         console.log(`Your rental car discount will be ${discountCost}, the discounted cost of your car will be ${totalCost}`);
//     }
//     return (totalCost)
// }
// // rentalCarCost()


// //-------------------
// // Define a function called totalVacationCost() that returns the total cost of the user’s
// // vacation by calling the 3 functions that you created above.
// // Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// // Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost.
// // Call the function totalVacationCost()
// // Bonus: Instead of using a prompt inside the 3 first functions, only use a prompt inside the totalVacationCost() function.

// //------------------------------------------------------------------------
// function totalVacationCost() {
//     // let rentalLength = parseInt(prompt(`For how many days would you like to rent a car?`))
//     let costRentalCar = rentalCarCost()
//     // let destination = prompt("What is your end destination")
//     let costPlaneTicket = planeRideCost()
//     // let nights = parseInt(prompt("How many nights are you staying in the hotel? "))
//     let costHotel = hotelCost()

//     console.log(`The plane ride will cost:${costPlaneTicket}, the hotel costs: ${costHotel}, and the rental car will cost: ${costRentalCar}`)

// }

// totalVacationCost()