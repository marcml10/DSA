let confirmation = "TICKET-98231-VIP";
let counter = 0;
for (let elemenst of confirmation) {
    counter +=1
    if (elemenst === "-") {
        break;
    }
}
console.log(confirmation.slice(counter, counter+5))