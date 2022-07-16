// When the user clicks the purchase button, render out
// "Something went wrong, please try again" in the paragraph
// that has the id="error".

let purchaseBtn = document.getElementById("purchase-btn")
let errorEl = document.getElementById("error")
let error_msg = "Something went wrong, please try again"

function message() {
    errorEl.textContent = error_msg
}

