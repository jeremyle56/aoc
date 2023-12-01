const fs = require('fs');

const input = fs.readFileSync('input.txt', 'utf-8').split('\n');

const trees = [];
for (let i = 0; i < input.length; i++) {
  const row = [];
  for (const num of input[i]) {
    row.push(parseInt(num));     
  }
  trees.push(row);
}

function part1(trees) {
  let count = 0;
  for (let i = 0; i < trees.length; i++) {
    for (let j = 0; j < trees[i].length; j++) {
      if (i === 0 || j === 0 || i === trees.length - 1 || j === trees[i].length) {
        count++;
        continue;
      }
  
      let visiable = false;
      let directionVisable = true;
  
      for (let k = i - 1; k >= 0; k--) {
        if (trees[k][j] >= trees[i][j]) {
          directionVisable = false;
          break;
        }
      }
  
      visiable = visiable || directionVisable;
      directionVisable = true;
      for (let k = i + 1; k < trees.length; k++) {
        if (trees[k][j] >= trees[i][j]) {
          directionVisable = false;
          break;
        }
      }
  
      visiable = visiable || directionVisable;
      directionVisable = true;
      for (let k = j - 1; k >= 0; k--) {
        if (trees[i][k] >= trees[i][j]) {
          directionVisable = false;
          break;
        }
      }
  
      visiable = visiable || directionVisable;
      directionVisable = true;
      for (let k = j + 1; k < trees[i].length; k++) {
        if (trees[i][k] >= trees[i][j]) {
          directionVisable = false;
          break;
        }
      }
      
      visiable = visiable || directionVisable;
      if (visiable) {
        count++;
      }
    }
  }
  
  return count
}

function part2(trees) {
  let score = 0;

  for (let i = 0; i < trees.length; i++) {
		for (let j = 0; j < trees[i].length; j++) {
			let upScore = 0;
			let downScore = 0;
			let leftScore = 0;
			let rightScore = 0;

			for (let k = i - 1; k >= 0; k--) {
				upScore++;
				if (trees[k][j] >= trees[i][j]) {
					break;
				}
			}

			for (let k = i + 1; k < trees.length; k++) {
				downScore++;
				if (trees[k][j] >= trees[i][j]) {
					break;
				}
			}

			for (let k = j - 1; k >= 0; k--) {
				leftScore++;
				if (trees[i][k] >= trees[i][j]) {
					break;
				}
			}

			for (let k = j + 1; k < trees[i].length; k++) {
				rightScore++;
				if (trees[i][k] >= trees[i][j]) {
					break;
				}
			}

			score = Math.max(score, upScore * downScore * leftScore * rightScore);
		}
	}

  return score;
}

console.log(part1(trees));
console.log(part2(trees));

