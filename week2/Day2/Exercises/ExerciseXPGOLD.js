/*let language = prompt("What language do you speak? ").toLowerCase()
console.log(language)

switch(language) {
  case "french":
  	console.log("Bonjour")
    break;
  case "english":
  	console.log("Hello")
    break;
   case "hebrew":
  	console.log("Shallom")

    break;
  default:
  console.log("01110011 01101111 01110010 01110010 01111001")

}*/


/*--------------exercise 2---------------------*/

/*let grades = prompt("What are your number grades")
grades1 = parseInt(grades)
console.log(grades)

if (grades1 > 90){
	console.log("A")
}
else if (grades1 > 80){
	console.log("B")
}
else if (grades1 > 70){
	console.log("C")
}
else{
	console.log("D")
}*/

/*------------------Exercise3----------------*/

/*Prompt the user for a string. It must be a verb.
If the length of the string is at least 3 and the string doesn’t end with “ing”, add ‘ing’ to the end of the string.
If the length of the string is at least 3 and the string ends with “ing” add “ly” to it’s end.
If the length of the string is less than 3, leave it unchanged.*/

let verb = prompt("Enter in a verb: ")
let ing = "ing"
let ver1 = verb.length
/*console.log(ver1)*/

if (ver1 <= 3)
{
	console.log(verb)
	
}
else if (verb.includes(ing)){
/*	verb = verb.endsWith("ing")*/
	ver1 >= 3;

	console.log(verb + "ly")

}
else {
	
	console.log(verb + ing)
}

