let sentence = "The dinner was not so bad , it was nice";
let result;
let arrSentence = sentence.split(" ");
console.log(arrSentence)

let indexWordBad = arrSentence.indexOf("bad");
let indexWordNot = arrSentence.indexOf("not");

// the method indexOf is giving back -1 if the element is not found
// let indexWordHello = arrSentence.indexOf("hello");
// console.log("index hello", indexWordHello);

// console.log("index bad", indexWordBad);
// console.log("index not", indexWordNot);

// console.log("number of elements to delete" , indexWordBad -  indexWordNot + 1)
											 // 8           3

if (indexWordBad>indexWordNot && indexWordBad !== -1 && indexWordNot !== -1){
	
	arrSentence.splice(indexWordNot, indexWordBad -  indexWordNot + 1, "good")
	console.log(arrSentence)
	
	result = arrSentence.join(" ")
	console.log(result)

} else {
	console.log(sentence)
}