let colors = ["red", "orange","yellow","green", "turquoise", "lightblue", "blue","darkblue","purple",]
let sectionColors = document.getElementById("gridC2")
let isMouseDown = false;

//sets the variable of the new background inthe global scope to be
//used in future functions
let colorBg
//give the event listener a function 
function getBgColor(){
    //the variable is retrieved within the function and background color is changed
    colorBg = this.style.backgroundColor;
    // console.log(colorBg)

}

//for loop creates a new div object for each color in the array colors
for(let i= 0; i < colors.length; i++){
    //create new div item
    let newDiv = document.createElement("div");
    //give div style
    newDiv.style.backgroundColor = colors[i];
    //give div style
    newDiv.style.border = "1px solid black";
    //add a new class to the div
    newDiv.classList.add("BackgroundColor");
    //add div to the desired  section
    sectionColors.appendChild(newDiv);
    // bgColorSelector[i].addEventListener("click", setBgColor)
}
//locate the clear button and give it a 
let clearBtn = document.getElementsByClassName("button")[0]
clearBtn.addEventListener("click", clear)


//new variable introduces section two
let coloringGrid = document.getElementById("gridC3")
//create for loop to create coloring grid
for (let i =0; i < 400; i++){
    //new variable creates div
    let newDiv1 = document.createElement("div");
    //give dive style
    newDiv1.style.border = "1px solid black";
    //give div a new class
    newDiv1.classList.add("inputBackground")
    newDiv1.addEventListener("mousedown", function(){
        newDiv1.style.backgroundColor = colorBg;
        isMouseDown = true;
    })
    newDiv1.addEventListener("mouseover", function(){
        if(isMouseDown){
        newDiv1.style.backgroundColor = colorBg;
        }
    })
    newDiv1.addEventListener("mouseup", function(){
            isMouseDown = false;

    })
    //upload the new div to the section
    coloringGrid.appendChild(newDiv1);
    //adds event listener to each square
    clearBtn.addEventListener("click", clear)
    function clear(){
        newDiv1.style.backgroundColor = "white"
    }


}

//selects the element background color by class. Should be all of the divs with background colors
let bgColorSelector = document.getElementsByClassName("BackgroundColor")
// console.log(bgColorSelector)
//create a for loop adding an event click listener to each div item within the length of the selected element
for(let i= 0; i < bgColorSelector.length; i++){
    bgColorSelector[i].addEventListener("click", getBgColor)
}

//select the coloring grid divs
let inputBg = document.getElementsByClassName("inputBackground")
// console.log(inputBg)
//give each div item within the coloring grid a click function
for (let i = 0; i < inputBg.length; i++){
    //iterates throught he divs and adds an event listener
    inputBg[i].addEventListener("click", setBgColor);
}


//deliver the desired background color
function setBgColor(event){
    event.target.style.backgroundColor = colorBg;
}


