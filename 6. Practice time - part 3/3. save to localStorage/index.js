// Save a value to localStorage ✅
oneDirection = [
    "Niall", "Zayn", "Harry", "Louis", "Liam"
]
console.log(oneDirection)
localStorage.setItem("oneDirection", JSON.stringify(oneDirection)) // saving into localStorage

strangerThingsKids = [
    "max", "eleven", "mike", "will", "dustin", "lucas"
]
console.log(strangerThingsKids)
localStorage.setItem("strangerThingsKids", JSON.stringify(strangerThingsKids)) // saving into localStorage AS STRING


// Delete your code and refresh the page ✅
// Fetch your value from localStorage and log it out
let fetchedValue = JSON.parse(localStorage.getItem("oneDirection")) // fetching array from local storage (AS OBJECT)
console.log("Fetched item: ", fetchedValue)

let otherFetchedValue = JSON.parse(localStorage.getItem("strangerThingsKids"))
console.log("Other Fetched item: ", otherFetchedValue)