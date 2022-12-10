const fs = require('fs');

const a = fs.readFileSync('input.txt', 'utf-8').split('\n');

let total = 0;
a.forEach((x) => {
    const length = x.length;
    const firstHalf = x.slice(0, length / 2);
    const secondHalf = x.slice(length / 2);
    for (const char of firstHalf) {
        if (secondHalf.includes(char)) {
          const index = firstHalf.indexOf(char);
          const number = firstHalf.charCodeAt(index);
          if (number <= 90) {
            total += number - 'A'.charCodeAt(0) + 27;
          } else if (number <= 122) {
            total += number - 'a'.charCodeAt(0) + 1;
          }
         break;
        }
    }
});
console.log(total);
