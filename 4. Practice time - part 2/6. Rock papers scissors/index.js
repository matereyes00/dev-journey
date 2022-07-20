let hands = ["rock", "paper", "scissor"]

// Create a function that returns a random item from the array
function makeMove() {
    let move = Math.floor( Math.random() * hands.length ) // index 
    let hand = hands[move]
    return hand
}

console.log(makeMove())