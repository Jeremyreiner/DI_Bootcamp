// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops (Nested means one inside the other - check out “nested for loops” on Google).
// Do this Daily Challenge by youself, without looking at the answers on the internet.


// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

let star = "*"
let longStar = "* * * * * *";
do
{
    console.log(star);
    star = star + " *";
}
while (star.length <= longStar.length);

// star = "*";

// let currentRow = 0
// // outer loop compares star to longStar
// do {
//     currentRow = currentRow + 2;

//     // returns another row and adds another star
//     do 
//     {
//         console.log(star)
//         star= star + " *";
//     }
//     while ( star.length <= currentRow);
    
// } while( star.length <= longStar.length);