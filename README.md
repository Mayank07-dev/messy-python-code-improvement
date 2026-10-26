# Messy Python Code Improvement

A messy Python script improved with AI assistance (Cursor AI) to make it readable, safe and maintainable.

## Files
| File | Purpose |
|------|---------|
| `messy_code.py` | The original messy script (kept for comparison) |
| `improved_code.py` | The cleaned and improved version |

## Problems in the original
- One-letter names (`f`, `g`, `t`, `m`, `x`) that hide meaning
- Manual index loops instead of `sum()` and list comprehensions
- Deeply nested `if/else` for grading
- No input validation (crashes on text or empty input)
- No docstrings, no functions for input, everything at top level
- The "best subject" check was wrong: it only compared with subject 1

## Improvements made
- Meaningful names: `calculate_average`, `get_grade`, `marks`
- Grade boundaries stored in a table (`GRADE_BOUNDARIES`) instead of nested `if/else`
- `read_int()` validates input and re-asks until it is correct
- Marks restricted to 0-100, subject count at least 1
- Docstrings, `main()` function and `if __name__ == "__main__"` guard
- Correct highest and lowest subject reporting
- Formatted output with f-strings

## How to run
```bash
python improved_code.py
```

## Example output
```
Report for Mayank
Average: 79.67
Grade: C
Highest: 95 (subject 2)
Lowest: 64 (subject 3)
```

## Tools
Python 3, Cursor AI
