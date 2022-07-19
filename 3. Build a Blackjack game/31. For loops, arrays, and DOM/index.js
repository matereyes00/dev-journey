let sentence = ["Hello", "my", "name", "is", "Per"] 
let greetingEl = document.getElementById("greeting-el")

// Render the sentence in the greetingEl paragraph using a for loop and .textContent
for (let i = 0; i < sentence.length; i++) {
    if (i === sentence.length - 1) {
        greetingEl.textContent += sentence[i] + "."
    } else {
        greetingEl.textContent += sentence[i] + " "
    }
    
}
