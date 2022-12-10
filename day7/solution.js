const fs = require('fs');

const input = fs.readFileSync('input.txt', 'utf-8').split('\n');

function getFS(input) {
    let fileSystem = { files: {}, dirs: {}};
    let currentDir = fileSystem;
    for (let i = 0; i < input.length; i++) {
        if (input[i].includes('$ cd')) {
            const dir = input[i].split('cd ')[1];
            if (dir === '..') {
                currentDir = currentDir.parent
            } else if (dir === '/') {
                currentDir = fileSystem;
            } else {
                if (!currentDir.dirs[dir]) {
                    currentDir.dirs[dir] = { parent: currentDir, files: {}, dirs: {}}
                }
                currentDir = currentDir.dirs[dir]
            }
        } else if (input[i].includes(`$ ls`)) {
            i++
            while (i < input.length && !input[i].startsWith(`$`)) {
                const [size, name] = input[i].split(' ');
                if (/^\d+$/.test(size)) {
                    currentDir.files[name] = parseInt(size);
                }
                i++
            }
            i--
        }
    }
    return fileSystem
}

function part1(fileSystem) {
    let size = 0;
    let ans = 0;
    
    for (const file in fileSystem.files) {
        size += fileSystem.files[file];
    }
    
    for (const dir in fileSystem.dirs) {
        const [dirSize, dirAns] = part1(fileSystem.dirs[dir]);
        size += dirSize;
        ans += dirAns;
    }
    
    if (size <= 100000) {
        ans += size;
    }
    
    return [size, ans];
}

function part2(fileSystem) {
    const sizes = findSizes2(fileSystem);
    const total = sizes[sizes.length - 1];
    const sizeNeedFree = total - 70000000 + 30000000
    sizes.sort((a, b) => a - b);
    for (const size of sizes) {
        if (size >= sizeNeedFree) {
            return size;
        }
    }
    return -1;
}

function findSizes2(fileSystem) {
    let size = 0;
    let result = [];
    
    for (const file in fileSystem.files) {
        size += fileSystem.files[file]
    }
    
    for (const dir in fileSystem.dirs) {
        const dirSize = findSizes2(fileSystem.dirs[dir])
        size += dirSize[dirSize.length - 1]
        result = result.concat(dirSize)
    }
    result.push(size);
    return result;
}

// console.log(part1(getFS(input)))
console.log(part2(getFS(input)))
