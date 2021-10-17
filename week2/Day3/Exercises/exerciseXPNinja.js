// Exercise 1 : Checking The BMI
// Instructions
// Create two objects, each object should hold a persons details. Here are the details:
// FullName
// Mass
// Height
// Each object should also have a key which value is a function (ie. A method), that calculates the Body Mass Index (BMI)
// of each person
// Outside of the objects, create a JS function that compares the BMI of both objects.
// Display the name of the person who has the largest BMI.
//-----------------------------------------------------------------------------------------------------
// function bmi() {
//     return this.Mass / (this.Height*2);
//   }

// let person1 = {
//     fullName: "James",
//     Mass: 77,
//     Height: 1.65,
//     BMI: function bmi() {
//         return this.Mass / (this.Height*2);
//       }
// }
// let person2 = {
//     fullName: "Joonathon",
//     Mass: 65,
//     Height: 1.75,
//     BMI: function bmi() {
//         return this.Mass / (this.Height*2);
//       }
// }
// if (person1.BMI() >= person2.BMI()) {
//     console.log(`${person1.fullName} has the larger BMI of ${person1.BMI()}`)
// }
// else{
//     console.log(`${person2.fullName} has the larger BMI of ${person2.BMI()}`)
// }

//---------------------------------------------------------------------------------------------------------
// Exercise 2 : Grade Average
// Instructions
// Hint:
// - This Exercise is trickier then the others. You have to think about its structure before you start coding.
// - You must use functions to complete this exercise, to do so take a look at tomorrow’s lesson.
// In this exercise we will be creating a function which takes an array of grades as an argument and will console.log the average.
// Create a function called findAvg(gradesList) that takes an argument called gradesList.
// Your function must calculate and console.log the average.
// If the average is above 65 let the user know they passed
// If the average is below 65 let the user know they failed and must repeat the course.
// Bonus Try and split parts 1,2 and 3,4 of this exercise to two separate functions.
// Hint One function must call the other.

let gradesList = [65,88,100,44,33,65,90,67]
let sum = 0

function getSum() {
    //classic for loop start
    for(let i = 0; i < gradesList.length; i++){
        //creating a new sum for each iteration of the array
        sum = gradesList[i] + sum;
        //setting a starting num value with the first index of the array
    }
    console.log(sum)
}
getSum()
function AvgGPA(){
    let avg = sum / gradesList.length
}
AvgGPA


// // If the average is above 65 let the user know they passed
// if(averageGPA < 64){
//     console.log(`You have passed the course with an avg of ${gradeAVG}`)
// }
// // If the average is below 65 let the user know they failed and must repeat the course.
// else{
//     console.log(`You have not passed the course. You need to repeat `)
// }