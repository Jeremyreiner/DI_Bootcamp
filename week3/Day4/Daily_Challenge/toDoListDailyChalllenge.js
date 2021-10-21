let addToDoButton = document.getElementById("addToDo")
let ToDoContainer = document.getElementById("toDoContainer")
let userInput = document.getElementById("inputField")
let listTasks = [];



addToDoButton.addEventListener("click", function(){
    //if the user enters a value than continue forward
    if(userInput.value != "" ){
    //push user input into array
    let arrayLists = listTasks.push(userInput.value);
    console.log(arrayLists)
    // create a new variable for the userinput
    let newText = userInput.value
        //let the input variable equal a created element input element
        let input = document.createElement("input");
        //set the new variables attribute as a checkbox
        input.setAttribute("type", "checkbox");
        //give the new variable an id linking the label to the input
        input.setAttribute("id", `${newText}`)
        //do the same thing for label so they have matching ids
        let label = document.createElement("label");
        label.setAttribute("for", `${newText}`)
        // combining the css with js
        label.classList.add("label")
        //add the text from user to the label
        label.append(newText)
        //add the label to the input element
        label.append(input)
        //add the input back to the container
        ToDoContainer.appendChild(label)
        //reset the value of the input bar
        userInput.value = "";

        
        let inputTag = document.getElementById(`${newText}`)
        console.log(inputTag)
        //add event listeners for crossing out and removing the toDo
        inputTag.addEventListener("click", function(){
            label.style.textDecoration = "line-through";
        })
        inputTag.addEventListener("dblclick", function(){
            ToDoContainer.removeChild(label);
        })
    }
    else{
        //if user does not enter a value to the checklist, there will be an alert
    alert("You forgot to enter an item")
    }
})



