"""
Week 1 — Day 1: Python Basics
Run:  python tutorials/week-1/day-1/basics.py

What you’ll practice
- Variables & primitive types
- f-strings
- Arithmetic (/, //, %, **)
- String methods & slicing
- (Stretch) simple input and even/odd logic

How to use
1) Read each EXERCISE block.
2) Replace TODOs with your code.
3) Run the file and check the prints / self-checks.
"""

# =============== EXERCISE 1 — Variables & Types =====================
# TODO: set your own values
your_name: str = "Edward"      # e.g., "Edward"
your_age: int = 25             # e.g., 25
your_score: float = 3.7        # e.g., 3.7

print("EX1:", your_name, your_age, your_score)
print("EX1 types:", type(your_name).__name__, type(your_age).__name__, type(your_score).__name__)

# Quick self-checks (don’t change these)
assert isinstance(your_name, str), "your_name should be a string"
assert isinstance(your_age, int), "your_age should be an int"
assert isinstance(your_score, float), "your_score should be a float"


# =============== EXERCISE 2 — f-strings =============================
# TODO: implement a function that returns a sentence about a person using f-strings
def describe_person(name: str, age: int, score: float) -> str:
    """
    Return: "<name> is <age> years old and has a score of <score>."
    Use an f-string. Keep score to one decimal place.
    """
    # TODO: replace the line below
    return f"{name} is {age} years old and has a score of {score:.1f}."


print("EX2:", describe_person(your_name, your_age, your_score))


# =============== EXERCISE 3 — Arithmetic ============================
# TODO: implement a function that returns several arithmetic results for x and y
def arithmetic(x: int, y: int) -> dict:
    """
    Return a dict with keys:
      'sum', 'product', 'division', 'int_division', 'modulo', 'power'
    - division: true division (float)
    - int_division: floor division (//)
    - modulo: remainder
    - power: x**y
    """
    # TODO: implement (one line each is fine)
    return {
        "sum": x + y,
        "product": x * y,
        "division": x / y,
        "int_division": x // y,
        "modulo": x % y,
        "power": x ** y,
    }


x, y = 7, 3
ops = arithmetic(x, y)
print("EX3:", ops)
# Self-checks
assert ops["sum"] == 10
assert ops["product"] == 21
assert abs(ops["division"] - 7 / 3) < 1e-9
assert ops["int_division"] == 2
assert ops["modulo"] == 1
assert ops["power"] == 343


# =============== EXERCISE 4 — String Operations =====================
# TODO: implement basic string ops
def string_ops(text: str) -> dict:
    """
    Return a dict with:
      'lower'  -> text in lowercase
      'upper'  -> text in UPPERCASE
      'first5' -> first five characters (use slicing)
    """
    return {
        "lower": text.lower(),
        "upper": text.upper(),
        "first5": text[:5],
    }


sample = "Agent-Based Modelling"
sops = string_ops(sample)
print("EX4:", sops)
assert sops["lower"].startswith("agent")
assert sops["upper"].startswith("AGENT")
assert sops["first5"] == "Agent"


# =============== EXERCISE 5 (Stretch) — Even/Odd via Input ==========
# Toggle this to True if you want to try interactive input.
RUN_INTERACTIVE = False

def is_even(n: int) -> bool:
    """Return True if n is even, else False."""
    return n % 2 == 0


if RUN_INTERACTIVE:
    raw = input("Enter an integer: ")
    try:
        n = int(raw)
        print("even" if is_even(n) else "odd")
    except ValueError:
        print("That wasn't an integer!")

print("All Day 1 checks ran. ✅")