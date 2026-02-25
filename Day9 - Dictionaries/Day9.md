# Silent Auction 

A command-line silent auction program written in Python. Bidders enter their name and bid one at a time, and the program announces the winner once all bids are in.

## Concepts Used to Build This

### Dictionaries
The core data structure of this project. `auction_dictionary` stores each bid with the **bid amount as the key** and the **bidder's name as the value**. This is a meaningful design choice — it makes it natural to compare bids numerically and look up who placed a given bid. This project likely represents a first real use case where a dictionary is clearly a better fit than a list.

### Iterating Over a Dictionary
`get_highest_bidder()` loops over the dictionary using `for key in auction_dictionary`, accessing each bid amount as the key and retrieving the corresponding name with `auction_dictionary[key]`. This pattern — iterating over keys to inspect and compare values — is one of the most common ways to work with dictionaries.

### Finding a Maximum by Hand
Rather than using Python's built-in `max()`, the highest bid is found manually by keeping a running `highest_bid` variable and updating it whenever a larger key is found. This is a classic algorithm pattern worth understanding from first principles before reaching for shortcuts.

### Functions
Two helper functions keep the logic clean and separated from the loop:

- `add_bid()` — handles writing to the dictionary
- `get_highest_bidder()` — handles reading from it and returning the result

Separating concerns this way makes each piece easier to reason about and reuse.

### Returning a List from a Function
`get_highest_bidder()` returns both the winner's name and their bid amount together as a two-element list `[name, bid]`. The caller then accesses them by index (`highest_bidder[0]`, `highest_bidder[1]`). This is a practical solution for returning multiple values from a single function.

### `while` Loop with a Boolean Flag
The bidding loop runs with `while not list_complete`, continuing until the boolean flag is flipped to `True` when the user signals no more bidders. The same exit-flag pattern seen in previous projects, applied here to a data collection loop.

### `match` / `case` with `.lower()`
The user's yes/no answer is handled with a `match` statement. Calling `.lower()` on the input first means the check works regardless of how the user capitalises their answer — a small but important defensive touch.

### `continue` in a Loop
When the user types `yes`, the `continue` keyword skips the rest of the current loop iteration and goes straight back to the top, prompting the next bidder immediately without any extra logic needed.

