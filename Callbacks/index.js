// callbacks!!
// function within a function
// aka connection between functions

function one (call_two) {
    console.log(" Step 1 complete. Please call step 2 ");
    // making connection between function two and one
    call_two();
}

function two () {
    console.log(" step 2 ");
}

// order: top to bottom
// two();
// one();

one(two);