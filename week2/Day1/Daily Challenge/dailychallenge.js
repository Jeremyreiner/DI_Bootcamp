/*exercise 1*/

/*Remove Banana from the array.
Sort the array in alphabetical order.
Add “Kiwi” to the end of the array.
Remove “Apples” from the array. Don’t use the same method as in part 1.
Sort the array in reverse order. (Not alphabetical, but reverse the current Array i.e. [‘a’, ‘c’, ‘b’] becomes [‘b’, ‘c’, ‘a’])
At the end you should see this outcome:
*/


/*let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
fruits.splice(0, 1)
let order = fruits.sort();

fruits.push("kiwi")

let fruits2 = fruits.slice(1)

let orderR = fruits2.reverse();
console.log(orderR)
*/



/*Exercise 2:
Using this array :


Access and then console.log “Oranges”.
Bonus: If you would like more array exercises take a look at the link below.

Array Exercises*/

let fruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(fruits[1][1][0])

