
/*Ask the user to give you a sentence containing the word “Nemo”. For example "I love the movie named Nemo !
"*/
let sentence = prompt("Write a sentence using the word: Nemo")



/*Find the word “Nemo”*/

let found = String.indexOf(sentence)
let str = fish.split("nemo")


/*Console.log a string as follows: "I found Nemo at [the position of the word Nemo]!".*/
let newSentence = ("i found" + fish + "at the sea.")
console.log(newSentence)



/*/*Bonus : If you can’t find Nemo, console.log “I can’t find Nemo”.*/