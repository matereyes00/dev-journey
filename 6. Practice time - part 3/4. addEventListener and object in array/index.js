let data = [
    {
        player: "Jane",
        score: 52
    }, 
    {
        player: "Mark",
        score: 41
    }
]

// Fetch the button from the DOM, store it in a variable
const logBtn = document.getElementById("log-btn");
// Use addEventListener() to listen for button clicks
logBtn.addEventListener("click", function() {
    // Log Jane's score when the button is clicked (via data)
    for (let i = 0; i < data.length; i++) {
        if (data[i].player === "Jane") {
            console.log(data[i].score);
        } 
    }
    //console.log(data[0].score)
})
