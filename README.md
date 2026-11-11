# 🧠 Python Language Learning Module

> A comprehensive, file-by-file Python curriculum designed for **self-paced learners** and **instructors / educators**. Every topic is paired with standalone, runnable `.py` scripts, clear code explanations, and practical exercises.

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Learning Level](https://img.shields.io/badge/Level-Beginner%20to%20Intermediate-green.svg)](#-file-by-file-curriculum--module-guide)
[![Language](https://img.shields.io/badge/Language-English%20%7C%20Indonesian%20%F0%9F%87%AE%F0%9F%87%A9-orange.svg)](#-about-this-project)

---

## 📖 About This Project

This repository is a modular study guide for mastering the **Python programming language**, taking you step-by-step from foundational syntax to Object-Oriented Programming (OOP) and numerical computing.

- 🎓 **For Learners**: Run and inspect individual files. Predict the output, read the comments, tweak the values, and test your understanding with practice challenges.
- 👨‍🏫 **For Educators & Mentors**: Structured specifically by concept. Each `.py` script serves as a self-contained live-coding demonstration or lab prompt.
- 🌐 **Bilingual Context (🇮🇩 / 🇬🇧)**: Explanations and documentation are in English, with real-world examples, comments, and variable names incorporating Indonesian context (such as vehicle plate lookups, university student records `Mahasiswa`, etc.).

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.8 or higher** installed:

```bash
python --version
# On macOS / Linux:
python3 --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/MandyTjandra/Python-Language-Module.git
cd Python-Language-Module
```

### 3. (Optional) Install NumPy for Module 4
Module 4 includes scientific computing examples using `numpy`:

```bash
# Optional: create a virtual environment
python -m venv venv

# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# macOS / Linux:
source venv/bin/activate

# Install NumPy
pip install numpy
```

---

## 📂 Complete Repository Directory

```text
Python-Language-Module/
├── LICENSE                                    # MIT License
├── README.md                                  # Main course guide & file catalog
└── Modules/
    ├── README.md                              # Detailed curriculum syllabus
    ├── Module 1 (Intro)/                      # 8 files: Syntax, types, casting, operators
    │   ├── Casting.py
    │   ├── Comments.py
    │   ├── DataTypes.py
    │   ├── HelloWorld.py
    │   ├── IdentityOperator.py
    │   ├── Input_and_Output.py
    │   ├── LogicalOperator.py
    │   ├── Operator.py
    │   └── README.md
    ├── Module 2 (Conditional)/                # 2 files: Branching & dictionary switch
    │   ├── Conditionals.py
    │   ├── SwitchCase.py
    │   └── README.md
    ├── Module 3 (Looping)/                    # 2 files: for & while loops
    │   ├── For.py
    │   ├── While.py
    │   └── README.md
    ├── Module 4 (Array)/                      # 3 files: Lists & NumPy arrays
    │   ├── Array.py
    │   ├── Array_Syntax.py
    │   ├── Numpy.py
    │   └── README.md
    ├── Module 5 (String)/                     # 13 files across 7 subdirectories
    │   ├── Concanate String/
    │   │   └── Concatenation.py
    │   ├── Escape Character/
    │   │   ├── CarriageReturn.py
    │   │   └── Escape.py
    │   ├── Format String/
    │   │   ├── F_String.py
    │   │   └── Placeholders_and_Modifiers.py
    │   ├── Modify String/
    │   │   ├── RemoveWhitespace.py
    │   │   ├── ReplaceString.py
    │   │   ├── SplitString.py
    │   │   └── Upper_and_Lower_Case.py
    │   ├── Python String/
    │   │   ├── AssignString.py
    │   │   ├── CheckString.py
    │   │   ├── LoopingString.py
    │   │   ├── Multilines.py
    │   │   ├── Not_in_String.py
    │   │   ├── Quotes_Inside_Quotes.py
    │   │   ├── StringInArray.py
    │   │   └── StringLength.py
    │   ├── Slicing String/
    │   │   └── Slicing.py
    │   ├── String Methods/
    │   │   └── StringMethods.py
    │   └── README.md
    └── Module 6 (Function)/                   # 12 files across 3 subdirectories
        ├── Class/
        │   ├── Class.py
        │   ├── Class2.py
        │   ├── Init.py
        │   ├── ObjectMethod.py
        │   ├── Pass.py
        │   ├── SelfParameter.py
        │   └── str.py
        ├── Function/
        │   ├── Argument.py
        │   ├── Function.py
        │   └── Math.py
        ├── Pointer/
        │   ├── PengenalanPointer.py
        │   └── Pointer.py
        └── README.md
```

---

## 🔍 File-by-File Curriculum & Module Guide

### 📘 [Module 1: Introduction to Python](./Modules/Module%201%20(Intro))
*Focus: Foundational syntax, data types, dynamic typing, user input, and operators.*

| File | Core Concepts & Specific Implementation | Run Command |
| :--- | :--- | :--- |
| **[`HelloWorld.py`](./Modules/Module%201%20(Intro)/HelloWorld.py)** | Basic `print("Hello World!")` execution; understanding terminal output. | `python "Modules/Module 1 (Intro)/HelloWorld.py"` |
| **[`Comments.py`](./Modules/Module%201%20(Intro)/Comments.py)** | Single-line `#` comments; variable assignments (`age = 45`, `salary = 1456.8`, `name = "John"`). | `python "Modules/Module 1 (Intro)/Comments.py"` |
| **[`DataTypes.py`](./Modules/Module%201%20(Intro)/DataTypes.py)** | Covers 10 native data types: `str`, `int`, `float`, `complex (3j)`, `list`, `tuple`, `dict`, `set`, `bool`, and `bytes (b"Geeks")`. | `python "Modules/Module 1 (Intro)/DataTypes.py"` |
| **[`Casting.py`](./Modules/Module%201%20(Intro)/Casting.py)** | Type casting with `int(3.2)` (truncates decimals), `str("Halo!")`, and `float(5.5)`. | `python "Modules/Module 1 (Intro)/Casting.py"` |
| **[`Input_and_Output.py`](./Modules/Module%201%20(Intro)/Input_and_Output.py)** | Prompting interactive CLI input via `val = input("Enter your value: ")`. | `python "Modules/Module 1 (Intro)/Input_and_Output.py"` |
| **[`Operator.py`](./Modules/Module%201%20(Intro)/Operator.py)** | Arithmetic operations on `a = 9`, `b = 4`: addition (`+`), subtraction (`-`), multiplication (`*`), modulus (`%`), power (`**`), and floor division (`//`). | `python "Modules/Module 1 (Intro)/Operator.py"` |
| **[`LogicalOperator.py`](./Modules/Module%201%20(Intro)/LogicalOperator.py)** | Boolean logic evaluating `a and b` and `a or b` on booleans `True` and `False`. | `python "Modules/Module 1 (Intro)/LogicalOperator.py"` |
| **[`IdentityOperator.py`](./Modules/Module%201%20(Intro)/IdentityOperator.py)** | Membership testing: evaluating `"banana" in ["apple", "banana"]`. | `python "Modules/Module 1 (Intro)/IdentityOperator.py"` |

---

### 📙 [Module 2: Conditionals & Decision Making](./Modules/Module%202%20(Conditional))
*Focus: Branching logic, whitespace indentation, and hash-map lookup tables.*

| File | Core Concepts & Specific Implementation | Run Command |
| :--- | :--- | :--- |
| **[`Conditionals.py`](./Modules/Module%202%20(Conditional)/Conditionals.py)** | Binary input check (`"1"` ➔ True, `"0"` ➔ False, else ➔ Unknown) using `if`, `elif`, and `else`. | `python "Modules/Module 2 (Conditional)/Conditionals.py"` |
| **[`SwitchCase.py`](./Modules/Module%202%20(Conditional)/SwitchCase.py)** | Emulating switch-case using an Indonesian vehicle license plate dictionary (`'B'`: Bekasi, `'A'`: Banten, `'D'`: Bandung, `'E'`: Cirebon) with `.upper()` and safe fallback `.get()`. | `python "Modules/Module 2 (Conditional)/SwitchCase.py"` |

---

### 📗 [Module 3: Looping & Iteration](./Modules/Module%203%20(Looping))
*Focus: Counted loops, conditional iteration, counter increments, and string concatenation.*

| File | Core Concepts & Specific Implementation | Run Command |
| :--- | :--- | :--- |
| **[`For.py`](./Modules/Module%203%20(Looping)/For.py)** | Counted iteration: `for x in range(0, 4):` displaying iterations 0 through 3. | `python "Modules/Module 3 (Looping)/For.py"` |
| **[`While.py`](./Modules/Module%203%20(Looping)/While.py)** | Condition loop: `while x < 4:` with explicit increment `x += 1`. Compares space-separated `print(..., x)` against string-concatenated `print(... + str(x))`. | `python "Modules/Module 3 (Looping)/While.py"` |

---

### 📕 [Module 4: Arrays & Lists](./Modules/Module%204%20(Array))
*Focus: Python lists as dynamic arrays, list mutations, and NumPy numerical computing.*

| File | Core Concepts & Specific Implementation | Run Command |
| :--- | :--- | :--- |
| **[`Array.py`](./Modules/Module%204%20(Array)/Array.py)** | `Num = [1, 2, 3]`: Zero-based indexing, element modification (`Num[0] = 10`), list length via `len()`, iterating by value, and single-line comma formatting using `range(len(Num))`. | `python "Modules/Module 4 (Array)/Array.py"` |
| **[`Array_Syntax.py`](./Modules/Module%204%20(Array)/Array_Syntax.py)** | Mutating `angka = [1, 2, 3, 4, 5]`: `.append(6)`, `.pop(2)` (remove by index), and `.remove(1)` (remove by value). Contains reference notes for 11 list methods. | `python "Modules/Module 4 (Array)/Array_Syntax.py"` |
| **[`Numpy.py`](./Modules/Module%204%20(Array)/Numpy.py)** | Scientific arrays with `np.array([10, 20, 30])`, element mutation, arithmetic on elements, and calculating total sum via `np.sum()`. | `python "Modules/Module 4 (Array)/Numpy.py"` |

---

### 🟪 [Module 5: Strings in Depth](./Modules/Module%205%20(String))
*Focus: Text manipulation, substring slicing, character sanitization, f-strings, and terminal animations.*

#### 📁 Python String Basics
| File | Implementation Details |
| :--- | :--- |
| **[`AssignString.py`](./Modules/Module%205%20(String)/Python%20String/AssignString.py)** | Assigning string literals with single quotes (`a = 'Hello'`). |
| **[`Quotes_Inside_Quotes.py`](./Modules/Module%205%20(String)/Python%20String/Quotes_Inside_Quotes.py)** | Alternating single and double quotes to nest quotes without escape characters. |
| **[`Multilines.py`](./Modules/Module%205%20(String)/Python%20String/Multilines.py)** | Multi-line string paragraphs using triple quotes (`"""`). |
| **[`StringInArray.py`](./Modules/Module%205%20(String)/Python%20String/StringInArray.py)** | Treating strings as character arrays: indexing character `'e'` from `"Hello, World!"` with `a[1]`. |
| **[`StringLength.py`](./Modules/Module%205%20(String)/Python%20String/StringLength.py)** | Measuring string length using `len(a)`. |
| **[`LoopingString.py`](./Modules/Module%205%20(String)/Python%20String/LoopingString.py)** | Iterating over each letter of `"banana"` with `for x in ...`. |
| **[`CheckString.py`](./Modules/Module%205%20(String)/Python%20String/CheckString.py)** | Substring presence check using `"free" in txt` within an `if` statement. |
| **[`Not_in_String.py`](./Modules/Module%205%20(String)/Python%20String/Not_in_String.py)** | Substring absence check using `"expensive" not in txt`. |

#### 📁 Slicing, Modification, Formatting & Escapes
| File | Implementation Details |
| :--- | :--- |
| **[`Slicing.py`](./Modules/Module%205%20(String)/Slicing%20String/Slicing.py)** | Slicing range `[2:5]`, start slice `[:5]`, end slice `[2:]`, and negative slice `[-5:-2]`. |
| **[`Concatenation.py`](./Modules/Module%205%20(String)/Concanate%20String/Concatenation.py)** | Combining strings using the `+` operator (`'Hello ' + "World!"`). |
| **[`RemoveWhitespace.py`](./Modules/Module%205%20(String)/Modify%20String/RemoveWhitespace.py)** | Stripping leading and trailing spaces with `.strip()`. |
| **[`ReplaceString.py`](./Modules/Module%205%20(String)/Modify%20String/ReplaceString.py)** | Replacing characters with `.replace("H", "J")` (`"Jello, World!"`). |
| **[`SplitString.py`](./Modules/Module%205%20(String)/Modify%20String/SplitString.py)** | Splitting comma-separated text into a list with `.split(",")`. |
| **[`Upper_and_Lower_Case.py`](./Modules/Module%205%20(String)/Modify%20String/Upper_and_Lower_Case.py)** | Casing conversion via `.lower()` and `.upper()`. |
| **[`StringMethods.py`](./Modules/Module%205%20(String)/String%20Methods/StringMethods.py)** | Comprehensive dictionary of 43 built-in string methods with demos of `.capitalize()`, `.lower()`, and `.swapcase()`. |
| **[`F_String.py`](./Modules/Module%205%20(String)/Format%20String/F_String.py)** | Variable embedding with `f"My name is John, I am {age}"`. |
| **[`Placeholders_and_Modifiers.py`](./Modules/Module%205%20(String)/Format%20String/Placeholders_and_Modifiers.py)** | Fixed-point decimals with `{price:.2f}` and inline math expressions `{20 * 59}`. |
| **[`Escape.py`](./Modules/Module%205%20(String)/Escape%20Character/Escape.py)** | Escape characters: `\"`, `\\`, octal codes (`\110\145\154\154\157`), and newline/tabs (`\n`, `\t`). |
| **[`CarriageReturn.py`](./Modules/Module%205%20(String)/Escape%20Character/CarriageReturn.py)** | Dynamic CLI overwrite using carriage return `\r` and `time.sleep(1)` to create an in-place counter (0–9). |

---

### 🟨 [Module 6: Functions & Object-Oriented Programming (OOP)](./Modules/Module%206%20(Function))
*Focus: Functions, parameter passing, arbitrary arguments, memory references, and class definitions.*

#### 📁 Functions & Memory Reference
| File | Implementation Details |
| :--- | :--- |
| **[`Function.py`](./Modules/Module%206%20(Function)/Function/Function.py)** | Declaring and invoking a zero-parameter function using `def printf():`. |
| **[`Argument.py`](./Modules/Module%206%20(Function)/Function/Argument.py)** | Positional arguments: single-argument (`fname`) and multi-argument (`fname, lname`) function calls. |
| **[`Math.py`](./Modules/Module%206%20(Function)/Function/Math.py)** | Function `math(a, b)` parsing two space-separated integers from terminal input via `map(int, input().split())`. |
| **[`Pointer.py`](./Modules/Module%206%20(Function)/Pointer/Pointer.py)** | Arbitrary positional arguments (`*kids` tuple), accessing by index, and iterating through returned names. |
| **[`PengenalanPointer.py`](./Modules/Module%206%20(Function)/Pointer/PengenalanPointer.py)** | Investigating Python's memory model: inspecting object memory addresses with `id(a)`, examining memory size in bytes with `sys.getsizeof()`, and explaining why Python uses references rather than raw pointers. |

#### 📁 Classes & OOP
| File | Implementation Details |
| :--- | :--- |
| **[`Class.py`](./Modules/Module%206%20(Function)/Class/Class.py)** | Basic class declaration `class MyClass: x = 5` and instantiating an object `p1 = MyClass()`. |
| **[`Pass.py`](./Modules/Module%206%20(Function)/Class/Pass.py)** | Using the `pass` statement as a syntactical placeholder in empty classes and functions. |
| **[`Init.py`](./Modules/Module%206%20(Function)/Class/Init.py)** | The `__init__(self, name, age)` constructor method, creating instances `Person("John", 36)` and `Person("Mandy", 19)`. |
| **[`Class2.py`](./Modules/Module%206%20(Function)/Class/Class2.py)** | Real-world Indonesian university student record model (`Mahasiswa`): initialising attributes `nama`, `nrp`, `umur`, `ipk`, `semester`, and `status`. Demonstrates formatted output with tab alignment, `{ipk:.2f}`, and inline conditional expression for status (`'Aktif'` vs `'Tidak Aktif'`). |
| **[`ObjectMethod.py`](./Modules/Module%206%20(Function)/Class/ObjectMethod.py)** | Defining methods inside a class (`myfunc(self)`) that access instance properties. |
| **[`SelfParameter.py`](./Modules/Module%206%20(Function)/Class/SelfParameter.py)** | Demonstrates that the `self` parameter can be renamed (e.g. `mysillyobject`, `abc`), creating instances `p1` to `p5`, and deleting attributes (`del p2.age`) or instances (`del p3`). |
| **[`str.py`](./Modules/Module%206%20(Function)/Class/str.py)** | Implementing the `__str__()` dunder method to customize how instances display when printed (`return f"{self.name}({self.age})"`). |

---

## 👨‍🏫 Pedagogical Guide: Teaching & Learning Workflow

For maximum learning impact, follow the **4-Step Learning Cycle**:

```
 ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
 │  1. OBSERVE  │ ──> │    2. RUN    │ ──> │3. EXPERIMENT │ ──> │   4. SOLVE   │
 │ Read concept │     │ Execute file │     │ Tweak values │     │ Complete the │
 │  & comments  │     │ in terminal  │     │ & test edge  │     │  challenges  │
 └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

1. **Observe**: Read the module `README.md` to understand the theory and syntax rules.
2. **Run**: Execute the specific file directly in your terminal to see the actual output.
3. **Experiment**: Change inputs, mutate values, or introduce deliberate syntax changes to see how Python responds.
4. **Solve**: Complete the graded practice challenges (🟢 Easy, 🟡 Medium, 🔴 Challenge) located at the bottom of each module guide.

---

## 🤝 Contributing

Contributions are warmly welcomed! You can:
- Add new exercise challenges to any module guide.
- Contribute new example scripts (e.g. error handling, file I/O).
- Improve code comments or documentation clarity.

Feel free to open a Pull Request or create an Issue.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE) © 2026 Mandy Tjandra. Free for educational and personal use. Happy coding! 💻✨
