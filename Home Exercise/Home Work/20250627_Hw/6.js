let phrase = "Мама мыла раму";
let spaceIndices = [];

for (let i = 0; i < phrase.length; i++) {
  if (phrase[i] === " ") {
    spaceIndices.push(i);
  }
}

console.log("Номера символов, содержащие пробелы:", spaceIndices);