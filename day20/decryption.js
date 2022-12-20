const fs = require('fs');

const parseInput = () => {
  const input = fs.readFileSync('./input.txt', 'utf-8')
  const numbers = input.split('\n').map((n, index) => ({ value: parseInt(n), index}));
  return numbers;
};

const part1 = () => {
  const numbers = parseInput();
  for (let i = 0; i < numbers.length; i++) {
    const currentIndex = numbers.findIndex(({ index }) => index === i);
    const [bruh] = numbers.splice(currentIndex, 1);
    numbers.splice((currentIndex + bruh.value) % numbers.length, 0, bruh);
  }

  const zeroIndex = numbers.findIndex(({ value }) => value === 0);
  const keys = [1000, 2000, 3000].map(a => numbers[(zeroIndex + a) % numbers.length].value);
  return keys.reduce((x, y) => x + y, 0);
}

const part2 = () => {
  const decryptionKey = 811589153;
  const numbers = parseInput().map((n, index) => ({ value: n.value * decryptionKey, index }));

  for (let i = 0; i < numbers.length * 10; i++) {
    const currentIndex = numbers.findIndex(({ index }) => index === i % numbers.length);
    const [bruh] = numbers.splice(currentIndex, 1);
    numbers.splice((currentIndex + bruh.value) % numbers.length, 0, bruh);
  }

  const zeroIndex = numbers.findIndex(({ value }) => value === 0);
  const keys = [1000, 2000, 3000].map(a => numbers[(zeroIndex + a) % numbers.length].value);
  return keys.reduce((x, y) => x + y, 0);
}

console.log(part1());
console.log(part2());