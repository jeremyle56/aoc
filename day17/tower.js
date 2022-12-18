const fs = require('fs');
const { parse } = require('path');

function parseInput() {
  const input = fs.readFileSync('./input.txt', 'utf-8');
  const rocks = [[['#','#','#','#']], [['.','#','.'], ['#','#','#'], ['.','#','.']], ['.','.','#'], ['.','.','#'], ['#','#','#'], [['#'], ['#'], ['#'], ['#']], [['#', '#'], ['#', '#']]];

  return { input, rocks };
}

// Doesn't factor in the shapes of the rocks
// function part1() {
//   const { input, rocks } = parseInput();

//   let shape = 0;
//   let pileHeight = 0;
//   let down = pileHeight + 4;
//   for (let i = 0; i < 2021;) {
//     for (const dir of input) {
//       let left = 0;
//       let right = 0;
//       let height = 0; 
//       switch (shape) {
//         case 0: left = 2, right = 5, height = 1; break;
//         case 1: left = 2, right = 4, height = 3; break;
//         case 2: left = 2, right = 4, height = 3; break;
//         case 3: left = 2, right = 2, height = 4; break;
//         case 4: left = 2, right = 3, height = 2; break;
//       }
//       console.log(shape, height);
  
//       if (dir === '>' && right + 1 < 7) {
//         left += 1;
//         right += 1;
//       } else if (dir === '<' && left - 1> 0){
//         left -= 1;
//         right -= 1;
//       }
  
//       down--;
//       if (down === pileHeight) {
//         pileHeight += height;
//         down = pileHeight + 4;
//         shape = (shape + 1) % 5;
//         i++;
//       }

//       if (i === 2020) {
//         return pileHeight;
//       }
//     }
//   }

//   return pileHeight;
// }

console.log(part1());