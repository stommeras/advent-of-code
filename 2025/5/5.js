const fs = require("fs");
const path = require("path");
const filePath = process.argv[2] || path.join(__dirname, "in");

const data = fs.readFileSync(filePath, "utf8");
const [ranges, ids] = data.trim().split("\r\n\r\n");

let available = 0;

for (const id of ids.split("\n")) {
  const idNum = Number(id);
  for (const range of ranges.split("\n")) {
    const [start, end] = range.trim().split("-").map(Number);
    if (idNum >= start && idNum <= end) {
      available++;
      break;
    }
  }
}

console.log("----- Part 1 -----");
console.log("Available:", available);

const rangeList = ranges.split("\n").map(line => {
  const [start, end] = line.trim().split("-").map(Number);
  return { start, end };
}).sort((a, b) => a.start - b.start);

const merged = [];
for (const range of rangeList) {
  if (merged.length === 0 || merged[merged.length - 1].end < range.start - 1) {
    merged.push(range);
  } else {
    merged[merged.length - 1].end = Math.max(merged[merged.length - 1].end, range.end);
  }
}

const totalFreshIds = merged.reduce((sum, range) => sum + (range.end - range.start + 1), 0);

console.log("\n----- Part 2 -----");
console.log("Fresh IDs:", totalFreshIds);