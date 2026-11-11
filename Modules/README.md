# 📚 Course Modules & File Syllabus Index

Welcome to the **Modules Directory**. This directory houses the 6 core learning chapters of the course, spanning **32 standalone Python scripts**. Each file is designed to be executed directly, studied, and modified.

---

## 🧭 Course Progression Path

```text
  ┌───────────────────────┐       ┌────────────────────────┐       ┌──────────────────────┐
  │ Module 1: Intro       │ ────> │ Module 2: Conditionals │ ────> │ Module 3: Looping    │
  │ Syntax, Types & Ops   │       │ If-Else & Plat Lookup  │       │ For, While & Ranges  │
  └───────────────────────┘       └────────────────────────┘       └──────────────────────┘
                                                                               │
  ┌───────────────────────┐       ┌────────────────────────┐                   ▼
  │ Module 6: Funcs & OOP │ <──── │ Module 5: Strings      │ <──── ┌──────────────────────┐
  │ Methods & Mahasiswa   │       │ Slicing & Animations   │       │ Module 4: Arrays     │
  └───────────────────────┘       └────────────────────────┘       │ Lists & NumPy Matrix │
                                                                   └──────────────────────┘
```

---

## 📂 Detailed Module & File Catalog

### 1. [Module 1: Introduction to Python](./Module%201%20(Intro))
*Focus: Foundations, data types, casting, input, and operators.*
* 📄 [`HelloWorld.py`](./Module%201%20(Intro)/HelloWorld.py) — First output with `print("Hello World!")`.
* 📄 [`Comments.py`](./Module%201%20(Intro)/Comments.py) — Explanatory comments (`#`) and basic variables (`age`, `salary`, `name`).
* 📄 [`DataTypes.py`](./Module%201%20(Intro)/DataTypes.py) — Exploring 10 Python types (`str`, `int`, `float`, `complex`, `list`, `tuple`, `dict`, `set`, `bool`, `bytes`).
* 📄 [`Casting.py`](./Module%201%20(Intro)/Casting.py) — Type conversions using `int(3.2)`, `str("Halo!")`, and `float(5.5)`.
* 📄 [`Input_and_Output.py`](./Module%201%20(Intro)/Input_and_Output.py) — Capturing keyboard input using `input("Enter your value: ")`.
* 📄 [`Operator.py`](./Module%201%20(Intro)/Operator.py) — Arithmetic operators: addition, subtraction, multiplication, modulo (`%`), power (`**`), and floor division (`//`).
* 📄 [`LogicalOperator.py`](./Module%201%20(Intro)/LogicalOperator.py) — Logical evaluation with `and` and `or`.
* 📄 [`IdentityOperator.py`](./Module%201%20(Intro)/IdentityOperator.py) — Membership verification (`"banana" in x`).

---

### 2. [Module 2: Conditionals & Decision Making](./Module%202%20(Conditional))
*Focus: Branching logic and hash table lookup.*
* 📄 [`Conditionals.py`](./Module%202%20(Conditional)/Conditionals.py) — Evaluating user binary input (`"1"`, `"0"`, or other) using `if`, `elif`, and `else`.
* 📄 [`SwitchCase.py`](./Module%202%20(Conditional)/SwitchCase.py) — Emulating switch-case logic via a vehicle license plate dictionary (`B`, `A`, `D`, `E`) with `.upper()` and safe fallback `.get()`.

---

### 3. [Module 3: Looping & Repetition](./Module%203%20(Looping))
*Focus: Definite iteration and condition-based loops.*
* 📄 [`For.py`](./Module%203%20(Looping)/For.py) — Counted iteration using `for x in range(0, 4):`.
* 📄 [`While.py`](./Module%203%20(Looping)/While.py) — Condition loop `while x < 4:` with step increment `x += 1`, comparing comma vs string concatenation printing.

---

### 4. [Module 4: Arrays & Numerical Computing](./Module%204%20(Array))
*Focus: Dynamic list manipulation and NumPy vector mathematics.*
* 📄 [`Array.py`](./Module%204%20(Array)/Array.py) — Lists as arrays: indexing (`Num[0]`), modification (`Num[0] = 10`), length (`len()`), and single-line formatted iteration.
* 📄 [`Array_Syntax.py`](./Module%204%20(Array)/Array_Syntax.py) — List methods: `.append(6)`, `.pop(2)` (by index), and `.remove(1)` (by value), plus reference notes for 11 list methods.
* 📄 [`Numpy.py`](./Module%204%20(Array)/Numpy.py) — High-performance computing: `np.array()`, element manipulation, and total array summation via `np.sum()`.

---

### 5. [Module 5: Strings in Depth](./Module%205%20(String))
*Focus: Text analysis, substring slicing, character sanitization, f-strings, and terminal animations.*

* **Python String Basics:**
  * 📄 [`AssignString.py`](./Module%205%20(String)/Python%20String/AssignString.py) — Declaring string literals with single quotes.
  * 📄 [`Quotes_Inside_Quotes.py`](./Module%205%20(String)/Python%20String/Quotes_Inside_Quotes.py) — Nesting double quotes inside single quotes and vice-versa.
  * 📄 [`Multilines.py`](./Module%205%20(String)/Python%20String/Multilines.py) — Defining multi-line text blocks with `"""`.
  * 📄 [`StringInArray.py`](./Module%205%20(String)/Python%20String/StringInArray.py) — Accessing individual character elements by index (`a[1]`).
  * 📄 [`StringLength.py`](./Module%205%20(String)/Python%20String/StringLength.py) — Measuring character count with `len()`.
  * 📄 [`LoopingString.py`](./Module%205%20(String)/Python%20String/LoopingString.py) — Iterating across string characters with `for x in ...`.
  * 📄 [`CheckString.py`](./Module%205%20(String)/Python%20String/CheckString.py) — Testing substring existence with `"free" in txt`.
  * 📄 [`Not_in_String.py`](./Module%205%20(String)/Python%20String/Not_in_String.py) — Testing substring absence with `"expensive" not in txt`.

* **Slicing, Modification & Formatting:**
  * 📄 [`Slicing.py`](./Module%205%20(String)/Slicing%20String/Slicing.py) — Range slicing `[2:5]`, prefix `[:5]`, suffix `[2:]`, and negative offsets `[-5:-2]`.
  * 📄 [`Concatenation.py`](./Module%205%20(String)/Concanate%20String/Concatenation.py) — Joining strings using the `+` operator.
  * 📄 [`RemoveWhitespace.py`](./Module%205%20(String)/Modify%20String/RemoveWhitespace.py) — Trimming outer spaces with `.strip()`.
  * 📄 [`ReplaceString.py`](./Module%205%20(String)/Modify%20String/ReplaceString.py) — Replacing character occurrences with `.replace("H", "J")`.
  * 📄 [`SplitString.py`](./Module%205%20(String)/Modify%20String/SplitString.py) — Splitting comma-delimited strings into a list with `.split(",")`.
  * 📄 [`Upper_and_Lower_Case.py`](./Module%205%20(String)/Modify%20String/Upper_and_Lower_Case.py) — Transforming casing via `.lower()` and `.upper()`.
  * 📄 [`StringMethods.py`](./Module%205%20(String)/String%20Methods/StringMethods.py) — Comprehensive catalog of 43 string methods with executable examples of `.capitalize()`, `.lower()`, and `.swapcase()`.
  * 📄 [`F_String.py`](./Module%205%20(String)/Format%20String/F_String.py) — Variable interpolation with `f"My name is John, I am {age}"`.
  * 📄 [`Placeholders_and_Modifiers.py`](./Module%205%20(String)/Format%20String/Placeholders_and_Modifiers.py) — Decimal precision specifiers `{price:.2f}` and embedded arithmetic `{20 * 59}`.

* **Escape Sequences & Terminal Overwrites:**
  * 📄 [`Escape.py`](./Module%205%20(String)/Escape%20Character/Escape.py) — Escape codes (`\"`, `\\`, `\n`, `\t`, and octal `\110\145\154\154\157`).
  * 📄 [`CarriageReturn.py`](./Module%205%20(String)/Escape%20Character/CarriageReturn.py) — Overwriting console lines dynamically using `\r` and `time.sleep()`.

---

### 6. [Module 6: Functions & Object-Oriented Programming (OOP)](./Module%206%20(Function))
*Focus: Functions, parameter passing, memory models, and class definitions.*

* **Functions & Memory:**
  * 📄 [`Function.py`](./Module%206%20(Function)/Function/Function.py) — Basic function declaration with `def printf():`.
  * 📄 [`Argument.py`](./Module%206%20(Function)/Function/Argument.py) — Single and multi-parameter functions (`fname`, `fname, lname`).
  * 📄 [`Math.py`](./Module%206%20(Function)/Function/Math.py) — Function taking two space-separated integers using `map(int, input().split())`.
  * 📄 [`Pointer.py`](./Module%206%20(Function)/Pointer/Pointer.py) — Arbitrary arguments tuple (`*kids`) and indexing elements.
  * 📄 [`PengenalanPointer.py`](./Module%206%20(Function)/Pointer/PengenalanPointer.py) — Memory identity inspection via `id(a)` and byte allocation via `sys.getsizeof()`.

* **Object-Oriented Programming (Classes & Objects):**
  * 📄 [`Class.py`](./Module%206%20(Function)/Class/Class.py) — Class blueprint declaration and instance property access (`p1.x`).
  * 📄 [`Pass.py`](./Module%206%20(Function)/Class/Pass.py) — Using `pass` as a syntactical placeholder for unfinished classes and functions.
  * 📄 [`Init.py`](./Module%206%20(Function)/Class/Init.py) — The `__init__()` constructor method for initializing instance properties.
  * 📄 [`Class2.py`](./Module%206%20(Function)/Class/Class2.py) — Indonesian student data model (`Mahasiswa`): initialising `nama`, `nrp`, `umur`, `ipk`, `semester`, and `status` with formatted tab output and ternary status logic.
  * 📄 [`ObjectMethod.py`](./Module%206%20(Function)/Class/ObjectMethod.py) — Binding and calling methods on object instances (`myfunc(self)`).
  * 📄 [`SelfParameter.py`](./Module%206%20(Function)/Class/SelfParameter.py) — Demonstrating custom naming for `self` (`mysillyobject`, `abc`), and deleting properties or instances using `del`.
  * 📄 [`str.py`](./Module%206%20(Function)/Class/str.py) — Implementing the `__str__()` method to return clean string representations when instances are printed.

---

## 👩‍🏫 Lesson Plan Blueprint (For Teachers)

| Session | Module Focus | Specific Files to Demonstrate | In-Class Coding Exercise |
| :---: | :--- | :--- | :--- |
| **1** | Syntax & Calculations | `HelloWorld.py`, `DataTypes.py`, `Operator.py` | Create a tip and bill calculator using `input()` and casting. |
| **2** | Decision Branching | `Conditionals.py`, `SwitchCase.py` | Create a grade scale converter (A-F) or plate number validator. |
| **3** | Iteration & Repetition | `For.py`, `While.py` | Build a countdown blastoff script or multiplication table. |
| **4** | Dynamic Collections | `Array.py`, `Array_Syntax.py`, `Numpy.py` | Build a student score statistics tracker (min, max, average). |
| **5** | Text & Parsing | `Slicing.py`, `F_String.py`, `CarriageReturn.py` | Build an email domain parser and a command-line loading bar. |
| **6** | Functions & OOP | `Math.py`, `Pointer.py`, `Class2.py`, `str.py` | Model a `BankAccount` class with deposit, withdraw, and `__str__`. |
