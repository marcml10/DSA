let email = "alex.jones@google.com";
let modified = email.split(/[@.]/);
for (let i = 0; i < modified.length ; i ++) {
    if (i==2) {
        console.log(modified[i])
    }
}