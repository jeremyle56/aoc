const fs = require('fs');

const input = fs.readFileSync('input.txt', 'utf-8').split('\n');

// Inital solution was using a cycle counter and [20, 60, 100,...].includes(cycleCounter)
function part1() {
  const changes = [];
  for (const line of input) {
    const split = line.split(' ');
    changes.push(0);
    if (split[0] === 'addx') {
      changes.push(parseInt(split[1]));
    }
  }
  let result = 0;
  let x = 1;
  for (let i = 0; i < changes.length; i++) {
    if (i % 40 === 19) {
      result += (i + 1) * x;
    }
    x += changes[i];
  }

  return result;
}

function part2() {
  const changes = [];
  for (const line of input) {
    const split = line.split(' ');
    changes.push(0);
    if (split[0] === 'addx') {
      changes.push(parseInt(split[1]));
    }
  }
  
  let x = 1;
  for (let i = 0; i < changes.length; i++) {
    if (i % 40 === x - 1 || i % 40 === x || i % 40 === x + 1) {
      process.stdout.write('#');
    } else {
      process.stdout.write('.');
    }
    if (i % 40 === 39) {
      console.log();
    }
    x += changes[i];
  }
}

function part1InitalAttempt() {
  let cycleCounter = 1; // Mistake was had counter start at 0 not 1
  let strength = 0;
  let x = 1;
  for (const line of input) {
    const split = line.split(' ');
    if (split[0] === 'addx') {
      cycleCounter++;
      if ([20, 60, 100, 140, 180, 220].includes(cycleCounter)) {
        strength += x * cycleCounter;
      }
      x += parseInt(split[1]);
    }
    cycleCounter++;
    if ([20, 60, 100, 140, 180, 220].includes(cycleCounter)) {
      strength += x * cycleCounter;
    }
  }

  return strength;
}

console.log(part1());
console.log(part2());
console.log(part1InitalAttempt());
