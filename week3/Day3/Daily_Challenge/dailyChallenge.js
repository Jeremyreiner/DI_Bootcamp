let input = document.getElementById("userInput")
let button  = document.getElementById("enter")
let ul = document.getElementsByTagName("ul")[0]

//add a listener for key down and open a new function
input.addEventListener('keydown', keyDown);
function keyDown(e) {
    //creat a new variable for li
    let li = document.createElement("li");
    //add text context that will be from the user input
    li.textContent += ` ${e.code} key down`;
    //upload the li onto the page through the ul
    ul.appendChild(li)
    //reset the value
    input.value = " ";
}

input.addEventListener('keyup', keyUp);
function keyUp(e) {
    let li = document.createElement("li");
    li.textContent += ` ${e.code} key up`;
    ul.appendChild(li)
    input.value = " ";
}

