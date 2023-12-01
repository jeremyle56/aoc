const fs = require('fs');

function parseInput() {
  const input = fs.readFileSync('input.txt', 'utf-8').split('\n\n');
  let monkeysInput = input.map(a => a.split('\n'));
  const monkeys = [];
  for (const monk of monkeysInput) {
    const start = monk[1].split(':')[1].split(',').map(a => parseInt(a));
    const operation = monk[2].split('= old')[1].replace(' ', '').split(' ');
    const divisor = parseInt(monk[3].split('by ')[1]);
    const trueCase = parseInt(monk[4].split('monkey ')[1]);
    const falseCase = parseInt(monk[5].split('monkey ')[1]);
    const monkey = {start, operation, divisor, trueCase, falseCase};
    monkeys.push(monkey);
  }

  return monkeys;
}

function part1() {
  const monkeys = parseInput();

  const inspect = new Array(monkeys.length).fill(0);
  const items = monkeys.map(a => a.start);
  for (let i = 0; i < 20; i++) {
    for (let j = 0; j < monkeys.length; j++) {
      while (items[j].length !== 0) {
        let item = items[j][0];
        inspect[j]++;
        if (monkeys[j].operation[0] === '*') {
          if (monkeys[j].operation[1] === 'old') {
            item *= item;
          } else {
            item *= parseInt(monkeys[j].operation[1]);
          }
        } else if (monkeys[j].operation[0] === '+') {
          if (monkeys[j].operation[1] === 'old') {
            item += item;
          } else {
            item += parseInt(monkeys[j].operation[1]);
          }
        }

        item = Math.floor(item / 3);
        if (item % monkeys[j].divisor === 0) {
          items[monkeys[j].trueCase].push(item);
        } else {
          items[monkeys[j].falseCase].push(item);
        }
        items[j].shift();
      }
    }
  }

  inspect.sort((a, b) => b - a);
  return inspect[0] * inspect[1];
}

function part2() {
  const monkeys = parseInput();

  const inspect = new Array(monkeys.length).fill(0);
  const items = monkeys.map(a => a.start);
  const mod = monkeys.reduce((a, b) => a * b.divisor, 1);

  for (let i = 0; i < 10000; i++) {
    for (let j = 0; j < monkeys.length; j++) {
      while (items[j].length !== 0) {
        let item = items[j][0];
        inspect[j]++;

        if (monkeys[j].operation[0] === '*') {
          if (monkeys[j].operation[1] === 'old') {
            item *= item;
          } else {
            item *= parseInt(monkeys[j].operation[1]);
          }
        } else if (monkeys[j].operation[0] === '+') {
          if (monkeys[j].operation[1] === 'old') {
            item += item;
          } else {
            item += parseInt(monkeys[j].operation[1]);
          }
        }

        item %= mod;
        if (item % monkeys[j].divisor === 0) {
          items[monkeys[j].trueCase].push(item);
        } else {
          items[monkeys[j].falseCase].push(item);
        }
        items[j].shift();
      }
    }
  }

  inspect.sort((a, b) => b - a);
  return inspect[0] * inspect[1];
}

function mergeSolution(part2) {
  const monkeys = parseInput();

  const inspect = new Array(monkeys.length).fill(0);
  const items = monkeys.map(a => a.start);
  const mod = monkeys.reduce((a, b) => a * b.divisor, 1);

  for (let i = 0; i < (part2 === true ? 10000: 20); i++) {
    for (let j = 0; j < monkeys.length; j++) {
      while (items[j].length !== 0) {
        let item = items[j][0];
        inspect[j]++;

        // Shorter solution would use eval, which requires different parse
        if (monkeys[j].operation[0] === '*') {
          if (monkeys[j].operation[1] === 'old') {
            item *= item;
          } else {
            item *= parseInt(monkeys[j].operation[1]);
          }
        } else if (monkeys[j].operation[0] === '+') {
          if (monkeys[j].operation[1] === 'old') {
            item += item;
          } else {
            item += parseInt(monkeys[j].operation[1]);
          }
        }

        part2 === true ? item %= mod : item = Math.floor(item / 3);
        if (item % monkeys[j].divisor === 0) {
          items[monkeys[j].trueCase].push(item);
        } else {
          items[monkeys[j].falseCase].push(item);
        }
        items[j].shift();
      }
    }
  }

  inspect.sort((a, b) => b - a);
  return inspect[0] * inspect[1];
}

// console.log(part1());
// console.log(part2());
console.log(mergeSolution(false));
console.log(mergeSolution(true));
