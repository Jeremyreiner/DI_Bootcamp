// Create A Hangman Game:
// Instructions:
// Create the “Hangman” game. Your game will run in the console.
// You need to guess a hidden word. Each letter you guess will appear in the console. You have 10 chances before you lose the game.

// Check it out here

// Prompt player 1 for a word. The word must have a minimum of 8 letters. Present the word in the console with stars (********).
// At this point continuously prompt player 2 for a letter.
// If the letter is in the word chosen by player 1, display the word in stars again but with the correct letter (*****t**).
// If the letter appears in the word multiple times, make sure it is seen in all the correct places when showing the stars with the correct guesses (***t**t*).
// If player 2 guesses incorrectly 10 times display a message in the console saying YOU LOSE.
// Show a list of all the guesses after each turn. In your code prevent player 2 from guessing the same letter twice.
// If player 1 wins, display a message that says CONGRATS YOU WIN
//--------------------------------------------------------------------------------------------------------------------

// Prompt player 1 for a word. The word must have a minimum of 8 letters. Present the word in the console with stars (********).

let playerOneWord = "";
//while in do loop continue prompting player one for a word with minimum 8 charecters
do{
    playerOneWord = prompt(`Please give me a word with a minimum of eight letters.`).toLowerCase();
}
//do loop is done and then checks to verify if inside the while loop is correct
while(playerOneWord.length < 8)

let stars = "";
//switches the playersOneWords letters out for stars
for (let i=0; i<playerOneWord.length; i++){
     stars = stars + "*";
}
// console.log(stars);
// If the letter is in the word chosen by player 1, display the word in stars again but with the correct letter (*****t**).
let attempts = 0;
attempts = attempts + 1;
// At this point continuously prompt player 2 for a letter.
let playerTwoLetter = prompt(`Player 2, please give me a letter.`).toLowerCase();
//index OfLetter checks if player twos guess is in player ones word
let indexOfLetter = playerOneWord.search(playerTwoLetter);
//if the letter from player two is in the word
if (indexOfLetter != -1){
    // display the word in stars again but with the correct letter (*****t**).
    stars[indexOfLetter] = playerTwoLetter;
    //.substring will cut the string at the starting point up until designated point. 
    //we are cutting the stars substring at 0 up to indexOfletter
    // adding in player twos letter, and then resubmitting the stars one space after player twos letter up until the end
    stars = stars.substring(0, indexOfLetter) + playerTwoLetter + stars.substring(indexOfLetter + 1);
    console.log(stars);
}
else{

}
