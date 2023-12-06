const fs = require('fs');

const a = fs.readFileSync('input.txt', 'utf-8').split('\n');

let total = 0;
for (let i = 0; i < a.length; i += 3) {
  const first = a[i];
  const second = a[i + 1];
  const third = a[i + 2];
  for (const char of first) {
    if (second.includes(char) && third.includes(char)) {
      const index = first.indexOf(char);
      const number = first.charCodeAt(index);
      if (number <= 90) {
        total += number - 'A'.charCodeAt(0) + 27;
      } else if (number <= 122) {
        total += number - 'a'.charCodeAt(0) + 1;
      }
      break;
    }
  }
}
console.log(total);
