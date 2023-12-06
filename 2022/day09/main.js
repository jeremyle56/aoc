const fs = require('fs');

const input = fs.readFileSync('input.txt', 'utf-8').split('\n');

const directions = input.map(a => a.split(' ')[0]);
const numMoves = input.map(a => parseInt(a.split(' ')[1]))
let offset = {
  R: [1, 0],
  L: [-1, 0],
  U: [0, 1],
  D: [0, -1],
};

class ArraySet extends Set {
  add(arr) {
    super.add(arr.toString());
  }
}

function part1() {
  let headX = 0, headY = 0;
  let tailX = 0, tailY = 0;
  let tailSeen = new ArraySet([[0 , 0]]);

  for (let i = 0; i < directions.length; i++) {
    let [dx, dy] = offset[directions[i]];
    for (let j = 0; j < numMoves[i]; j++) {
      headX += dx;
      headY += dy;
      while (Math.max(Math.abs(tailX - headX), Math.abs(tailY - headY)) > 1) {
        if (Math.abs(tailX - headX) > 0) {
          headX > tailX ? tailX += 1 : tailX += -1;
        }
        if (Math.abs(tailY - headY) > 0) {
          headY > tailY ? tailY += 1: tailY += -1;
        }
        tailSeen.add([tailX, tailY]);
      }
    }
  }

  return tailSeen.size;
}

function part2() {
  let rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]];
  let tailSeen = new ArraySet();

  for (let i = 0; i < directions.length; i++) {
    let [dx, dy] = offset[directions[i]];
    for (let j = 0; j < numMoves[i]; j++) {
      let [headX, headY] = rope[0];
      rope[0] = [headX + dx, headY + dy];

      for (let k = 1; k < rope.length; k++) {
        let [prevX, prevY] = rope[k - 1];
        let [currX, currY] = rope[k];
        while (Math.max(Math.abs(currX - prevX), Math.abs(currY - prevY)) > 1) {
          if (Math.abs(currX - prevX) > 0) {
            currX += (prevX > currX ? 1 : -1);
          }
          if (Math.abs(currY - prevY) > 0) {
            currY += (prevY > currY ? 1 : -1);
          }
        }
        rope[k] = [currX, currY];
      }
      tailSeen.add([rope[9]]);
    }
  }

  return tailSeen.size;
}

function smartSolution(n) {
  let rope = [];
  for (let i = 0; i < n; i++) {
    rope.push([0, 0]);
  }
  let tailSeen = new ArraySet();

  for (let i = 0; i < directions.length; i++) {
    let [dx, dy] = offset[directions[i]];
    for (let j = 0; j < numMoves[i]; j++) {
      let [headX, headY] = rope[0];
      rope[0] = [headX + dx, headY + dy];

      for (let k = 1; k < n; k++) {
        let [prevX, prevY] = rope[k - 1];
        let [currX, currY] = rope[k];
        while (Math.max(Math.abs(currX - prevX), Math.abs(currY - prevY)) > 1) {
          if (Math.abs(currX - prevX) > 0) {
            currX += (prevX > currX ? 1 : -1);
          }
          if (Math.abs(currY - prevY) > 0) {
            currY += (prevY > currY ? 1 : -1);
          }
        }
        rope[k] = [currX, currY];
      }
      tailSeen.add([rope[n - 1]]);
    }
  }

  return tailSeen.size;
}

console.log(part1());
console.log(part2());
console.log(smartSolution(2), smartSolution(10))
