let count = 0
let countEl = document.getElementById("count-el")
console.log(countEl)

function increment() {
    count = count + 1
    // change the count-el in the HTML to reflect the new count
    countEl.innerText = count
    console.log(count)
}


