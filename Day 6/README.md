# Day 6 – Data Preprocessing, Regex & Seaborn

## Regex Cheat Sheet

| Pattern | Meaning | Example |
|---|---|---|
| `\d` | Digit | 123 |
| `\w` | Word character | Python |
| `\s` | Whitespace | Space |
| `.` | Any character | a, 1, @ |
| `+` | One or more | aaa |
| `*` | Zero or more | aaa |
| `?` | Optional | color/colour |
| `^` | Beginning of string | ^Hello |
| `$` | End of string | world$ |
| `[]` | Character set | [A-Z] |
| `()` | Capturing group | (abc) |
| `|` | OR | cat|dog |
| `\.` | Literal dot | . |
| `\b` | Word boundary | Python |


## Regex Functions Used

- `re.findall()` – Finds all matching patterns
- `re.search()` – Searches for a pattern
- `re.match()` – Checks the beginning of a string
- `re.sub()` – Replaces matching patterns
- `re.split()` – Splits text using a pattern
