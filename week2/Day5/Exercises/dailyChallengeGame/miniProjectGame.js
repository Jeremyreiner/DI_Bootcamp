// Exercise 1 : Play A Guessing Game
// Instructions
// Create a new folder on your computer.
// Clone or Download the index.html and style.css files from this github link.
// Follow the steps written below
//--------------------------------------------------------------------------
// First Part
// 1.  Create a JS file and link it to the index.html file.
// 2. Take a look at your html file, you should have a button with an “onclick” event.
//   This event is equal to the function playTheGame(). 
//   It means that when you will click on the button, the function playTheGame() will be called.
//   We will learn more about events next week ;)
//   Now let’s create the function:
// 3. In the JS file, create a function called playTheGame() that takes no parameter.
function playTheGame(){
    let loopAgain = true;
    let userNumber ;
    let computerNumber;
    // In the function, start by asking the user if they would like to play the game (Hint: use the built-in confirm() function).
    let play = prompt("Would you like to play the game? (yes/no)");
    play = play.toLowerCase();
    do {
        // If the answer is false, alert “No problem, Goodbye”.
        if (play === "no"){
            alert("No problem, Goodbye");
            //leaving loop
            loopAgain = false;
            
        }
        // If his answer is true, follow these steps:
        else if (play === "yes" ){
            // Ask the user to enter a number between 0 and 10 (Hint: use the built-in prompt() function).
            userNumber = parseInt(prompt("Please enter a number between 1- 10."));
            let numIsNaN = isNaN(userNumber);
            // You then have to check the validity of the user’s number :
            // If the user didn’t enter a number (ie. if he entered another data type) alert “Sorry Not a number, Goodbye”.
            if(numIsNaN) {
                alert("Sorry Not a number,try again.");
                //returning back trhough loop untill valid number is provided
                loopAgain = true;
            }
            // If the user didn’t enter a number between 0 and 10 alert “Sorry it’s not a good number, Goodbye”.
            else if((10 < userNumber) || (userNumber < 0)){
                alert("Sorry it’s not a good number,try agani.");
                //returning back trhough loop untill valid number is provided
                loopAgain = true;
            }
            else{// Else (ie. he entered a number between 0 and 10), create a variable named computerNumber
                // where the value is a random number between 0 and 10 (Hint: Use the built-in Math.random() function). 
                // Make sure that the number is rounded.
                computerNumber = Math.round(Math.random()*10);
                // console.log(computerNumber)
                loopAgain = false; //get out of loop
                test(userNumber,computerNumber);
            }
        }
        else{
            play = prompt("You did not resond with yes or no.");
            loopAgain = true;   // Restart the loop
        }
    }while(loopAgain == true);
}
//-------------------------------------------------------------------------------------------------------
// Second Part
// Outside of the playTheGame() function, create a new function named test(userNumber,computerNumber)
// that takes 2 parameters : userNumber and computerNumber
// The point of this function is to check if the userNumber is the same as the computerNumber:
function test(userNumber,computerNumber) {
    let maxTries = 2;   // 3 tries 0,1,2
    for(let i=0; i <= maxTries; i++){
        // If userNumber is equal to computerNumber, alert “WINNER” and stop the game. 
        if (userNumber === computerNumber){
        alert("WINNER!!");
        return;
        }
        // If userNumber is bigger than computerNumber, alert “Your number is bigger then the computer’s, guess again”
        else if (userNumber > computerNumber){
            alert(`Your number is bigger then the computer’s, guess again.`);
            // (Hint: use the built-in prompt() function to ask the user for a new number).
            let newUserNumber = parseInt(prompt("Your guess was too high, please insert another number"));
            userNumber = newUserNumber;
            
        }
        // If userNumber is lower than computerNumber, alert “Your number is smaller then the computer’s, guess again”
        // (Hint: use the built-in prompt() function to ask the user for a new number).
        else if (userNumber < computerNumber){
            alert("Your number is lower then the computer’s, guess again.");
            let newUserNumber = parseInt(prompt("Your guess was too low, please insert another number"));
            userNumber = newUserNumber;
        }
        else{

        }
    }
    // If the user guessed more than 3 times, alert “out of chances” and exit the function.
    alert(`out of chances: your number: ${userNumber}, computer number: ${computerNumber}`)
    
}

//------------------------------------------------------------------------------------
// Bonus
// In the First Part, instead of stopping the process if the user didn’t enter a valid number. Continue asking
// for a number until the user enters a valid number.
//--------------------------------------------------------------------------------------------------------------------------------