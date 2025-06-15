# Python Coding Conventions

## 1. General Principles

- Code should be readable, consistent, and maintainable.
- Follow [PEP 8](https://peps.python.org/pep-0008/) as the primary style guide.
- Write code for humans, not just for machines.

## 2. File Organization

- Each module should have a clear purpose.
- Use UTF-8 encoding.
- Place imports at the top of the file, grouped as:
  1. Standard library imports
  2. Third-party imports
  3. Local application imports
- Use absolute imports when possible.

## 3. Naming Conventions

- Variables, functions, methods: `lower_case_with_underscores`
- Classes, exceptions: `CapWords` (PascalCase)
- Constants: `ALL_CAPS_WITH_UNDERSCORES`
- Private members: prefix with a single underscore `_private`
- Avoid single-character variable names except for counters or iterators.

## 4. Indentation & Spacing

- Use 4 spaces per indentation level. Do not use tabs.
- Limit lines to 79 characters.
- Use blank lines to separate functions, classes, and logical sections.
- No extra spaces inside parentheses, brackets, or braces.
- Use a single space after commas, colons, and semicolons.

## 5. Imports

- One import per line.
- Avoid wildcard imports (`from module import *`).
- Imports should be on separate lines.

## 6. Docstrings & Comments

- Use docstrings for all public modules, functions, classes, and methods.
- Use triple double quotes for docstrings (`"""Docstring"""`).
- Write comments in English, clear and concise.
- Update comments when code changes.
- Use inline comments sparingly and only when necessary.

## 7. Functions & Methods

- Keep functions small and focused.
- Use descriptive names.
- Use type hints where appropriate.
- Default argument values should not be mutable objects.

## 8. Classes

- Use new-style classes (inherit from `object` in Python 2, always in Python 3).
- Use properties for getters/setters instead of explicit methods when possible.

## 9. Exceptions

- Use specific exceptions.
- Catch exceptions only when necessary.
- Do not use bare `except:` clauses.

## 10. String Handling

- Prefer f-strings (Python 3.6+) for formatting: `f"Hello, {name}!"`
- Use single quotes `'` or double quotes `"` consistently.

## 11. Type Annotations

- Use type hints for function arguments and return values.
- Use `Optional`, `List`, `Dict`, etc. from `typing` as needed.

## 12. Testing

- Write tests for new code.
- Use `unittest`, `pytest`, or similar frameworks.
- Name test files and functions clearly.

## 13. Miscellaneous

- Avoid global variables.
- Use list comprehensions and generator expressions where appropriate.
- Prefer `with` statements for resource management (files, locks, etc.).
- Remove unused code and imports.

---

**References:**
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)
