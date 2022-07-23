// ORDER from customer
// FETCH ingredients
// START production
// SERVE function

// place ORDER (2)
// cut fruit (2)
// add water and ice (1)
// start machine (1)
// select container (2)
// select toppings (3)
// serve icecream (2)

// if we dont get the order, we can't start the production
// store room: BACK END
// Kitchen: FRONT END
let stocks = {
    Fruits : ["Apple", "Banana", "Strawberry", "Grapes"],
    Liquid : ["Water", "Ice"],
    Holder: ["Cone", "Cup", "Stick"],
    Toppings: ["Chocolate", "Peanuts"]
}

// from the customer; everytime we get the order
let order = (Fruit_name, call_production) => {
    setTimeout( () => {
        console.log(`${stocks.Fruits[Fruit_name]} was selected`);
        call_production(); // wont start production until fruit is selected 
    }, 2000);
    
};

// production of ice cream
let production = () => {
    setTimeout( () => {
        console.log("Production has started");

        setTimeout( () => {
            console.log("The fruit has been chopped.");

            setTimeout( () => {
                console.log(`${stocks.Liquid[0]} and ${stocks.Liquid[1]} was added`);

                setTimeout( () => {
                    console.log("Machine has been started.");

                    setTimeout( () => {
                        console.log(`Ice cream was placed on the ${stocks.Holder[0]}`);

                        setTimeout( () => {
                            console.log(`Topping ${stocks.Toppings[1]} was added`);

                            setTimeout( () => {
                                console.log("Served Ice Cream!");
                            }, 2000);

                        }, 3000);

                    }, 2000);

                }, 1000);

            }, 1000);

        }, 2000);

    }, 0000);
};

order(0, production);
// Order Placed. Please call production.
// Order received. Starting production.
