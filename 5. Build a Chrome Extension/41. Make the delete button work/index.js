let myLeads = []
const inputEl = document.getElementById("input-el")
const inputBtn = document.getElementById("input-btn")
const ulEl = document.getElementById("ul-el")
// 1. Store the delete button in a deleteBtn variable 
const deleteBtn = document.getElementById("delete-btn");

const leadsFromLocalStorage = JSON.parse( localStorage.getItem("myLeads") )
if (leadsFromLocalStorage) {
    myLeads = leadsFromLocalStorage
    console.log(myLeads)
    renderLeads()
}

// 2. Listen for double clicks on the delete button (google it!)
deleteBtn.addEventListener('dblclick', function() {
    // 3. When clicked, clear localStorage, myLeads, and the DOM
    localStorage.clear() 
    myLeads = []
    ulEl.innerHTML = ""
    console.log(myLeads)
    console.log(typeof(myLeads))
})

inputBtn.addEventListener("click", function() {
    myLeads.push(inputEl.value)
    inputEl.value = ""
    localStorage.setItem("myLeads", JSON.stringify(myLeads) )
    renderLeads()

    console.log(myLeads)
    console.log(typeof(myLeads))
})

function renderLeads() { // making leads appear as a string
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


// https://www.codegrepper.com/code-examples/javascript/how+to+listen+for+double+click+in+javascript