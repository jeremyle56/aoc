const fs = require('fs')

const North = [{ x: -1, y: -1 }, { x: 0, y: -1 }, { x: 1, y: -1 }];
const South = [{ x: -1, y: 1 }, { x: 0, y: 1 }, { x: 1, y: 1 }];
const East = [{ x: 1, y: -1 }, { x: 1, y: 0 }, { x: 1, y: 1 }];
const West = [{ x: -1, y: -1 }, { x: -1, y: 0 }, { x: -1, y: 1 }];
let moves = [North, South, West, East];

const grid = new Set()
const elves = [];

const input = fs.readFileSync('./input.txt', 'utf-8');
input.split('\n').forEach((line, y) => {
  line.split('').forEach((char, x) => {
    if (char === '#') {
      grid.add(`${x},${y}`);
      elves.push({ x, y });
        }
    });
});

const solve = () => {
  for (let i = 1; i < Number.MAX_SAFE_INTEGER; i++) {
    let toMove = [];

    elves.forEach((elve, id) => {
      let count = 0;
      let pos = elve;
      for (let move of moves) {
        if (move.every(e => !grid.has(`${elve.x + e.x},${elve.y + e.y}`))) {
          if (count === 0) {
            pos = { x: elve.x + move[1].x, y: elve.y + move[1].y };
          }
          count++;
        }
      }

      if (count < 4 && count !== 0) {
        toMove.push([id, pos]);
      }
    });

    toMove.forEach(move => {
      if (toMove.filter(e => e[1].x === move[1].x && e[1].y === move[1].y).length === 1) {
        grid.delete(`${elves[move[0]].x},${elves[move[0]].y}`);
        elves[move[0]] = move[1];
        grid.add(`${move[1].x},${move[1].y}`)
      }
    });

    moves.push(moves.shift());

    if (i === 10) {
      let maxX = elves[0].x;
      let minX = maxX;
      let maxY = elves[0].y;
      let minY = maxY;
      for (let elve of elves) {
        if (elve.x > maxX) maxX = elve.x;
        if (elve.x < minX) minX = elve.x;
        if (elve.y > maxY) maxY = elve.y;
        if (elve.y < minY) minY = elve.y;
      }
      let empty = (maxX - minX + 1) * (maxY - minY + 1) - elves.length;
      console.log(empty);
    }

    if (toMove.length === 0) {
      console.log(i);
      break;
    }
  }
}

solve();
