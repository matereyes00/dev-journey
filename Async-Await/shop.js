let stocks = {
    Fruits : ["Apple", "Banana", "Strawberry", "Grapes"],
    Liquid : ["Water", "Ice"],
    Holder: ["Cone", "Cup", "Stick"],
    Toppings: ["Chocolate", "Peanuts"]
}

// serving ice cream?
let isShopOpen = true 

// create a new promise 
//create a time function to establish relationship between TIME and WORK
function time(ms) {
    return new Promise( (resolve, reject) => {
        if(isShopOpen) {
            // when shop is open
            // form relationship between time and work
            setTimeout(resolve, ms)
        } else {
            // when shop is closed
            reject(console.log("Shop is closed"))
        }
    });
}

async function kitchen() {
    try{ // STEPS OF MAKING ICE CREAM
        await time(2000)
        console.log(`${stocks.Fruits[0]} was selected`) // how to define 2 seconds?

        await time(0000)
        console.log("Start the production")

        await time(2000)
        console.log("cut the fruit")

        await time(1000)
        console.log(`Added ${stocks.Liquid[0]} and ${stocks.Liquid[1]} was added`)

        await time(1000)
        console.log("Start the machine")

        await time(2000)
        console.log(`Ice cream placed on ${stocks.Holder[1]}`)

        await time(3000)
        console.log(`${stocks.toppings[0]} was selected`)

        await time(2000)
        console.log("Save ice cream")

    }
    catch(error){
        console.log("Customer Left", error)
    }
    finally{
        console.log("Day ended, Shop is closed")
    }
}

kitchen(); // trigger