const fs = require('fs');

const parseInput = () => {
  const input = fs.readFileSync('./input.txt', 'utf-8');
  const cubesPos = new Set();
  input.split('\n').map(line => {
    const [x, y, z] = line.split(',').map(n => parseInt(n));
    cubesPos.add(`${x},${y},${z}`);
  });

  return cubesPos;
}

const part1 = (cubesPos) => {
  let surfaceArea = 0;
  for (const cube of cubesPos) {
    const [x, y, z] = cube.split(',').map(n => parseInt(n));
    let count = 6;
    if (cubesPos.has(`${x + 1},${y},${z}`)) count--;
    if (cubesPos.has(`${x - 1},${y},${z}`)) count--;
    if (cubesPos.has(`${x},${y + 1},${z}`)) count--;
    if (cubesPos.has(`${x},${y - 1},${z}`)) count--;
    if (cubesPos.has(`${x},${y},${z + 1}`)) count--;
    if (cubesPos.has(`${x},${y},${z - 1}`)) count--;
    surfaceArea += count;
  }

  return surfaceArea;
}

const part2 = () => {
  const cubesPos = parseInput();
  const minX = Math.min(...[...cubesPos].map(c => parseInt(c.split(',')[0]))); 
  const minY = Math.min(...[...cubesPos].map(c => parseInt(c.split(',')[1])));
  const minZ = Math.min(...[...cubesPos].map(c => parseInt(c.split(',')[2])));
  const maxX = Math.max(...[...cubesPos].map(c => parseInt(c.split(',')[0])));
  const maxY = Math.max(...[...cubesPos].map(c => parseInt(c.split(',')[1])));
  const maxZ = Math.max(...[...cubesPos].map(c => parseInt(c.split(',')[2])));

  const visited = new Set();
  let surfaceArea = 0;
  const dirs = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]];
  const stack = [[0, 0, 0]];

  while (stack.length > 0) {
    const [x, y, z] = stack.pop();
    if (visited.has(`${x},${y},${z}`)) continue;
    if (cubesPos.has(`${x},${y},${z}`)) continue;
    if (x < minX - 1 || y < minY - 1 || z < minZ - 1) continue;
    if (x > maxX + 1 || y > maxY + 1 || z > maxZ + 1) continue;
    visited.add(`${x},${y},${z}`);

    let count = 6;
    if (!cubesPos.has(`${x + 1},${y},${z}`)) count--;
    if (!cubesPos.has(`${x - 1},${y},${z}`)) count--;
    if (!cubesPos.has(`${x},${y + 1},${z}`)) count--;
    if (!cubesPos.has(`${x},${y - 1},${z}`)) count--;
    if (!cubesPos.has(`${x},${y},${z + 1}`)) count--;
    if (!cubesPos.has(`${x},${y},${z - 1}`)) count--;
    surfaceArea += count;

    for (const [dx, dy, dz] of dirs) {
      stack.push([x + dx, y + dy, z + dz]);
    }
  }

  return surfaceArea;
}

console.log(part1(parseInput()));
console.log(part2());