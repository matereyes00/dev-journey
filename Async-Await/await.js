let stocks = {
    Fruits : ["Apple", "Banana", "Strawberry", "Grapes"],
    Liquid : ["Water", "Ice"],
    Holder: ["Cone", "Cup", "Stick"],
    Toppings: ["Chocolate", "Peanuts"]
}

// serving ice cream?
let isShopOpen = true 

// where the customer is sitting
let toppings_choice = () => {
    
    // make a new promise
    return new Promise( (resolve, reject) => {
        
        // create setTimeout to ORDER (asking process)
        setTimeout( () => {
            resolve(console.log("which topping would you love?"))
        }, 3000)
        // to go out of the kitchen to ask

    });

};


// steps to be worked on IN THE kitchen
// making ice cream. Realizes they dont know what the customer likes for topping
// customer: chef go out, kitchen stops when chef goes out
async function kitchen() {
    // inside the kitchen
    console.log("A")
    console.log("B")
    console.log("C")

    // remembers what topic likes
    // once chef takes customer's order, steps D and E can be performed
    await toppings_choice()

    console.log("D")
    console.log("E")
}

kitchen()

// these are other people working
// once these tasks are done, go back to chef who asks customer what they want
console.log("doing the dishes")
console.log("cleaning the tables")
console.log("taking others' order")