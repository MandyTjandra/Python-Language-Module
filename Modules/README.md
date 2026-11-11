# 📚 Course Modules & Syllabus Index

Welcome to the **Modules Directory**. Each folder here represents a self-contained chapter designed to teach core Python concepts progressively.

---

## 🧭 Suggested Learning Track

For self-paced students and structured classroom curricula, we recommend following the numbered sequence below:

```text
  Module 1: Foundations ──> Module 2: Conditionals ──> Module 3: Loops
                                                           │
  Module 6: OOP & Funcs <── Module 5: Strings In-Depth <── Module 4: Lists & NumPy
```

---

## 📋 Comprehensive Chapter Guide

### [Module 1: Introduction to Python](./Module%201%20(Intro))
* **Level**: Beginner | **Est. Time**: 1 - 2 Hours
* **Key Files**:
  * [`HelloWorld.py`](./Module%201%20(Intro)/HelloWorld.py) — Console output using `print()`.
  * [`Comments.py`](./Module%201%20(Intro)/Comments.py) — Documentation and variable assignment.
  * [`DataTypes.py`](./Module%201%20(Intro)/DataTypes.py) — Numbers, sequences, mappings, sets, and booleans.
  * [`Casting.py`](./Module%201%20(Intro)/Casting.py) — Explicit type conversion (`int`, `float`, `str`).
  * [`Input_and_Output.py`](./Module%201%20(Intro)/Input_and_Output.py) — Reading user input via `input()`.
  * [`Operator.py`](./Module%201%20(Intro)/Operator.py), [`LogicalOperator.py`](./Module%201%20(Intro)/LogicalOperator.py), [`IdentityOperator.py`](./Module%201%20(Intro)/IdentityOperator.py) — Arithmetic, boolean algebra, and membership tests.
* **Target Competency**: Set up Python, declare variables safely, perform arithmetic and boolean checks, and build interactive CLI prompts.

---

### [Module 2: Conditionals & Branching](./Module%202%20(Conditional))
* **Level**: Beginner | **Est. Time**: 1 Hour
* **Key Files**:
  * [`Conditionals.py`](./Module%202%20(Conditional)/Conditionals.py) — `if`, `elif`, and `else` decision branches.
  * [`SwitchCase.py`](./Module%202%20(Conditional)/SwitchCase.py) — Dictionary mapping as an idiomatic switch-case pattern (`dict.get()`).
* **Target Competency**: Write programs that respond dynamically to diverse inputs, enforce boundaries, and organize dispatch tables cleanly.

---

### [Module 3: Looping & Iteration](./Module%203%20(Looping))
* **Level**: Beginner | **Est. Time**: 1 - 1.5 Hours
* **Key Files**:
  * [`For.py`](./Module%203%20(Looping)/For.py) — Counted iteration using `for` and `range()`.
  * [`While.py`](./Module%203%20(Looping)/While.py) — Condition-driven loops, step incrementing, and terminating conditions.
* **Target Competency**: Automate repeated computations, iterate over index ranges, and prevent accidental infinite loops.

---

### [Module 4: Arrays & Lists](./Module%204%20(Array))
* **Level**: Intermediate | **Est. Time**: 1.5 - 2 Hours
* **Key Files**:
  * [`Array.py`](./Module%204%20(Array)/Array.py) — Python list indexing, element replacement, length calculation, and iteration.
  * [`Array_Syntax.py`](./Module%204%20(Array)/Array_Syntax.py) — List mutation methods (`.append()`, `.pop()`, `.remove()`, `.sort()`).
  * [`Numpy.py`](./Module%204%20(Array)/Numpy.py) — NumPy array creation, vector operations, and `np.sum()`.
* **Target Competency**: Organize linear collections of data, manipulate lists dynamically, and recognize when to leverage NumPy for high-performance mathematics.

---

### [Module 5: Strings in Depth](./Module%205%20(String))
* **Level**: Intermediate | **Est. Time**: 2 Hours
* **Key Subfolders**:
  * [`Python String/`](./Module%205%20(String)/Python%20String) — Quotes nesting, multi-line strings (`"""`), character access, and `in` checks.
  * [`Slicing String/`](./Module%205%20(String)/Slicing%20String) — Substring extraction with start, stop, and negative indexes.
  * [`Modify String/`](./Module%205%20(String)/Modify%20String) — `.strip()`, `.replace()`, `.split()`, and letter casing.
  * [`Format String/`](./Module%205%20(String)/Format%20String) — Modern `f"{var}"` formatting and float precision modifiers (`:.2f`).
  * [`Concanate String/`](./Module%205%20(String)/Concanate%20String) — Joining strings safely.
  * [`Escape Character/`](./Module%205%20(String)/Escape%20Character) — Special characters (`\n`, `\t`, `\"`) and in-place overwriting (`\r`).
* **Target Competency**: Parse, clean, slice, and dynamically construct textual data for reports, logs, and user interfaces.

---

### [Module 6: Functions & Object-Oriented Programming](./Module%206%20(Function))
* **Level**: Intermediate | **Est. Time**: 2 - 3 Hours
* **Key Subfolders**:
  * [`Function/`](./Module%206%20(Function)/Function) — Defining reusable functions (`def`), parameters vs arguments, and return values.
  * [`Pointer/`](./Module%206%20(Function)/Pointer) — Variable-length tuples (`*args`), memory references, and object inspection (`id()`, `sys.getsizeof()`).
  * [`Class/`](./Module%206%20(Function)/Class) — Classes, constructors (`__init__`), instance attributes, `self`, methods, and `__str__`.
* **Target Competency**: Modularize applications into clean functional components, understand object memory references, and build custom OOP models.

---

## 👩‍🏫 Lesson Plan Blueprint (For Teachers)

If you are using this repository to teach a 6-week or 6-session Python course:

| Session | Topic | Lecture & Live Demo | Lab Activity |
| :---: | :--- | :--- | :--- |
| **1** | Syntax & Fundamentals | Run `HelloWorld.py` & `Operator.py` | Create a simple CLI tip calculator using `input()` and casting. |
| **2** | Decisions & Logic | Demonstrate `if-elif-else` & `dict.get` | Build an interactive grading system (A, B, C, D, F) or license plate lookup. |
| **3** | Loops & Repetition | Compare `for i in range()` vs `while` | Write a multiplication table generator or a guessing game. |
| **4** | Lists & Numerical Arrays | List mutations + NumPy speed demo | Manage a student roster list (add, remove, sort, calculate averages). |
| **5** | Text & String Magic | Slicing + F-strings + `\r` progress bar | Build a user input sanitizer that parses emails or creates invoice lines. |
| **6** | Functions & OOP | Functions with `*args` + Classes with `__init__` | Model a `BankAccount` or `Student` class with custom methods. |

---

*(Select any module link above to start learning!)*
