// Instructions
// Have you heard the infamous song “99 Bottles of Beer?”
// In ths exercise you need to console.log the lyrics to the song 99 Bottles of Beer as an output.
// What your code should do is:
// instead of subtracting by 1, everytime a bottle drops the subtracted number should go up by 1
// For example the first time a bottle drops we subtract by 1, the second time we subtract by 2 and so on.
//---------------------------------------------------------------------------------------------------------------------------
// Prompt the user for a number to begin counting down bottles.
let numberPrompt = parseInt(prompt(`Please give me a number to start the song.`));
let maxBottles = 10;
for (i = 0; i > maxBottles; i++) {
    //update number prompt after last 
    let newBottleTotal = numberPrompt - i;
    //updated bottle will be the new bottle cound
    let updatedBottleTotal = numberPrompt - newBottleTotal;
}
console.log(`${newBottleTotal}, bottles of beer on the wall, ${newBottleTotal}, bottles of beer. Take one down, pass it around, ${updatedBottleTotal} bottles of beer on the wall.`)
    