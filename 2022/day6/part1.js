const fs = require('fs');

const a = fs.readFileSync('input.txt', 'utf-8')

let num = 0;
for (let i = 0; i < a.length; i++) {
    const bruh = new Set([a[i],a[i+1],a[i+2],a[i+3]])
    if (bruh.size === 4) {
        num = i;
        break;
    }
}
console.log(num);
