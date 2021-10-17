// Exercise 1 : Building Management
// Instructions
// Console.log the number of floors in the building.
// Console.log how many apartments are on the floors 1 and 3.
// Console.log the name of the second tenant and the number of rooms he has in his apartment.
// Check if the sum of Sarah and David’s rent is bigger than Dan’s rent. If it is than increase Dan’s rent to 1200.
//-----------------------------------------------------------------------------------------------------
let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
    },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
    },
}
if(building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]  > building.numberOfRoomsAndRent.dan[1]){
    building.numberOfRoomsAndRent.dan[1] = 1200;
}
else{
    building.numberOfRoomsAndRent.dan[1] = 1000;
}
console.log(building.numberOfFloors)
console.log(building.numberOfAptByFloor.firstFloor)
console.log(building.numberOfAptByFloor.thirdFloor)
console.log(building.nameOfTenants[2])
console.log(building.numberOfRoomsAndRent.david[0])
console.log(building.numberOfRoomsAndRent.dan[1])





//---------------------------------------------------------------------------------------------------------
// Exercise 2 : Divisible By Three
// Instructions
// Loop through the array above and determine whether or not each number is divisible by three.
// Each time you loop console.log true or false.
//-----------------------------------------------------------------------------------------------------------
// let numbers = [123, 8409, 100053, 333333333, 7];

// for (let i = 0; i < numbers.length; i++){
//     if ( numbers[i] % 3 == 0){
//         console.log(`True`)

//     }
//     else{
//         console.log(`False`)
//     }
// }








//-----------------------------------------------------------------------------------------------------------
// Exercise 3 : Playing With Numbers
// Instructions
// Requirements : Don’t use built-in Javascript methods to answer the following questions.
// You have to create the logic by yourself. Use simple for loops.
// 1. Console.log the sum of all the numbers in the age array.
// 2. Console.log the highest age in the array.
//-----------------------------------------------------------------------------------------------------------
// let age = [20,5,12,43,98,55];
// for(i=0; i < age.length; i++){
//     console.log(Math.max(age[i]))
// }

// let sum = age.reduce(function(a, b){
//     return a + b;
// }, 0);
// console.log(sum)
//-----------------------------------------------------------------------------------------------------------