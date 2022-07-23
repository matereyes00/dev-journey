// synchronous - prints it 1 by one. If one process gets stuck, everything else is affected.
console.log(" I ");
console.log(" eat ");

// asynchronous fxn
//setTimer: runs a function after a certian amount of time
// args, time (ms)
setTimeout(()=>{
    console.log(" ice cream "); // prints after 4 seconds
}, 4000)

console.log(" with a ");
console.log(" spoon ");

// what if u wanna move the word spoon
// console.log(" I ");
// console.log(" eat ");
// console.log(" spoon ");
// console.log(" ice cream ");
// console.log(" with a ");

