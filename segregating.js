let guests = [
    { name: "Alex", isVIP: true },
    { name: "Sam", isVIP: false },
    { name: "Chris", isVIP: true }
];
for (let i=0; i< guests.length ; i++) {
    if (guests[i]["isVIP"]!=true) {
        guests.splice(i,1)
    }
}
console.log(guests)