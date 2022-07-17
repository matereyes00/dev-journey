let firstCard = 6
let secondCard = 9
let sum = firstCard + secondCard

// blackjack: get exactly 21 (close to 21 but NEVER above 21)
if (sum < 21) {
    console.log("Do you want to draw a new card?")
} else if (sum === 21) {
    console.log("Woo! You've got blackjack")
} else if (sum > 21) {
    console.log("You're out of the game!")
}