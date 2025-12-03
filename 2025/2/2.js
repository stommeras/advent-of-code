const fs = require("fs");
const path = require("path");
const filePath = process.argv[2] || path.join(__dirname, "in");

fs.readFile(filePath, "utf8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  const invalidIds = new Set();

  data.split(",").forEach((range) => {
    const [start, end] = range.split("-");

    for (let i = parseInt(start); i <= parseInt(end); i++) {
      const num = i.toString();
      const len = num.length;

      if (len % 2 !== 0) {
        i = Math.pow(10, len);
      }

      if (len % 2 === 0) {
        const mid = len / 2;
        const firstHalf = num.slice(0, mid);
        const secondHalf = num.slice(mid);

        if (firstHalf === secondHalf) {
          invalidIds.add(i);
        }
      }
    }
  });

  console.log("----- Part 1 -----");
  console.log(
    "Sum of invalid IDs:",
    Array.from(invalidIds).reduce((a, b) => a + b, 0)
  );
});

fs.readFile(filePath, "utf8", (err, data) => {
  if (err) {
    console.error("Error reading file:", err);
    return;
  }

  const invalidIds = new Set();

  data.split(",").forEach((range) => {
    const [start, end] = range.split("-");

    for (let i = parseInt(start); i <= parseInt(end); i++) {
      const regex = /^(\w+)\1+$/;
      if (regex.test(i.toString())) {
        invalidIds.add(i);
      }
    }
  });

  console.log("\n----- Part 2 -----");
  console.log(
    "Sum of invalid IDs:",
    Array.from(invalidIds).reduce((a, b) => a + b, 0)
  );
});
