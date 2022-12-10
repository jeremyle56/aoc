const fs = require('fs');

const a = fs.readFileSync('input.txt', 'utf-8').split('\n');

let total = 0;
for (const pair of a) {
    const seperate = pair.split(`,`);
    const first = seperate[0].split(`-`);
    const second = seperate[1].split(`-`);
    const firstLower = parseInt(first[0]);
    const firstHigher = parseInt(first[1]);
    const secondLower = parseInt(second[0]);
    const secondHigher = parseInt(second[1]);
    if (firstLower <= secondHigher && firstLower >= secondLower) {
        total++
    } else if (firstHigher >= secondLower && firstHigher <= secondHigher) {
        total++;
    } else if (secondLower >= firstLower && secondLower <= firstHigher) {
        total++;
    } else if (secondHigher >= firstLower && secondHigher <= firstLower) {
        total++;
    }
}
console.log(total);
