// Algorithms inspired by solutions on reddit, brain too small to come up with it

const fs = require('fs');

function parseInput() {
  const input = fs.readFileSync('./input.txt', 'utf8');
  const beacons = {};
  const sensors =  input.split('\n').map(a => {
    const sensorX = parseInt(a.split(': ')[0].split(',')[0].split('=')[1]);
    const sensorY = parseInt(a.split(': ')[0].split(',')[1].split('=')[1]);
    const beaconX = parseInt(a.split(': ')[1].split(',')[0].split('=')[1]);
    const beaconY = parseInt(a.split(': ')[1].split(',')[1].split('=')[1]);

    beacons[beaconX + ',' + beaconY] = true;

    return {
      sensorX, 
      sensorY, 
      beaconX, 
      beaconY, 
      distance: Math.abs(sensorX - beaconX) + Math.abs(sensorY - beaconY)
    };
  });

  return {sensors, beacons};
}

function isDistress(edge, sensors) {
  if (edge.x < 0 || edge.x > 4000000 || edge.y < 0 || edge.y > 4000000) return false;

  for (const sensor of sensors) {
    if (sensor.distance >= Math.abs(edge.x - sensor.sensorX) + Math.abs(edge.y - sensor.sensorY)) {
      return false;
    }
  }

  return true;
}

function part1() {
  const {sensors, beacons} = parseInput();

  const notContain = new Set();
  const y = 2000000;
  for (const sensor of sensors) {
    const vertDistance = Math.abs(sensor.sensorY - y);;
    if (vertDistance <= sensor.distance) {
      const horiDistance = sensor.distance - vertDistance;
      for (let i = sensor.sensorX - horiDistance; i <= sensor.sensorX + horiDistance; i++) {
        if (!beacons[i + ',' + y]) {
          notContain.add(i);
        }
      }
    }
  }

  return notContain.size;
}

function part2() {
  const { sensors } = parseInput();

  for (const sensor of sensors) {
    const edges = [];
    for (let i = sensor.distance; i >= 0; i--) {
      edges.push({ x: sensor.sensorX + i + 1, y: sensor.sensorY - Math.abs(sensor.distance - i) });
      edges.push({ x: sensor.sensorX - i - 1, y: sensor.sensorY + Math.abs(sensor.distance - i) });
    }

    for (const edge of edges) {
      if (isDistress(edge, sensors)) {
        return edge;
      }
    }
  }
}


console.log(part1());
const part2Ans = part2();
console.log(part2Ans.x * 4000000 + part2Ans.y);

// Inital solutiont to make a grid (bad idea, at least parsing was correct)
// function parseInput() {
//   const input = fs.readFileSync('./input.txt', 'utf8');
//   let sensors = input.split('\n')
//     .map(a => a.split(': ')[0])
//     .map(a => a.split(',')
//     .map(b => parseInt(b.split('=')[1]))
//     );
//   let beacons = input.split('\n')
//     .map(a => a.split(': ')[1])
//     .map(a => a.split(',')
//     .map(b => parseInt(b.split('=')[1]))
//     );

//   const minX = Math.min(
//     Math.min(...sensors.map(a => a[0])), 
//     Math.min(...beacons.map(a => a[0]))
//   );
//   const minY = Math.min(
//     Math.min(...sensors.map(a => a[1])), 
//     Math.min(...beacons.map(a => a[1]))
//   );

//   if (minX < 0) {
//     const add = Math.abs(minX);
//     sensors = sensors.map(a => [a[0] + add, a[1]]);
//     beacons = beacons.map(a => [a[0] + add, a[1]]);
//   }
//   if (minY < 0) {
//     const add = Math.abs(minY);
//     sensors = sensors.map(a => a[1] + add);
//     sensors = sensors.map(a => a[1] + add);
//   }

//   const maxX =  Math.max(
//     Math.max(...sensors.map(a => a[0])), 
//     Math.max(...beacons.map(a => a[0]))
//   );
//   const maxY = Math.max(
//     Math.max(...sensors.map(a => a[1])), 
//     Math.max(...beacons.map(a => a[1]))
//   );
  
//   const map = Array.from({ length: maxY + 1}, () => Array.from({ length: maxX + 1}, () => '.'));
//   for (const [x, y] of sensors) {
//     map[y][x] = 'S';
//   }
//   for (const [x, y] of beacons) {
//     map[y][x] = 'B';
//   }

//   return {map, sensors};
// }
