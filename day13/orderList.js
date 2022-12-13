const fs = require('fs');

function parseInput() {
  const input = fs.readFileSync('./input.txt', 'utf8').split('\n\n');
  const pairs = input.map(a => {
    const first = JSON.parse(a.split('\n')[0]);
    const second = JSON.parse(a.split('\n')[1]);
    return [first, second];
  });

  return pairs;
}

function compare(a, b) {
  if (typeof a === 'number' && typeof b === 'number') {
    return a < b ? true : a > b ? false : undefined;
  } else if (typeof a === typeof b) {
    for (let i = 0; i < a.length && i < b.length; i++) {
      const cmp = compare(a[i], b[i]);
      if (cmp !== undefined) {
        return cmp;
      }
    }
    return a.length < b.length ? true : a.length > b.length ? false : undefined;
  } else {
    let nA = typeof a === 'number' ? [a] : a;
    let nB = typeof b === 'number' ? [b] : b;
    return compare(nA, nB);
  }
}

function part1() {
  const pairs = parseInput();

  let result = 0;
  let i = 0;

  for (const [a, b] of pairs) {
    i++;
    if (compare(a, b)) {
      result += i;
    }
  }

  return result;
}

function part2() {
  const pairs = parseInput();

  const merge = [];
  for (const [a, b] of pairs) {
    merge.push(a, b);
  }

  const divider1 = [[2]];
  const divider2 = [[6]];
  merge.push(divider1, divider2);

  merge.sort((a, b) => compare(a, b) ? -1 : 1);
  return (merge.indexOf(divider1) + 1) * (merge.indexOf(divider2) + 1);
}


console.log(part1());
console.log(part2());
