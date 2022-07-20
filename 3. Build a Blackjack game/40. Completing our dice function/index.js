

// console.log(randomNumber)

// how to turn into 1 -> 6??

// create a function, rollDice(), that returns a random number between 1 and 6
function rollDice() {
    // Try to modify the expression so that we get a range from 1 to 6
    let randomNumber = Math.floor( Math.random() * 6 ) + 1
    return randomNumber
}

console.log(rollDice())