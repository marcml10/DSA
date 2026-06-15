// messy user search term, cleans it up, 
// and checks if it contains a banned keyword. 
// This is the {PROBLEM STATEMENT}

let message = "   BUY CHEAP WATCHES!!!   ";
let trimmedOne = message.trim().toLowerCase().split(" ");
for (let message of trimmedOne) {
    if (message == "cheap") {
        console.log("spam detected")
    }
}
