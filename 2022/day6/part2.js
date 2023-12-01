const fs = require('fs');

const input = fs.readFileSync('input.txt', 'utf-8').split('\n');

let num = 0;
for (let i = 0; i < a.length; i++) {
    let bruh = new Set()
    for(let j = 0; j < 14; j++) {
        bruh.add(a[i+j])
    }
    if (bruh.size === 14) {
        num = i + bruh.size;
        break;
    }
}
console.log(num)
