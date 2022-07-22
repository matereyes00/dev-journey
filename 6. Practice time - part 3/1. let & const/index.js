// SETTING THE STAGE
const player = "Per"
const opponent = "Nick"
const game = "AmazingFighter"
let points = 0
let hasWon = false

// PLAYING THE GAME
points += 100
hasWon = true

const playerWonMsg = `
    ${player} got ${points} points and won the ${game} game!
`

const opponentWonMsg = `
    The winner is ${opponent}! ${player} lost the game!
`

// ANNOUNCING THE WINNER
if (hasWon) {
    console.log(playerWonMsg)
} else {
    console.log(opponentWonMsg)
}

// Go through all variables and decide if they should be let or const ✅
// Change the console logs to use template strings instead of double quotes