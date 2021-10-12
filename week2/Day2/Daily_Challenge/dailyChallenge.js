/*Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”. For example, “The movie is not that bad, I like it”.


Create a variable called wordNot where it’s value is the first appearance of the substring “not” (from the sentence variable).


Create a variable called wordBad where it’s value is the first appearance of the substring “bad” (from the sentence variable).


If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.


For example, the result here should be : “The movie is good, I like it”


If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.*/


let sentence = "The movie is that bad, I like it"
let array  = sentence.split(" ")
/*console.log(array)*/
let wordNot = array.indexOf("not")
/*console.log(wordNot)*/
let wordBad = array.indexOf("bad")
/*console.log(wordBad)*/
let result ; 

if (wordBad > wordNot && wordBad !== -1 && wordNot !== -1){
	/*splice removes everything from a starting index obj to a finishing index obj*/
	array.splice(wordNot, wordBad - wordNot + 1 , "good")
							/*5		-	3	+	1*/
	result = array.join(" ")
	console.log(result)
	
	}
	/*now because of the /not that bad/g locates the specific class to replace as good*/
	/*wordBad/ wordNot === -1 reutrns the condition, if the word is not found inside the sentence. */
else {
	console.log(sentence)
}



/*Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”. For example, “The movie is not that bad, I like it”.
Create a variable called wordNot where it’s value is the first appearance of the substring “not” (from the sentence variable).
Create a variable called wordBad where it’s value is the first appearance of the substring “bad” (from the sentence variable).
If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, then console.log the result.
For example, the result here should be : “The movie is good, I like it”
If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.*/


let sentence = "the movie is not that bad  , I like it."
let array  = sentence.split(" ")
/*console.log(array)*/
let wordNot = array.indexOf("not")
/*console.log(wordNot)*/
let wordBad = array.indexOf("bad")
/*console.log(wordBad)*/

if (wordBad > wordNot){
	console.log(sentence.replace(/not that bad/g, "good"))
	
	}
else{
	console.log(sentence)
}

/*let sent1 = sentence.replace(/not that bad/g, "good")
console.log(sent1)*/