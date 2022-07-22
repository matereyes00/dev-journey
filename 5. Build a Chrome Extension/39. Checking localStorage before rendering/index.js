let myLeads = []
const inputEl = document.getElementById("input-el")
const inputBtn = document.getElementById("input-btn")
const ulEl = document.getElementById("ul-el")

// ["lead1", "lead2"] VS null
let leadsFromLocalStorage = JSON.parse( localStorage.getItem("myLeads") ) //getting the array and turning it to object
console.log(leadsFromLocalStorage)

// basically in this part, we want to keep the links on the page itself so when it refreshes, it doesnt go away

// 1. Check if leadsFromLocalStorage is truthy
if (leadsFromLocalStorage) {
    // 2. If so, set myLeads to its value and call renderLeads()
    myLeads = leadsFromLocalStorage
    renderLeads()
}

inputBtn.addEventListener("click", function() {
    myLeads.push(inputEl.value)
    inputEl.value = ""
    localStorage.setItem("myLeads", JSON.stringify(myLeads) )
    renderLeads()

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
