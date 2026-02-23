# Hangman

A command-line Hangman game written in Python. A random word is selected and the player guesses one letter at a time, with ASCII art updating to show remaining lives.

## Concepts Used to Build This

### Functions
The game is broken into small, single-purpose helper functions rather than written as one long script. This reflects an understanding of how to decompose a problem — each function does one job and can be reasoned about independently.

- `select_random_word()` — picks a random word from the list and returns it as a character list
- `underscore_word()` — generates a blank `_` display list matching the word's length
- `letter_exists_in_word()` — checks if a guessed letter appears in the word
- `stringify()` — converts a character list back into a printable string
- `find_occurrences()` — finds every index position where a letter appears in the word

### Working with Lists vs Strings
A deliberate design decision was made to work with words as **lists of characters** throughout the game, only converting to strings when printing. This makes it easy to update individual positions in the display (`current_state_underscore[i] = letter`) — something that isn't possible with plain strings since strings are immutable in Python.

### List Comprehension
`find_occurrences()` uses a list comprehension combined with `range()` and `str.startswith()` to collect every index where a letter appears:

```python
positions = [i for i in range(len(string)) if string.startswith(substring, i)]
```

This is a more compact and Pythonic alternative to building the list with a `for` loop and `.append()`.

### The `while` Loop as a Game Loop
The core game runs inside a `while` loop controlled by two conditions — `lives > 0` and `not player_won`. The loop continues as long as both are true, and exits naturally the moment either flips. This is the fundamental pattern for turn-based game logic.

### State Persistence Across Loop Iterations
`current_state_underscore` is created **once before the loop** and mutated in place each turn. This is what allows correct guesses to "stick" — the revealed letters accumulate across iterations rather than resetting each time.

### Win/Loss Detection
- **Win** — after each correct guess, the current display list is compared directly to `word_to_guess`. When they match, `player_won` is set to `True`, ending the loop.
- **Loss** — `lives` is decremented on each wrong guess. When it hits 0, the loop condition fails and the game ends.

### `match` / `case` (Structural Pattern Matching)
Python 3.10+ `match` statement is used to select the correct ASCII art stage based on the current `lives` value. This is a cleaner alternative to a long `if / elif` chain when branching on a single variable with discrete values.

### Importing from Multiple Modules
The project is split across files — `assets.py` holds the word list and ASCII art stages, and the main script imports from it in two ways: `from assets import word_list` for direct access, and `import assets` for namespaced access to the art stages (`assets.full_health`, `assets.dead`, etc.).

### `str.count()` and `str.startswith()`
`letter_exists_in_word()` uses `.count()` to check how many times a letter appears, and `find_occurrences()` uses `.startswith()` at each index position as a way to locate substrings — a less commonly taught but flexible string method.

