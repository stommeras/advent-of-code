const fs = require("fs");
const path = require("path");
const filePath = process.argv[2] || path.join(__dirname, "in");

fs.readFile(filePath, "utf8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  const lines = data.trim().split("\n");

  const maxJolts = [];

  lines.forEach((line) => {
    const nums = line.trim().split("").map(Number);
    const largest = Math.max(...nums.slice(0, nums.length - 1));
    const largestIndex = nums.indexOf(largest);
    const secondLargest = Math.max(...nums.slice(largestIndex + 1));
    maxJolts.push(Number(largest.toString() + secondLargest.toString()));
  });

  console.log("----- Part 1 -----");
  console.log(
    "Sum of maxjolts: ",
    maxJolts.reduce((a, b) => a + b, 0)
  );
});

fs.readFile(filePath, "utf8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  const lines = data.trim().split("\n");

  const maxJolts = [];

  lines.forEach((line) => {
    const nums = line.trim().split("").map(Number);
    const digits = [];
    let digitsLeft = 12;
    let currentIndex = -1;


    while (digitsLeft-- > 0) {
        const currentNums = [...nums.slice(currentIndex + 1, nums.length - digitsLeft)]
        const largest = Math.max(...currentNums);
        digits.push(largest);
        currentIndex = nums.slice(currentIndex + 1).indexOf(largest) + currentIndex + 1;
    }

    maxJolts.push(Number(digits.join("")))
  });


  console.log("----- Part 2 -----");
  console.log(
    "Sum of maxjolts: ",
    maxJolts.reduce((a, b) => a + b, 0)
  );
});
