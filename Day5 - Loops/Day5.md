# Password Generator 🔐

A command-line password generator written in Python that creates randomized passwords from a custom mix of letters, symbols, and numbers.

## Concepts Used to Build This

### Python Fundamentals

**Variables and Data Types** — String and integer variables are used throughout: lists store the character pools, and `int()` is used to convert user input (which comes in as a string) into a usable number for controlling loop iterations.

**Lists** — The foundation of this project. Three predefined lists (`letters`, `numbers`, `symbols`) act as character pools to draw from. Three additional empty lists are built up during the loops to collect the user's requested characters, and then combined into one final list for shuffling.

**List Concatenation** — The three selected character lists are joined into a single list using the `+` operator (`selected_letters + selected_symbols + selected_numbers`), producing one flat collection ready to be shuffled.

**`for` Loops with `range()`** — A `for` loop combined with `range(1, count + 1)` is used to repeat a character-selection action exactly as many times as the user requested, once each for letters, symbols, and numbers.

**`int()` Type Conversion** — Since `input()` always returns a string, `int()` wraps each input call to convert the count values into integers so they can be used in `range()`.

**Printing with `end=''`** — The final password is printed character by character using a `for` loop. Passing `end=''` to `print()` suppresses the default newline, so all characters appear on a single line rather than stacked vertically.

### The `random` Module
Two functions from the `random` module are used:

- **`random.randint(a, b)`** — Generates a random integer between two values (inclusive), used here to pick a random index from each character pool list.
- **`random.sample(population, k)`** — Returns a new list of `k` unique elements drawn in random order from the population. Used to shuffle all selected characters into a final randomized password without repeating any element.

### Index-Based List Access
Characters are retrieved from the pools using a randomly generated index (`letters[random.randint(...)]`), demonstrating an understanding of how lists are zero-indexed and how to access elements by position.

### Building Up a List with `.append()`
Rather than constructing the password all at once, characters are added one at a time to growing lists using `.append()`, reinforcing the pattern of iteratively building a data structure.

## How to Run

```bash
python main.py
```

You will be prompted to enter how many letters, symbols, and numbers you want. The generator will then produce a shuffled password combining all three.

## Example Output

```
Welcome to the password generator
How many letters would you like in your password?
5
How many symbols would you like in your password?
3
How many numbers would you like in your password?
2

Your password is:
k@3R!mZ#Qe
```
