const fs = require('fs');

const a = fs.readFileSync('input.txt', 'utf-8').split('\n');

let total = 0;
for (const pair of a) {
    const seperate = pair.split(`,`);
    const first = seperate[0].split(`-`);
    const second = seperate[1].split(`-`);
    if (parseInt(first[0]) <= parseInt(second[0]) && parseInt(first[1]) >= parseInt(second[1])) {
        total++;
    } else if (parseInt(second[0]) <= parseInt(first[0]) && parseInt(second[1]) >= parseInt(first[1])) {
        total++;
    }
}
console.log(total);
