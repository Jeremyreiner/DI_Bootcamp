// Exercise 1 : Move The Box
// Instructions
// Move the box from left to right
// Tip: use setInterval
//----------------------------------------------------------
//select the button and give him a event listener function
// let button = document.querySelectorAll("button")[0]
// console.log(button)
// button.addEventListener("click", moveAnimation)

// //make a function for moving down one over one px
// function moveAnimation(){
//     let red = document.getElementById("animate");
//     let position = 0;
//     let animation = setInterval(function(){
//         if(position == 350){
//             clearInterval(animation)
//         }
//         else{
//             position++;

//             red.style.left = position +"px";
//         }
//     })
// }






// setInterval(function() {
    
// }, 5000);
//---------------------------------------------------------------------------

// Exercise 2: Drag & Drop
// Instructions
// Tip : Check out this video on drag and drop

// Create a draggable square/box element in your HTML file.
// In your javascript file add the functionality which will allow you
//  to drag the square/box and drop it into a larger box.
//-----------------------------------------------------------------------------------
// first locate the item that we want to drag
let item = document.getElementsByClassName("draggedItem")[0]
//next on the item we need to add a listener functionvt
console.log(item)
//to activate an action
item.addEventListener("dragstart", dragItem)
//give the drag item function a job
function dragItem(event){
    console.log("start Dragging", event.target.item)
    event.target.classList.add("StartDragging")
    event.dataTransfer.setData("text/plain", event.target.id)

}

let allDropZones = document.getElementsByClassName("dropzone")
console.log(allDropZones)

function addListener(){
    for (let zone of allDropZones){
        zone.addEventListener("dragover", dragOver)
        zone.addEventListener("drop", dropItem)

    }
}
addListener()

function dragOver(event){
    event.preventDefault();
}
function dropItem(event){
    event.preventDefault()
    let droppedElement = event.dataTransfer.getData("text/plain")
    let nodeElement = document.getElementById(droppedElement)
    event.target.appendChild(nodeElement)
}

//---------------------------------------------------------------------------------------------------------------