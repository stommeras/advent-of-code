const fs = require("fs");
const path = require("path");
const filePath = process.argv[2] || path.join(__dirname, "in");

const data = fs.readFileSync(filePath, "utf8");
const grid = data.trim().split("\n").map((line) => line.trim().split(""));

const height = grid.length;
const width = grid[0].length;

const directions = [
  [-1, -1], [-1, 0], [-1, 1],
  [0, -1],           [0, 1],
  [1, -1],  [1, 0],  [1, 1]
];

const countAdjacentRolls = (grid, y, x) => {
  return directions.filter(([dy, dx]) => {
    const newY = y + dy;
    const newX = x + dx;
    return newY >= 0 && newY < height && newX >= 0 && newX < width && grid[newY][newX] === "@";
  }).length;
};

// Part 1
const accessibleRolls = grid
  .flatMap((row, y) => row.map((cell, x) => (cell === "@" && countAdjacentRolls(grid, y, x) < 4 ? 1 : 0)))
  .reduce((sum, val) => sum + val, 0);

console.log("----- Part 1 -----");
console.log("Rolls:", accessibleRolls);

// Part 2
const gridCopy = grid.map(row => [...row]);
let totalRemoved = 0;

while (true) {
  const toRemove = [];

  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      if (gridCopy[y][x] === "@" && countAdjacentRolls(gridCopy, y, x) < 4) {
        toRemove.push([y, x]);
      }
    }
  }

  if (toRemove.length === 0) break;

  toRemove.forEach(([y, x]) => (gridCopy[y][x] = "."));
  totalRemoved += toRemove.length;
}

console.log("\n----- Part 2 -----");
console.log("Total removed:", totalRemoved);