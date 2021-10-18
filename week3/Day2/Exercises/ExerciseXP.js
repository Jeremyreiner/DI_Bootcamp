// Exercise 1 : Change The Article
// Instructions
// When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
//---------------------------------------------------------------------------------------------------------------
// Using DOM methods, remove the last paragraph in the <article> tag from the DOM.
// let parentElem = document.querySelector("article");
// console.log(parentElem)
// let childElem = document.querySelectorAll("p")[3]
// console.log(childElem)

// parentElem.removeChild(childElem);
// // Add an event listener which will change the background color of the h2 tag from the DOM when clicked on.
// document.querySelector('h2').onclick = function() {
//     document.body.style.background = 'red';
// }
// // Set the font size of the h1 tag to a random pixel size between 0 to 100.(Check out this documentation)
// let h1FontSize = document.getElementsByTagName("h1")[0];
// h1FontSize.style.fontSize = "75px";
// console.log(h1FontSize)

// // Add an event listener which will hide the h3 when it’s clicked on (use the display property).
// let h3Vanish = document.querySelectorAll("h3")[0]
// document.querySelector('h3').onclick = function() {
//     h3Vanish.style.display = 'none';
// }
// // Add a <button> to the HTML file, that when clicked on,
// //should make the text of all the paragraphs, bold.
// let btn = document.createElement("button")
// let btnTxt = document.createTextNode("Bold")
// let btnBold = btn.append(btnTxt)
// document.body.appendChild(btn)
// let allP = document.querySelectorAll("p")


// //adding a event listener to the button click with the anonomous function
// btn.addEventListener('click', function() { 
//     //creating a for loop to cycle through the paragraphs
//     for(let i = 0; i < allP.length; i++){
//         //for all paragraphs create the style class fontweight bold
//         allP[i].style.fontWeight = "bold"
//     } 
// })

// When the “Submit” button of the form is clicked:
// get the values of the input tags
// make sure that they are not empty,
// then append them to a HTML table, in the div, below the form.
// let submit = document.getElementById("submit")
// console.log(submit)

// submit.addEventListener(`click`, function (event){
//     //cancels the default reload of sending an input 
// 	    event.preventDefault();
//     //creates a variable for value title
// 	    let inputFname = document.getElementById('fname').value
//     console.log(inputFname)
//     //variable that finds the place of the object by ID
//     let inputFname1 = document.getElementById('fname')
//     //creates a variable for value last name
// 	    let inputLname =  document.getElementById('lname').value
//     console.log(inputLname)
//     //variable that finds the place of the object by ID
//     let inputLname1 =  document.getElementById('lname')
//     //creates a new paragraph element
// 	    let pOne = document.createElement("p")
//     let pTwo = document.createElement("p")
//     //create text item for 
//     let newInput = document.createTextNode(inputFname)
//     pOne.appendChild(newInput)
//     let newInput1 = document.createTextNode(inputLname)
//     pTwo.appendChild(newInput1)
    
// 	inputFname1.value = "";
// 	inputLname1.value = ""

// }
// )

// // When you hoover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)
// //locate the second paragraph
// let p2 = document.querySelectorAll("p")[1]
// //steal the fade class from w3schools
// p2.classList.add("w3-animate-fading")
// //add a hover function over p2
// p2.addEventListener(`hoover`, function(){
//     //and add the function of hover to activate the fade whilst hovering over p2
//     p2.classList.add(w3-animate-fading)
//     //to attach css class animation to p2 element

// })
// console.log(p2)
//-----------------------------------------HTML TO EXERCISE 1------------------------------------------------------------------------------
// <!DOCTYPE html>
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta http-equiv="X-UA-Compatible" content="IE=edge">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>Document</title>
//     <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
// </head>
// <body>
//     <article>
//         <h1> Some Facts </h1>
//         <h2> The Chocolate </h2>
//         <h3>History of the chocolate</h3>
//         <p> Chocolate is made from tropical Theobroma cacao tree seeds. 
//         Its earliest use dates back to the Olmec civilization in Mesoamerica.</p>
//         <p> After the European discovery of the Americas, chocolate became 
//         very popular in the wider world, and its demand exploded. </p>
//         <p> Chocolate has since become a popular food product that millions enjoy every day, 
//         thanks to its unique, rich, and sweet taste.</p> 
//         <p> But what effect does eating chocolate have on our health?</p> 
//     </article>
//     <form>
//       <label for="fname">First name:</label><br>
//       <input type="text" id="fname" name="fname"><br>
//       <label for="lname">Last name:</label><br>
//       <input type="text" id="lname" name="lname"><br><br>
//       <input type="submit" value="Submit" id="submit">
//     </form> 
//     <div class="usersAnswer"></div>
//     <script src= "ExerciseXP.js"></script>
// </body>
// </html>
//------------------------------------------------------------------------------------------------------------------------------------------------------
// Exercise 2 : Transform The Sentence
// Instructions
//--------------------------------------------------------------------------------------------------
// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph.
// let strong = document.querySelectorAll("strong")
// console.log(strong)
// function getBold (){
//     let getStrong = document.querySelectorAll("strong")
//     console.log(getStrong)
//     }
// getBold()

// // Create a function called highlight() that changes the color of all the bold text to blue.
// function highlight(){
//     for(i =0; i < strong.length; i ++){
//     strong[i].style.color= "blue";
//     }
// // }
// // // highlight()
// // // Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal()
// // //  onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example\
// function return_normal(){
// 	notbold = document.getElementsByTagName("p")[0];
// 	for(let i = 0 ; i < notbold.childElementCount;i++){
// 		notbold.children[i].style.fontWeight="normal";
// 		notbold.children[i].style.color="black";
// 	}
// }
// let p = document.getElementsByTagName("P")[0];

// p.addEventListener("mouseover",highlight);
// p.addEventListener("mouseout",return_normal);
//-------------------------------------------------------------------------------------------------------------------------------------------
// <!DOCTYPE html>
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta http-equiv="X-UA-Compatible" content="IE=edge">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>Document</title>
// </head>
// <body>
//     <p>
//         <strong>Hello</strong>
//          I hope you are enjoying
//         <strong>this</strong> 
//         class. At the
//         <strong>end</strong>
//          you
//         <strong>will</strong>
//         be great Developers!
//         <strong>Enjoy</strong> 
//         the 
//         <strong>JavaScript</strong> 
//         lessons
//     </p>
//     <script src= "ExerciseXP.js">
//     </script>
// </body>
// </html>
//---------------------------------------------------------------------------------------------------------------

// Exercice 3 : Volume Of A Sphere
// Instructions
// Write a JavaScript program to calculate the volume of a sphere. Use the code below as a base:

// //create new variables, at id locations
// let radius = document.getElementById("radius")
// let volume = document.getElementById("volume")
// let button = document.getElementById("submit")
// //make your button reactive by adding a event listener with click action.
// button.addEventListener("click", function(event){
//     //stops web browser from reloading information
//     event.preventDefault();
//     //create new variable for finding volume
//     let volumeResult = (Math.pow(radius.value, 3) * (4 / 3) * Math.PI);
//     console.log(volumeResult)
//     //the volume value will be equal to the result of volume result fixed up to four decimal points
//     volume.value = volumeResult.toFixed( 4)

// })
//-------------------------------------------------------------------------------------------------------------------
