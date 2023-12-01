const fs = require('fs')

const input = fs.readFileSync('./input.txt', 'utf-8');
const monkeys = [];
input.split('\n').forEach(a => {
  monkey = a.split(': ')[0];
  math = a.split(': ')[1];
  monkeys.push({ name: monkey, math });
});

const findMonkey = (name) => {
  return monkeys.find(a => a.name === name);
}

const compute = ({ math }) => {
  if (!isNaN(parseInt(math))) return math;
  if (math === 'x') return math;
  const first = compute(findMonkey(math.split(' ')[0]));
  const second = compute(findMonkey(math.split(' ')[2]));
  const operation = math.split(' ')[1];

  return `(${first})${operation}(${second})`;
}
 
const part1 = ({ math }) => {
  if (math.match(/^[a-zA-Z+\-*\/ ]+$/)) {
    const first = math.split(' ')[0];
    const second = math.split(' ')[2];
    const operation = math.split(' ')[1];

    if (operation === '+') {
      return part1(findMonkey(first)) + part1(findMonkey(second));
    } else if (operation === '-') {
      return part1(findMonkey(first)) - part1(findMonkey(second));
    } else if (operation === '*') {
      return part1(findMonkey(first)) * part1(findMonkey(second));
    } else {
      return part1(findMonkey(first)) / part1(findMonkey(second));
    }
  } else {
    return parseInt(math);
  }
}

const part2 = () => {
  findMonkey('root').math = 'pvgq = ngpl';
  findMonkey('humn').math = 'x';

  return compute(findMonkey('root'))
};

// Shorter equation (abuses pattern in input)
// const part2 = () => {
//   findMonkey('root').math = 'pvgq = ngpl';
//   findMonkey('humn').math = 'x';

//   const { math } = findMonkey('root');
//   const first = findMonkey(math.split(' ')[0]);
//   const second = findMonkey(math.split(' ')[2]);
//   const firstFirst = findMonkey(first.math.split(' ')[0]);
//   const firstSecond = findMonkey(first.math.split(' ')[2]);
//   return `${compute(firstFirst)}*${part1(firstSecond)}=${part1(second)}`
// }

console.log(part1(findMonkey('root')));
// Used online equation solver to find unknown
console.log(part2());


// Attempted manual computre - chains too long
// 34519614933704
// pvgq: jmbh * 8



// jmbh: 954 + jtsn
// jtsn: ztmb / jphw
// ztmb: bnqd - vdzc
// bnqd: ncml * gjbz
// ncml: 13 * jdff
// jdff: qlws / dwtg
// qlws: bjph + mcfw
// bjph: vggv * wnjs
// vggv: 3985 + tjdw
// tjdw: 1223 + whzj
// whzj: jqsv + lncv
// jqsv: 2 * lclp
// lclp: 1808 + hvsn
// hvsn: zsdb / qgsh
// zsdb: gqzc + wrwl
// gqzc: fnwl * wmbm
// fnwl: 70 + zssw
// zssw: sdjd + fghp
// sdjd: qqpv + gcfc






