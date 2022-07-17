let firstCard = 10
let secondCard = 11
let sum = firstCard + secondCard

let hasBlackJack = false //default, udh blackjack

if (sum <= 20) {
    console.log("Do you want to draw a new card? 🙂")
} else if (sum === 21) {
    console.log("Wohoo! You've got Blackjack! 🥳")
    hasBlackJack = true
} else {
    console.log("You're out of the game! 😭")
}

// variable keeps track of the state of the game
// variable reflects whether or not user has blackjack

// CASH OUT!
console.log(hasBlackJack)