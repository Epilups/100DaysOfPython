# Caesar Cipher 

A command-line implementation of the Caesar Cipher in Python, supporting both encoding and decoding of text with a customizable shift value.

## What is the Caesar Cipher?

The Caesar Cipher is one of the oldest encryption techniques. It works by shifting every letter in a message a fixed number of positions along the alphabet. For example, with a shift of 3, `a` becomes `d`, `b` becomes `e`, and so on. Decoding reverses the shift to recover the original message.

## Concepts Used to Build This

### Modular Arithmetic (`%`)
The core of the cipher. When shifting a letter's position, you can fall off the end of the alphabet — for example, shifting `z` by 1 should wrap around to `a`, not go out of bounds. The modulo operator `% 26` handles this automatically by wrapping any position back into the 0–25 range:

```python
shifted_position = (alphabet.index(letter) + shift) % 26
```

This is the mathematical heart of the Caesar Cipher and works identically for decoding by subtracting the shift instead.

### `list.index()`
Used to find the numeric position of a character in the alphabet list. This is what converts a letter into a number that can be shifted — `alphabet.index('a')` returns `0`, `alphabet.index('z')` returns `25`, and so on.

### Converting Between Letters and Positions
The encode/decode logic constantly moves between two representations — characters and their index positions — using `alphabet.index()` to go from letter to number, and `alphabet[i]` to go back from number to letter. Understanding this two-way mapping is fundamental to the cipher working at all.

### Functions with Parameters
Both `encode()` and `decode()` are defined to accept `text` and `shift` as parameters, making them reusable for any input rather than hardcoded to specific values. This separation of the logic from the input collection is a key step toward writing cleaner, more modular code.

### `while` Loop for Program Flow Control
The program uses a `while not exitCypher` loop to keep the cipher running across multiple uses. A boolean flag (`exitCypher`) is flipped to `True` when the user types `exit`, which ends the loop cleanly. This is the same boolean-as-exit-signal pattern used in game loops.

### Working with Lists and `stringify()`
Text is converted to a list of characters for processing, manipulated position by position, and then joined back into a string for output using the reused `stringify()` helper. This list-based approach makes it straightforward to work on individual characters by index.

### `int()` Type Conversion
The shift value is collected via `input()`, which always returns a string, and immediately converted with `int()` so it can be used in arithmetic. A small but necessary step whenever doing math with user input.

