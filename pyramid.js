function pyramid(pattern, rows, booleanInput) {
  let result = "\n"; // Start with a newline character

  if (booleanInput === false) {
    // Vertex up
    for (let i = 1; i <= rows; i++) {
      let spaces = ' '.repeat(rows - i);
      let symbols = pattern.repeat(2 * i - 1);
      result += spaces + symbols + '\n';
    }
  } else {
    // Vertex down
    for (let i = rows; i >= 1; i--) {
      let spaces = ' '.repeat(rows - i);
      let symbols = pattern.repeat(2 * i - 1);
      result += spaces + symbols + '\n';
    }
  }

  return result;
}

