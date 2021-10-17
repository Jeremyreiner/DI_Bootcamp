// Create an array which value is the planets of the solar system.
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// Each planet should have a different background color. (Hint: add a new class to each planet).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?
//-------------------------------------------------------------------------------------------------
let solarSystem = ["earth","jupiter","saturn","neptune","uranus","venus","mars","mercury"];
let backgroundColor = ["blue","lightblue","white","orange","red","yellow","green","grey","purple"];
function SolarS(){
    //creates loop iterating through names array
    for(let i=0; i < solarSystem.length; i++){
        //create new variable that is equal to the creation of the element div tag
        let newDiv = document.createElement( "div");
        //add in text for each planet
        newDiv.innerText = solarSystem[i];
        //give the div a class selector
        let newClass = newDiv.className = "planet";
        //attach a color to each planet within the loop
        let newColor = newDiv.style.background = backgroundColor[i];
        //call the element child and upload the new div using append child
        document.body.firstElementChild.appendChild(newDiv)
    }
}
SolarS()
// let solarSystem = { planet: "earth", moons: 1,}
// let solarSystem = { planet: "jupiter", moons: 79}
// let solarSystem = { planet: "saturn", moons: 82}
// let solarSystem = { planet: "neptune", moons: 14}
// let solarSystem = { planet: "uranus", moons: 27}
// let solarSystem = { planet: "venus", moons: 0}
// let solarSystem = { planet: "mars", moons: 2}
// let solarSystem = { planet: "mercury", moons: 0}


