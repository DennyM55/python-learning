### Reserved Words in Python (A.D. Format)

Here’s a clean and organized list of reserved words in Python in **A.D. format** for easy reference:

---

#### **A. Keywords for Control Flow**
- `if`, `elif`, `else` – Conditional statements.
- `for`, `while` – Looping constructs.
- `break` – Exits a loop immediately.
- `continue` – Skips to the next iteration of the loop.
- `pass` – Placeholder for "do nothing."

---

#### **B. Exception Handling**
- `try`, `except`, `finally` – Manage exceptions.
- `raise` – Raise an exception.

---

#### **C. Logical and Comparison**
- `and`, `or`, `not` – Logical operators.
- `is` – Tests object identity.
- `in` – Checks membership.

---

#### **D. Functions and Classes**
- `def` – Define a function.
- `class` – Define a class.
- `lambda` – Anonymous function.

---

#### **E. Variable Scopes**
- `global` – Declare global variables.
- `nonlocal` – Declare variables in enclosing scopes.

---

#### **F. Asynchronous Programming**
- `async`, `await` – For asynchronous code execution.

---

#### **G. Imports**
- `import`, `from`, `as` – For importing modules and aliasing.

---

#### **H. Special Literals**
- `True`, `False` – Boolean literals.
- `None` – Null value.

---

#### **I. Miscellaneous**
- `assert` – Debugging aid for validating conditions.
- `del` – Delete an object.
- `with` – Used with context managers.
- `yield` – Produce a value from a generator.

---

### Programmatic Check for Reserved Words:
```python
import keyword

# List all reserved words
print(keyword.kwlist)

# Check if a word is a reserved keyword
print(keyword.iskeyword("for"))    # Output: True
print(keyword.iskeyword("hello"))  # Output: False
```

Keep this cheat sheet handy! 🚀