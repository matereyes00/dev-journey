let myLeads = []
const inputEl = document.getElementById("input-el")

const inputBtn = document.getElementById("input-btn")

inputBtn.addEventListener("click", function() {
    // Push the value from the inputEl into the myLeads array 
    // instead of the hard-coded "www.awesomeleads.com" value
    // Google -> "get value from input field javascript"
    // https://stackoverflow.com/questions/11563638/how-do-i-get-the-value-of-text-input-field-using-javascript
    
    let inputElValue = document.getElementById("input-el").value
    myLeads.push(inputElValue)
    console.log(myLeads)
})


