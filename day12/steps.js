const fs = require('fs');

function parseInput() {
  let start, end;
  const input = fs.readFileSync('./input.txt', 'utf8').split('\n');
  const map = input.map((line, y) => line.split('').map((char, x) => {
    if (char === 'S') {
      start = { x: x, y: y };
      char = 'a';
    } else if (char === 'E') {
      end = { x: x, y: y };
      char = 'z';
    }
    return char.codePointAt(0) - 'a'.codePointAt(0);
  }));

  return { map, start, end };
}


function part1() {
  const { map, start, end } = parseInput();

  let finalPath = [];
  let queue = [];
  let visited = [`${start.x},${start.y}`];

  queue.push([start]);

  while (queue.length > 0 && finalPath.length == 0) {
    let path = queue.shift();
    let pos = path[path.length - 1];

    let dirs = [
      { x: pos.x + 1, y: pos.y },
      { x: pos.x, y: pos.y + 1 },
      { x: pos.x - 1, y: pos.y },
      { x: pos.x, y: pos.y - 1 }
    ];

    for (let dir of dirs) {
      if (dir.x < 0 || dir.x >= map[0].length ||
        dir.y < 0 || dir.y >= map.length ||
        visited.includes(`${dir.x},${dir.y}`) ||
        map[dir.y][dir.x] - map[pos.y][pos.x] > 1) {
        continue;
      }

      if (dir.x == end.x && dir.y == end.y) finalPath = path.concat([end]);
      visited.push(`${dir.x},${dir.y}`);
      queue.push(path.concat([dir]));
    }
  }

  return finalPath.length - 1;
}

// Original solution: Brute force, bfs from every 'a'
// Smart solution: Start from E (end) and find the first 'a'
function part2() {
  const input = fs.readFileSync('./input.txt', 'utf8');
  const map = input.split('\n').map(row => row.split('').map(character => character.charCodeAt(0)));

  let start = { x: 0, y: 0 };

  for (let y = 0; y < map.length; y++) {
    for (let x = 0; x < map[y].length; x++) {
      if (map[y][x] == 'S'.charCodeAt(0)) map[y][x] = 'a'.charCodeAt(0);
      if (map[y][x] == 'E'.charCodeAt(0)) {
        start = { x, y };
        map[y][x] = 'z'.charCodeAt(0);
      }
    }
  }

  let finalPath = [];
  const queue = [];
  const visited = [`${start.x},${start.y}`];

  queue.push([start]);

  while (queue.length > 0 && finalPath.length == 0) {
    const path = queue.shift();
    const pos = path[path.length - 1];

    const dirs = [
      { x: pos.x + 1, y: pos.y },
      { x: pos.x, y: pos.y + 1 },
      { x: pos.x - 1, y: pos.y },
      { x: pos.x, y: pos.y - 1 }
    ];

    for (const dir of dirs) {
      if (dir.x < 0 || dir.x >= map[0].length ||
        dir.y < 0 || dir.y >= map.length ||
        visited.includes(`${dir.x},${dir.y}`) ||
        map[pos.y][pos.x] - map[dir.y][dir.x] > 1) {
        continue;
      }

      if (map[dir.y][dir.x] == 'a'.charCodeAt(0)) finalPath = path.concat([dir]);
      visited.push(`${dir.x},${dir.y}`);
      queue.push(path.concat([dir]));
    }
  }

  return finalPath.length - 1;
}

// Cool recursive solution I found for part1
function dfsSolution() {
  const { map, start, end } = parseInput();

  const stepsMap = Array.from({ length: map.length }, () => Array(map[0].length))

  const adjacent = (x, y, res = []) => {
    if (x > 0 && map[y][x - 1] <= map[y][x] + 1) res.push({ x: x - 1, y: y });
    if (y > 0 && map[y - 1][x] <= map[y][x] + 1) res.push({ x: x, y: y - 1 });
    if (x < map[0].length - 1 && map[y][x + 1] <= map[y][x] + 1) res.push({ x: x + 1, y: y });
    if (y < map.length - 1 && map[y + 1][x] <= map[y][x] + 1) res.push({ x: x, y: y + 1 });
    return res;
  };

  const spread = (x, y, steps) => {
    if (stepsMap[y][x] <= steps) return;
    stepsMap[y][x] = steps;
    adjacent(x, y).forEach(pos => spread(pos.x, pos.y, steps + 1));
  }

  spread(start.x, start.y, 0);
  return stepsMap[end.y][end.x];
}

console.log('DFS Part1: ', dfsSolution());
console.log('BFS Part1: ', part1());
console.log('Smart BFS Part2: ', part2());
