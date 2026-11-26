"""One-line office joke, for make.fun.

The brief: the funniest one-line office joke the agent can write, at most
200 characters. It has to really be an office joke, land instantly, and stay
tight. The printer was picked because it is the one office appliance every
reader has fought: two settings, both useless, and a perfect record of never
printing the thing that mattered.
"""

LINE = "Our printer has two settings: jammed, and out of toner. It has never once printed the thing I actually needed."

# The entry must be exactly one line of 1-200 characters, and the sealed
# scorer rejects whitespace-only text, so fail loudly instead of writing it.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, limit is 200"
assert "\n" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be only whitespace"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
