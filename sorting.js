let storeItems = [
    { product: "Laptop", price: 1200 },
    { product: "Mouse", price: 25 },
    { product: "Keyboard", price: 80 }
];

for (let i=0; i<storeItems.length; i++) {
    for (let j=i+1; j<storeItems.length; j++) {
        if (storeItems[i]["price"] > storeItems[j]["price"]) {
            [storeItems[i], storeItems[j]] = [storeItems[j], storeItems[i]];
        }
    }
}
console.log(storeItems) 