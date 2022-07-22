let myLeads = []
const inputEl = document.getElementById("input-el")
const inputBtn = document.getElementById("input-btn")
const ulEl = document.getElementById("ul-el")

// Get the leads from the localStorage // PARSE 
// Store it in a variable, leadsFromLocalStorage
let leadsFromLocalStorage = JSON.parse(localStorage.getItem("myLeads"))
// Log out the variable
console.log("Leads from local storage: ", leadsFromLocalStorage)

inputBtn.addEventListener("click", function() {
    myLeads.push(inputEl.value) // get value
    inputEl.value = "" // clear input
    localStorage.setItem("myLeads", JSON.stringify(myLeads) ) // store in local storage AS A STRING
    renderLeads()
    
    // To verify that it works:
    console.log( localStorage.getItem("myLeads") )
})

function renderLeads() {
    let listItems = ""
    for (let i = 0; i < myLeads.length; i++) {
        listItems += `
            <li>
                <a target='_blank' href='${myLeads[i]}'>
                    ${myLeads[i]}
                </a>
            </li>
        `
    }
    ulEl.innerHTML = listItems  
}
