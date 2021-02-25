function starOutGrid(grid) {
  const numberOfRows = grid.length;
  const numberOfColumns = grid[0].length;

  // Make lists to keep track of which rows and columns we should clear
  const clearRows = Array(numberOfRows).fill(false);
  const clearColumns = Array(numberOfColumns).fill(false);

  // Pass 1: figure out which cols / rows to clear and set those in our lists
  for (let i = 0; i < numberOfRows; i++) {
    for (let j = 0; j < numberOfColumns; j++) {
      if (grid[i][j] === "*") {
        clearRows[i] = true;
        clearColumns[j] = true;
      }
    }
  }

  // Pass 2: clear rows and columns
  for (let i = 0; i < numberOfRows; i++) {
    for (let j = 0; j < numberOfColumns; j++) {
      if (clearRows[i] || clearColumns[j]) {
        grid[i][j] = "*";
      }
    }
  }

  return grid;
}