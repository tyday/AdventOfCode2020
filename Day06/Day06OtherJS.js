const fs = require("fs");

const part1 = fs
    .readFileSync("Day06.txt", "utf8")
    .split("\n\n")
    .map((string) => string.replace(/\n/g, ""))
    .reduce((sum, string) =>{
        console.log(sum,string, new Set(string).size)
        sum + new Set(string).size, 0
    });

console.log(part1);