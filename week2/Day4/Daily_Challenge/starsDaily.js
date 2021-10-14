// Prompt the user for several words (separated by commas).
// Put the words into an array.
// Console.log the words one per line, in a rectangular frame as seen below.
// Check out the Hints and Requirements below.
// Hello, World, in, a, frame
// you will transform it to : ["Hello", "World", "in", "a", "frame"]
//-----------------------------------------------------------------------
//make a list using a prompt that will be seperated with commas
// let stringWcomas = prompt("please give a list of words seperated by commas.")
let stringWcomas = "Hello,World,in,a,frame";
//use split() to form an array
let arrayOfWords = stringWcomas.split(",");

//set variable longestLength item to 0
let longestLength = 0;
//find the longest index item in the array.
for (let i = 0; i < arrayOfWords.length; i++){
    //word variable will equal individual words from array
    let word = arrayOfWords[i];
    //find length of individual words
    let length = word.length;
    //Last length will always start at 0 and grow if the next word is larger.
    if(length > longestLength){
        //last length is equal to the next longest word in array
        longestLength = length;
    }
}
// Top bar
console.log("*".repeat (longestLength + 4));
//body of the image
for (let i = 0; i < arrayOfWords.length; i++){
    //variable word of index array
    let word = arrayOfWords[i];
    //spaces will be empty gap in shortest word between borders
    let spaces = longestLength - word.length;
    //creates the frame and interior of the box
    console.log("* " + word + " ".repeat (spaces) + " *");
}
// bottem bar
console.log("*".repeat (longestLength + 4));
