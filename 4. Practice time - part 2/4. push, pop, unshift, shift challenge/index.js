let largeCountries = ["Tuvalu","India","USA","Indonesia","Monaco"]

// You need to help me fixup the largeCountries array so that 
// China and Pakistan are added back into their respective places

// Use push() & pop() and their counterparts unshift() & shift()
// Google how to use unshift() and shift()

/* 
* https://linuxhint.com/javascript-array-shift-and-unshift-method/#:~:text=Conclusion,item%20to%20the%20next%20index.
* The shift() method in JavaScript removes an item from the beginning of an array and shifts every other item to the previous index, whereas the unshift() method adds an item to the beginning of an array while shifting every other item to the next index.
*/

// removing Tuvalu, adding China
largeCountries.shift()
largeCountries.unshift("China")

// removing Monaco, adding Pakistan
largeCountries.pop()
largeCountries.push("Pakistan")

console.log(largeCountries)