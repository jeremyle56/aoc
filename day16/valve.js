const fs = require('fs');

function parseInput() {
  const input = fs.readFileSync('./input.txt', 'utf8');
  const valves = [];
  input.split('\n').forEach(a => {
    const valve = a.split('Valve ')[1].split(' ')[0];
    const rate = parseInt(a.split('rate=')[1].split(';')[0]);
    const to = a.split('valve')[1].replace('s', '').replace(' ', '').split(', ');
    const tunnels = {};
    to.forEach(a => tunnels[a] = a);
    valves.push({ name: valve, flowRate: rate, tunnels: tunnels });
  });

  return valves;
}

// Attempt 1 - Finds max from each valve (brute force)
// function part1() {
//   const valves = parseInput();

//   const visited = {};
//   for (const valve of Object.keys(valves)) {
//     visited[valve] = false;
//   }

//   let pressureRate = 0;
//   let pressure = 0;
//   let currentValve = 'AA';
//   for (let i = 0; i < 30; i++) {
//     let maxRateValve = 'AA';
//     for (const valve of valves[currentValve].to) {
//       console.log(valve);
//       if (valves[maxRateValve].rate < valves[valve].rate && !visited[valve]) {
//         maxRateValve = valve;
//       }
//     }

//     if (valves[maxRateValve].rate !== 0) {
//       pressureRate += valves[maxRateValve].rate;
//       pressure += pressureRate;
//       currentValve = maxRateValve;
//       visited[maxRateValve] = true;
//       i++;
//     }
//   }

//   return pressure;
// }

// Attempt 2 - sorts valves in highest order (doesn't work to start with AA)
// function calcTime(valve, currValve) {
//   if (currValve === undefined) {
//     return 0;
//   }
//   return 1 + calcTime(valve, valve.tunnels[currValve]);
// }

// function part1() {
//   const valves = parseInput();
//   const sortedValves = valves.sort((v1, v2) => v2.rate - v1.rate);

//   let totalPressureReleased = 0;
//   let timeRemaining = 30;
//   const openedValves = new Set();

//   let startingValve = valves.find(v => v.name === 'AA');
//   const timeNeeded = calcTime(startingValve, startingValve.name);
//   timeRemaining -= timeNeeded;

//   while (timeRemaining > 0) {
//     let highestFlowRateValue = null;
//     let highestFlowRate = -1;
//     for (const valve of sortedValves) {
//       if (!openedValves.has(valve.name) && calcTime(valve, valve.name) <= timeRemaining) {
//         if (valve.flowRate > highestFlowRate) {
//           highestFlowRateValue = valve;
//           highestFlowRate = valve.flowRate;
//         }
//       }
//     }

//     if (highestFlowRateValue === null) {
//       break;
//     }

//     const timeNeeded = calcTime(highestFlowRateValue, highestFlowRateValue.name);
//     timeRemaining -= timeNeeded;

//     totalPressureReleased += highestFlowRateValue.flowRate * timeRemaining;
//     openedValves.add(highestFlowRateValue.name);
//   }

//   return totalPressureReleased;
// }

// console.log(part1());
