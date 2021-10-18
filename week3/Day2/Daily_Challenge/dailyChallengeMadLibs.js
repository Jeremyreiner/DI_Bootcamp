// Get the value of each of the inputs in the HTML file when the button is clicked.
// Make sure the values are not empty
// Write a story that uses each of the values.
// Make sure you check the console for errors when playing the game.
// Bonus: Add a “shuffle” button to the HTML file, when clicked the button should
// change the story currently displayed (but keep the values entered by the user).
// The user could click the button at least three times and get a new story. Display the stories randomly.
//-----------------------------------------------------------------------------------------------------
// //creating a variable using all elements with the tag name input
// let inputValue = document.getElementsByTagName("input")
let li = document.querySelectorAll("li")
//creating a button variable using the element id 
let btn = document.getElementById("lib-button")
//add onto the button click eventlistener with a function
btn.addEventListener("click", function () {

    // list of new variable values
    let placeValue = place.value
    let newVerb = verb.value
    let personEl = person.value
    let newAdj= adjective.value
    let newNoun = noun.value
 
    let spanStory = document.getElementById("story")
    spanStory.innerHTML=`the place is ${placeValue}, and the verb is ${newVerb}, and the adj is ${newAdj}, and the noun is ${newNoun}, and the person is ${personEl}`;

})