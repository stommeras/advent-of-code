const fs = require("fs");
const path = require("path");
const filePath = process.argv[2] || path.join(__dirname, "in");

fs.readFile(filePath, "utf8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  let current = 50;
  let zeroes = 0;

  data.split("\n").map((line) => {
    const dir = line[0];
    const num = parseInt(line.slice(1));

    if (dir === "L") {
      current -= num;
    } else if (dir === "R") {
      current += num;
    }

    while (current < 0) {
      current = 100 + current;
    }

    while (current >= 100) {
      current = current - 100;
    }

    if (current === 0) {
      zeroes += 1;
    }
  });

  console.log("----- Part 1 -----");
  console.log("Zeroes:", zeroes);
});

fs.readFile(filePath, "utf8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  let current = 50;
  let zeroes = 0;

  data.split("\n").map((line) => {
    const dir = line[0];
    let num = parseInt(line.slice(1));

    if (dir === "L") {
      while (num-- > 0) {
        current--;
        if (current < 0) current = 99;
        if (current === 0) zeroes++;
      }
    } else if (dir === "R") {
      while (num-- > 0) {
        current++;
        if (current > 99) current = 0;
        if (current === 0) zeroes++;
      }
    }
  });

  console.log("\n----- Part 2 -----");
  console.log("Zeroes:", zeroes);
});
