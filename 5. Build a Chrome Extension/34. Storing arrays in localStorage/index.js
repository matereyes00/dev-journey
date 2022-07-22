let myLeads = `["www.awesomelead.com"]` 

// 1. turn myLeads string into an array
myLeads = JSON.parse(myLeads)
console.log((myLeads))

// 2. push new value to the array
myLeads.push("www.youtube.com")
console.log((myLeads))

// 3. turn array into a string again
myLeads = JSON.stringify(myLeads)
console.log((myLeads))

// 4. console.log the string using  typeof to verify that it's a string
console.log(typeof(myLeads))

const inputEl = document.getElementById("input-el")
const inputBtn = document.getElementById("input-btn")
const ulEl = document.getElementById("ul-el")

inputBtn.addEventListener("click", function() {
    myLeads.push(inputEl.value)
    inputEl.value = ""
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

// 1. turn myLeads string into an array
// 2. push new value to the array
// 3. turn array into a string again
// 4. console.log the string using  typeof to verify that it's a string