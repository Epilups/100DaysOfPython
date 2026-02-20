# Rock, Paper, Scissors

A simple command-line Rock, Paper, Scissors game written in Python.

## Concepts Used to Build This

### Python Fundamentals
This project was built using core Python knowledge that a beginner would encounter early in their learning journey.

**Variables and Data Types** — String variables store the ASCII art and player choices, while list variables hold the possible moves and win/loss/draw conditions.

**Multi-line Strings** — The ASCII art for each hand gesture (rock, paper, scissors) is stored using Python's triple-quoted strings, which allow text to span multiple lines without escape characters.

**Lists** — Used in two key ways: as a collection of valid choices (`['r', 'p', 's']`) and as a way to represent game outcomes and conditions (e.g., `[['r', 's'], ['p', 'r'], ['s', 'p']]` for all user-winning scenarios).

**Conditionals (`if / elif / else`)** — The game logic relies entirely on conditional branching to assign symbols, map user input to choices, and determine the winner by checking which condition list the outcome falls into.

**The `in` Operator** — Used to check whether the current `outcome` list exists within the `userwins`, `computerwins`, or `draw` lists — a clean way to avoid writing out every condition individually.

**f-Strings** — The results are printed using formatted string literals, allowing variables (the player's choice, the computer's choice, and the ASCII art) to be embedded directly into the output string.

**User Input (`input()`)** — `input()` is used to capture the player's move from the console.

### The `random` Module
The `random.choice()` function is imported from Python's standard library to randomly select the computer's move from the list of valid choices, simulating an opponent.

### Console UI with ASCII Art
A basic understanding of how text renders in a terminal was applied to create a visual representation of each move using ASCII art, giving the game a more engaging feel beyond plain text output.

