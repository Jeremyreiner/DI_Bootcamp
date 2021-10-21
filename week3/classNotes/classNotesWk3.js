//-----------------------------------------------------WEEK 3 DAY 1------------USING DOM IN JS-------------------------------------------------------------------------------------------
//------------------------WINDOW-----------------------------------------------------
//------------------------<HTML>-----------------------------------------------------
//----------<HEAD>-----------------------------<BODY>--------------------------------
//------------------------------------------------------------------------------------
//----------<TITLE>------------------<H1>-----------------<SCRIPT>--------------------
//------------------------------------------------------------------------<TYPE = JS>
//--------<"MY TITLE">------------<"MY TITLE">-----------<"ALERT()">-----------------
//-----------------------------------------------------------------------------------
// //1 creating a paragraph in the dom
// let newParagraph = document.createElement("p")
// //2 add text in the paragraph
// let newText = document.createTextNode("my new DOM paragraph is...")
// //3.add the text to the paragraph
// newParagraph.appendChild(newText);
// //4. retrieve the parent
// let divParent = document.body.firstElementChild;
// //5. add paragraph to div
// divParent.appendChild(newParagraph);
//-------------------------------------------------------------------------------------
//HOW TO INSERT TEXT TO INTO A HTML PAGE USING THE DOM AND CREATE REACTIVE PAGE USING ".TEXTCONTENT"
// let person = {
//     username: "jon",
//     signIn: true,
// }
//  //if the user is signed in, add his name to the h1
//  if(person.signIn){
//      //1. retrieve the h1 from html
//      let title = document.body.firstElementChild;
//      //2. open the h1 content and add onto it the username. AE "title + ${person.username}"
//      title.textContent += `${person.username}`
//  }
 //-----------Accessing Elements------------------------------------------
// element.children[index]
// element.firstElementChild
// element.lastElementChild
// element.parentNode
// element.nextElementSibling
// element.previousElementSibling
// element.textContent
//---------------------------------------------------------------------------
//  For each of the questions, find 2 WAYS of accessing :
// // 1. The div DOM node?
//  let divItem = document.body.firstElementChild;
//  console.log(divItem)
//  let divItem2 = document.body.children[0];
//  console.log(divItem2)

// // // 2. The ul DOM node?
// let ul = document.body.children[1];
// console.log(ul)
// let ul1 = document.body.firstElementChild.nextElementSibling
// console.log(ul1)

// // 3. The second li (with Pete)?
// let li = document.body.children[1].children[0]
// console.log(li)
// let li1 =  document.body.firstElementChild.nextElementSibling.lastElementChild
// console.log(li1)
//-----------------------Accessing Nodes With Methods---------------------------------------------------------------------

// element.getElementById()
// element.getElementsByClassName()
// element.getElementsByTagName()
// element.querySelector()
//------------USING ID'S TO GET SPECIFIC ELEMENTS FROM OUR HTML FILE------------------------
// let retrieveById = document.getElementById("secondTitle")
// console.log(retrieveById)
// //gives you a collection of items even if it is singular
// let retrievebyTag = document.getElementsByTagName("li")[0]
// console.log(retrievebyTag)
// //returns the element that is specified by the ID container
// let divcontainer = document.getElementById("container")
// //returns the tag name h1 within the div container
// let allH1 = divcontainer.getElementsByTagName("h1")
// console.log(allH1)
// //returns the id of container 
// let divContainer = document.querySelector("#container")
// console.log(divContainer)
// //returns all the h1's inside of the id container
// //querySelector returns the first element that is inside of the element
// //if you want all you need to do querySelectorAll. This returns all of the h1 elements inside of the id container.
// let allh1A = document.querySelector("#container > h1")
// console.log(allh1A)
//----------------------------------------------------------------------------------------------------
// For each of the questions, find 2 WAYS to access :

// 1. The div node
// let divContainer = document.getElementById("container")
// console.log(divContainer)
// let divContainer2 = document.querySelector("div")
// console.log(divContainer2)

// 2. The ul nodes, and render all of it's children one by one
// let ulElement = document.getElementsByTagName("ul")
// console.log(ulElement)
// // let ulElementSecond = document.getElementsByClassName("list")
// // console.log(ulElementSecond)
// // let ulElementThird = document.querySelectorAll(".list")
// // console.log(ulElementThird)
// // for (let ul of ulElement){
// //     console.log(ul.children[0].textContent, ul.children[1].textContent)
// // }
// // 3. The first li of each ul
// //for all of the ul inside of ulElement loop around the 0th index
// //of ul element.
// for (let ul of ulElement){
//     console.log(ul.children[0].textContent)
// }
// //selects with the query 
// //selector all all of the classes lists first child. jon and sarah
// let firstLi = document.querySelectorAll(".list :first-child");
// console.log(firstLi)

//------------------------------------------------------------------------------

// let ulElementThird = document.querySelectorAll(".list")
// //need to do for loop to loop through items within the list
// for (let ul of ulElementThird){
//     //adds onto the unordered list a class called title
//     ul.classList.add("title")
// }
// for (let ul of ulElementThird){
//     //replaces list class with this class
//     ul.classList.replace("list", "this")
// }
// // creates new link text within the anchor tag
// let anchor = document.getElementById("link");
// //changes text within the anchor tag
// anchor.textContent = "click Here"
// // adding an attribute to the text ex href, and after the comma is located the attribute
// //is equal to the link.
// anchor.setAttribute("href", "http://learn.di-learning.com/courses/collection/18/course/11/section/42/chapter/160");
//-------------------------------------------------------------------------------------------------
// let names = ["John", "Lola", "Tom"];
// // 1. Create a function that adds the name of each students to 
// // a paragraph
// // 2. each paragraph needs to be background yellow, font-size 25px
// // 3. Add the 3 paragraph to the div already on the page
// function paragraph(){
//     //creates loop iterating through names array
//     for(i=0; i < names.length; i++){
//         //create new variable that is equal to the creation of the element tag p
//         let newParagraph = document.createElement( "p");
//         //the new paragrapgh is given text that is equal to the iteration of the array
//         newParagraph.textContent = names[i];
//         //call the container element and upload the new paragraph using append child
//         document.getElementById("container").appendChild(newParagraph)
//         newParagraph.style.background = 'yellow';
//         newParagraph.style.fontSize= '25px';
//     }
// }
// //return function paragraph
// paragraph()
//-----------------------------------------------------------DAY 2 EVENT HANDLER DOM-----------------------------------------------------------------------------------------------------

// //1 creating a new row within the table
// let tableRow = document.createElement("tr")
// //1 creating a table data cell
// let tableData = document.createElement("td")
// //2 add text in to the data cell
// let newText = document.createTextNode("New row 1 cell 1")
// //3.add the new text to the table data cell
// tableData.appendChild(newText);
// //1  creating a table data cell
// let tableData1 = document.createElement("td")
// //2 add text in to the data cell
// let newText1 = document.createTextNode("New row 1 cell 2")
// //3.add the new text to the table data cell
// tableData1.appendChild(newText1);
// //4. find the location of which you want to insert the new content
// let table = document.getElementById("sampleTable").firstElementChild;
// console.log(table)
// //5. add the table data to table row
// tableRow.appendChild(tableData);
// //5. add the table data to table row
// tableRow.appendChild(tableData1);
// //add the table row to the table
// table.appendChild(tableRow)
//------HTML to the exercise above---------
// <!DOCTYPE html>
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta http-equiv="X-UA-Compatible" content="IE=edge">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>Document</title>
// </head>
// <body>
//     <table id="sampleTable" border="1"> 
//       <tr>
//         <td>Row1 cell1</td> 
//         <td>Row1 cell2</td>
//       </tr> 
//       <tr>
//         <td>Row2 cell1</td> 
//         <td>Row2 cell2</td>
//       </tr> 
//     </table>
// <input type="button" onclick="insertRow()" value="Insert row">  
//     <script src="classNotesWk3.js"></script>
// </body>
// </html>
//-------------------NEW EXERCISE---------------------------------------------------
// let button = document.getElementById("btn");
// let title = document.getElementById("title")

// // SYNTAX:
// // element.addEventListener(DOM events, callback function);

// // with a function as a callback function
// function welcome(){
// 	console.log("hello")
// }

// //to the button adding an event listener of welcome every time we click the button
// button.addEventListener("click", welcome)
// //adds welcome every time we click on the title
// title.addEventListener("click", welcome)


// // with anonymous function as a callback function
// button.addEventListener("click", function (){
// 	console.log("hello")
// })
// //to the button we are adding an eventlistener for hovering the mouse over the button instead of clicking
// // the result will be the word hovered when the mouse hovers over the button
// button.addEventListener("mouseover", function (){
// 	console.log("hovered")
// })

// title.addEventListener("click", function (){
// 	console.log("hello")
//--------------------HTML FOR EXERCISE ABOVE--------------------------

{/* <button id="btn">Click me</button>
<h1 id="title">I'm an H1</h1> */}

//----------------------------------------------------------------------
//goal is to click on button red and change background to red
//and click blue and change background to blue

// document.getElementById('btn').onclick = function() {
//     document.body.style.background = 'red';
// }
// document.getElementById('btn1').onclick = function() {
//     document.body.style.background = 'blue';
// }

//----------------HTML FOR EXERCISE ABOVE------------------------------
{/* <button id="btn">red </button>
<button id="btn1">blue</button> */}
//---------------------------------------------------------------------------

// Exercise
// 2. Add one button per color inside the div container (do it directly in the JS)
// 3. Each button should have an "click" event listener that 
// changes the background color of the document,  to the color of the button (do it directly in the JS)

// Example:
// when you click on the YELLOW button, it should change the document 
// background color to yellow
// let colors = ["blue", "yellow", "green", "pink"];

// for (let i = 0; i < colors.length; i++){
//     //create btn variables for each iteration of i
//     let btn = document.createElement("button");
//     //give the new button text content of each iteration of colors array
//     btn.textContent = colors[i]
//     console.log(btn)
//     //add an event listener for clicking on the button and attach the function
//     btn.addEventListener("click", changeColor);
//     //append the btn inside of the first element of the body
//     document.body.firstElementChild.appendChild(btn);
//     //create a function for the event listener
//     function changeColor() { 
//         //iterate throught each color inside the array and assign the color as a background
//         document.body.style.background = colors[i];
//     } 

// }
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//look up how to use the event parameter inside of your function example;
//function changeColor(event){
//     let colorButton = event.target.textContent.toLowerCase();
//     bodyElement.Style.backgroundColor = colorButton
// }
//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
//------------------------------------MANIPULATING FORMS------------------------------------
{/* <form id="add-book">
				<label for="title">Title</label>
				<input type="text" name="title" id="title">
				
				<label for="author">Author</label>
				<input type="text" name="author" id="author">
				
				<button>Add book</button>
</form>

<div id="container"></div> */}
//-------------------------------------------------------------------------------------------
let bookForm = document.forms[0]; //select by index
let bookForm = document.forms['add-book'] //select by id

// console.log(bookForm)
// console.log("elements", bookForm.elements.title)
//take the variable and add an event listener witht he submit and add book uncalled funtion
bookForm.addEventListener("submit", addBook)
//create a new variable div with all the elements of the id container
let div = document.getElementById("container")

function addBook (event) {
    //cancels the default reload of sending an input 
	event.preventDefault();
    //creates a variable for value title
	let inputTitle = event.target.elements.title
    //creates a variable for value author
	let inputAuthor = event.target.elements.author
    // creates a variable for the input value of title
	let titleValue = inputTitle.value;
    //creates a variable for the input value of author
	let authorValue = inputAuthor.value;
    //creates a new paragraph element
	let pOne = document.createElement("p")

	let textOne = document.createTextNode(titleValue)
	let textTwo = document.createTextNode(authorValue)


	pOne.appendChild(textOne)
	pTwo.appendChild(textTwo)

	div.appendChild(pTwo)
	div.appendChild(pOne)

	inputTitle.value = "";
	inputAuthor.value = ""
	 
}
//------------------------------------------------------------------DAY 3 DOM--------------------------------------------------------------------------------------------------------
//how to find an an object using selectors
			//querySelectorAll(selectors: DOM string)
			//getElementsByCkassName(selectors: DOM string)
			//getElementsByTagName(selectors: DOM string)
			//HOW TO RETRIEVE A SINGLE ID
			//----------------------
			//getElementByID(selectors: DOM string)
			//querySelector(selectors: DOM string)

//1a. retireve object/ item/ tag/ what you are searching for
//1b. retrieve the input values
//2. add to the elements an event listener, with a specific event
//3. add a callback function inside the addEvent listenr method
//4. write the logic inside of the callback function


// let allLi = document.querySelectorAll("li")
// //when looking at li it will look like an array, but it is not. you can access individual elements using its index positiion
// console.log(allLi[2])

// //for loop will automatically cycle through the index of allLi and return its index position.
// // for(let i = 0; i < allLi.length; i++){
// // 	console.log(allLi[i])
// // }

// //this for of loop will return each individual li value from its index position
// for (let li of allLi){
// 	console.log(li)
// }
//---------------------------ADDING DRAGGABLE OBJECTS EVENT LISTENER-------------------FROM-HERE-DOWN-----------------------------------------

// 1. --------------------Retrieve the item of choice--------------------------------
// let item = document.getElementById("item");
// //adds an event listener to created variable item for dragging element
// item.addEventListener("dragstart", startDragging);

// //---------------create a function for dragging the selected item----------------
// //the function of the event  listener  will be created for dragging
// function startDragging (event) {
// 	//always console.log to see that the function is working. check to see that the target item is aquired
// 	console.log("start dragging", event.target.id);
// 	//event.target refers directly back to the event you want to use (dragstart) and the target you are targeting(id = item)
// 	event.target.classList.add("startDragging");
// 	//when the event is called, we want to transfer the item data as well, so we need to set the data element of the file.
// 	//we call the event-----we call the data transfer --- and set the data method.
// 	// event------.----------dataTransfer-------.---------setData("type of data", id of the elem)
// 	event.dataTransfer.setData("text/plain",event.target.id)
// }


//2. ----------dropping the dragged target to the desired location-----------------
//now we select where the dragged item will be dropped and identify the locations
// let allDropZones = document.getElementsByClassName("dropzone");
// //console.log to check that we have selected our specific drop zones
// console.log(allDropZones)


//-----------------create a function------------------------
//that adds an event listener to our specific drop zones and cycle through using a for loop to assign listeners to item
// function addTheListeners (){
// 	//simple for loop attaches a event lister to the drop location. specifically giving a drag over listener 
// 	//and a drop listener to each zone item inside of the class allDropZones
// 	for (let zone of allDropZones){//	the function of dragging over is uncalled until used
// 		zone.addEventListener("dragover", draggingOver)
// 							//the function dropping is uncalled until used
// 		zone.addEventListener("drop", dropping)
// 	}
// }
// //call back funtion of add listeners so from the start all desired variables return a listener.
// //the next functions are called but not opened until the listener is activated
// addTheListeners()

//------------------- create function-------------------
// that adds an event listener that defigns what happens when the dragged item will hover over the drag zone
//----------------you can use this function to say that if the dragged item matches than you can drop the item here.
//-----------------otherwise the dragged item is not able to be dropped here
//by default we need to prevent the default setting of dragover event
// function draggingOver (event){
// 	//nothing is done when item is hovering over the selected drop. no action is taking, but the spot is identified
// 	event.preventDefault();
// //return the function only when desired and without (), this will activate it only when desired. Line 404
// }

//-------------------- Create a function----------------------
// what happens when you drop the dragged item
// function dropping(event){
// 	//prevents automatically outside of the specified location???????????
// 	event.preventDefault();	
// 	// 1. returns the event.dataTransfer.set that we have set for the dragging function
// 	// and we can save this in a new location using the event.dataTransfer.getData and then saving it in a variable
// 	let elementToDrop = event.dataTransfer.getData("text/plain")
// 	// 2. now we need to call the new variable by its ID name to select the transfer of data
// 	let elemNode = document.getElementById(elementToDrop)
// 	//append the data transfer to the correct location.
// 	// using the specified event(dropping) and the target (drop zone) we are appending (dataTransfer.getData)
// 	event.target.appendChild(elemNode)
// //return the function only when desired and without (), this will activate it only when desired. Line 406
// }
//---------------------------------HTML/ CSS FOR DRAGGABLE OBJECTS-------------------------------------------------------------
// <!DOCTYPE html>
// <html>
// <head>
// 	<meta charset="utf-8">
// 	<meta http-equiv="X-UA-Compatible" content="IE=edge">
// 	<title></title>
// 	<link rel="stylesheet" href="style.css">
// </head>
// <body>
// 	<section>
// 		<div class="dropzone"></div>
// 		<div class="dropzone"></div>
// 		<div class="dropzone"></div>
// 	</section>
	
	
// 	<section>
// 		<div id="item" class="draggedItem" draggable="true">1</div>
// 	</section>

// 	<script type="text/javascript" src="week3ClassNotes.css"></script>
// </body>
// </html>
//-------------CSS-----------------
// * {
// 	box-sizing: border-box;
// 	outline: 0;
// }

// section {
// 	display:  flex;
// 	justify-content: center;
// 	align-items: center;
// 	gap : 10px;
// 	margin-top:  10px;
// }

// .dropzone {
// 	width : 100px;
// 	height:  100px;
// 	border:  2px solid black;
// 	display:  flex;
// 	justify-content: center;
// 	align-items: center;
// }

// .draggedItem {
// 	width : 90px;
// 	height:  90px;
// 	padding:  2px;
// 	border:  2px solid green;
// 	border-radius:  20%;
// 	background-color: lightgreen;
// }

// .startDragging {
// 	border:  2px solid blue;
// 	border-radius:  40%;
// 	background-color: lightblue;
// }

//------------------------------------------------------------------------------------------------------------------^^^^^^^TO HERE^^^^^-----