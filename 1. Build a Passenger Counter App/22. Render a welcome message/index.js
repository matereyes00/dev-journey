// Grab the welcome-el paragraph and store it in a variable called welcomeEl
let welcomeEl = document.getElementById("welcome-el")
// Create two variables (name & greeting) that contains your name
// and the greeting we want to render on the page
let name = "Martina"
let greeting = "Greetings, earthling "
// Render the welcome message using welcomeEl.innerText
welcomeEl.innerText = greeting + name
console.log(welcomeEl)