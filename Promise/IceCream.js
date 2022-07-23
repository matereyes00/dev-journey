let stocks = {
    Fruits : ["Apple", "Banana", "Strawberry", "Grapes"],
    Liquid : ["Water", "Ice"],
    Holder: ["Cone", "Cup", "Stick"],
    Toppings: ["Chocolate", "Peanuts"]
}

// serving ice cream?
let isShopOpen = true 

// promise to the customer?
let order = (time, work) => {
    return new Promise((resolve, reject) =>{
        if (isShopOpen) { // if shop is open
            setTimeout( ()=>{ 
                resolve(work()); 
            }, time) // icecream is served, basta der r materials
        } else { // shop is closed
            reject(console.log("Our shop is closed"));
        }
    });
};

order(2000, ()=>console.log(`${stocks.Fruits[2]} was selected`))

// Promise chaining
// starting production
.then( ()=>{
    return order(0000, () => console.log("Production has started."));
})

// chopping the food
.then( () => {
    return order(2000, ()=>console.log("The fruit was chopped."));
})

// adding water and ice
.then( () => {
    return order(1000, () => console.log(`${stocks.Liquid[0]} and ${stocks.Liquid[1]} were added.`));
})

// starting the machine
.then( () => {
    return order(1000, () => {
        console.log("The machine has started.");
    })
})

// selecting a container
.then( () => {
    return order(2000, () => {
        console.log(`${stocks.Holder[2]} has been selected as ice cream container`)
    })
})

.then( () => {
    return order(3000, () => {
        console.log(`${stocks.Toppings[1]} topping selected`);
    })
})

.then( () => {
    return order(2000, () => console.log("Ice-cream served!"));
})

// error handling
// only works when promise is rejected 
// aka no ingredients for the icecream
.catch( () => {
    console.log("Customer left")
})

// run whether promise is resolved or rejected
.finally( () => {
    console.log("Day ended. The shop is closed.")
})