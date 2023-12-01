// Some cool Array.from usage
// Inspired solution from reddit

const fs = require('fs');

function parseInput() {
  const input = fs.readFileSync('./input.txt', 'utf8');
  const rocks = input.split('\n').map(a => a.split(' -> ').map(b => {
    const x = parseInt(b.split(',')[0]);
    const y = parseInt(b.split(',')[1]);
    return [x, y];
  }));

  const maxX = Math.max(...rocks.map(a => Math.max(...a.map(b => b[0]))));
  const maxY = Math.max(...rocks.map(a => Math.max(...a.map(b => b[1]))));

  const cave = Array.from({ length: maxY + 1}, () => Array.from({ length: maxX * 2 }, () => '.'));

  cave[0][500] = '+';

  const fillLine = (start, end) => {
    const [x1, y1] = start;
    const [x2, y2] = end;
    const xChanges = x1 !== x2;
    const [min, max] = xChanges ? [x1, x2].sort() : [y1, y2].sort();
    for (let i = min; i <= max; i++) {
      cave[xChanges ? y1: i][xChanges ? i : x1] = '#';
    }
  }

  rocks.forEach(a => a.reduce((last, next) => (fillLine(last, next), next)));
  return cave;
}

function addSand(cave) {
  let sand = [500, 0];
  if (cave[sand[1]][sand[0]] === 'o') throw new Error('bruh');
  while (true) {
    const [x, y] = sand;
    if (y === cave.length - 1) throw new Error('bruh2');
    else if (cave[y + 1][x] === '.') sand = [x, y + 1];
    else if (x < 0) throw new Error('bruh3');
    else if (cave[y + 1][x - 1] === '.') sand = [x - 1, y];
    else if (x > cave[0].length - 1) throw new Error('bruh4');
    else if (cave[y + 1][x + 1] === '.') sand = [x + 1, y];
    else break;
  }

  cave[sand[1]][sand[0]] = 'o';
}

function part1(cave) {
  let count = -1;
  while (true) {
    try {
      count++;
      addSand(cave);
    } catch(err) {
      return count;
    }
  }
}

function part2() {
  const grid = parseInput();
  const cave = JSON.parse(JSON.stringify(grid)).concat(Array.from({ length: 2 }, (_, i) => Array.from({ length: grid[0].length }, () => (i ? '#' : '.'))));

  return part1(cave);
}

console.log(part1(parseInput()));
console.log(part2());
