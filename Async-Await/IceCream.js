let stocks = {
    Fruits : ["Apple", "Banana", "Strawberry", "Grapes"],
    Liquid : ["Water", "Ice"],
    Holder: ["Cone", "Cup", "Stick"],
    Toppings: ["Chocolate", "Peanuts"]
}

// serving ice cream?
let isShopOpen = true 

// Promise [WAY 1]
// let order = () => {

//     //making promise
//     return new Promise( (resolve, reject) => {

//         if () {
//             resolve()
//         } 
        
//         else {
//             reject()
//         }
//     })
// }

// // first start
// // works IF PROMISE RESOLVED
// order()
// .then()
// .then()
// .then()
// // works IF PROMISE NOT RESOLVED
// .catch()
// // works BOTH WAYS
// .finally()


// WAY 2: Async Await
async function order ()  {// making a promise
    // 1. TRY 
    // 2. CATCH 
    // 3. FINALLY
    try{
        await abc; //abc is a function that doesnt exist (FAKE FUNCTION)
    }
    catch(error){
        // PRINTS 1. error
        console.log("abc doesn't exist", error)
    }

    finally{
        // PRINTS 2. finally
        console.log("Runs code anyways")
    }
} 

// PRINTS 3. resolved and u can also use (then,try catch, etc.)
order().then( () => {
    console.log("omg cool")
})