//1. In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation,
// using the setAttribute method.
// let divId = document.getElementById("navBar") 
// divId.setAttribute("id", "socialNetworkNavigation")
//2 We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// Create a new text node with “Logout” as its specified text.
// Append the text node to the newly created list node (li).
//3. Finally, append this updated list node to the unordered list above, using the appendChild method.
// Bonus


// //new variable that grabs the first place inside of the unordered list
// let ul1 = document.getElementsByTagName("ul")[0]
// //new variable that creates an element li
// let newLi =document.createElement("li")
// //new variable a that creates an anchor tag
// let a = document.createElement("a")
// //setting a new attribute tag for href inside of the anchor tag
// a.setAttribute("href", "")
// //giving the anchor tag inner text
// a.innerText = "log Out"
// //uploading the anchor tag inside of the new list element
// newLi.appendChild(a)
// //uploading the new list element inside of the unordered list
// ul1.appendChild(newLi)

// Use the firstElementChild and the lastElementChild properties to retrieve the first
// and last li elements from their parent element (ul). Display the text of each link. (Hint: use the textContent property).
// let ul = document.body.children[0].firstElementChild;
// let firstLi = ul.firstElementChild
// console.log(firstLi)
// let lastLi = ul.lastElementChild
// console.log(lastLi)
//----------------------------------------------------------------------------------------------------------------------
// Exercise 2 : Users
// // In the HTML above change the name “Pete” to “Richard”.
// //creating new variable inside of document selecting all the lists at index 1
// let accessUl = document.querySelectorAll("li")[1]
// console.log(accessUl)
// //reassigning at access Ul an inner text "Richard".
// let newName = accessUl.innerText = "Richard"
// console.log(newName)

// // Change each first name of the two <ul>'s to your name.
// //making a variable of all the elements that are part of class list
// let list = document.querySelectorAll(".list");
// // for x value of list
// for(let x of list){
//     //x of lists first element whild will have the text jeremy inserted inside
//     x.firstElementChild.textContent ="Jeremy"
    
// }

// // At the end of each <ul> add a <li> that says “Hey students”.
// //making a variable of all the elements that are part of class list
// for (let y of list){
//     //creat a new element li tag inside of document
//     let newLi = document.createElement("li")  
//     //give the new element text content
//     newLi.textContent = "Hey Students";
//     //re-inserting the new list element back into y of lists
//     y.appendChild(newLi)      
// }
// // Delete the name Sarah from the second <ul>.
// let liElement2 = document.body.children[2];
// console.log(liElement2);
// liElement2.removeChild(liElement2.children[1])

// Bonus
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.
//-------------------------------------------------------------------------------------
// Exercise 3 : Users And Style
// Instructions
// Bonus: If the background color of the div is “light blue”,
// alert “Hello x and y” (x and y are the users in the div

//----------------------------------------------------------------------------------------------
// Add a “light blue” background color and some padding to the <div>.
let div = document.getElementsByTagName("div")[0];
console.log(div)
//make a variable inside of div and insert css style background color
let divColor = div.style.backgroundColor = "lightblue"
console.log(divColor)
//make a variable for inside of the div class that style padding is 5px
let divPadding = div.style.padding = "5px"
console.log(divPadding)
// Do not display the first name (John) in the list.
//inside of the document body and first index of children
// let liElement2 = document.body.children[1];
// console.log(liElement2);
// //inside of the first index of children remove the 0th index of list items.
// liElement2.removeChild(liElement2.children[0])
// Add a border to the second name (Pete).
let liPete = document.getElementsByTagName("li")[0];
console.log(liPete)
// variable for styling border to the li item pete
let liBorder = liPete.style.border = "2px solid black"
console.log(liBorder)
// Change the font size of the whole body.
document.body.style.fontSize = "50px"
//locating the li element inside of the document bodies childs first index, and the first index childs 0th index
let liElement0 = document.body.children[1].children[0];
console.log(liElement0)
//locating the li element inside of the document bodies childs first index, and the first index childs first index
let liElement1 = document.body.children[1].children[1];
console.log(liElement1)
