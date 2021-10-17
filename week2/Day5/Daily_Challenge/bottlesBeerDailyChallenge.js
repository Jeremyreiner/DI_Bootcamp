// Instructions
// Have you heard the infamous song “99 Bottles of Beer?”
// In ths exercise you need to console.log the lyrics to the song 99 Bottles of Beer as an output.
// What your code should do is:
// instead of subtracting by 1, everytime a bottle drops the subtracted number should go up by 1
// For example the first time a bottle drops we subtract by 1, the second time we subtract by 2 and so on.
//---------------------------------------------------------------------------------------------------------------------------
// Prompt the user for a number to begin counting down bottles.
let numberPrompt = parseInt(prompt(`Please give me a number to start the song.`));
// In the song everytime a bottle falls we subtract the bottles by 1.
let maxTotal = numberPrompt;
for (let i = 0; i < maxTotal; i++){
    let totalBottles = maxTotal - i;
    let newBottleTotal = totalBottles -1;
    if(totalBottles > 1){
    console.log(`${totalBottles}, bottles of beer on the wall, ${totalBottles}, bottles of beer. Take one down, pass it around, ${newBottleTotal} bottles of beer on the wall.`)
    }
    else if(totalBottles === 1){
        console.log(`${totalBottles}, bottle of beer on the wall, ${totalBottles}, bottle of beer. Take one down, pass it around, ${newBottleTotal} bottles of beer on the wall.`)
    }
}
