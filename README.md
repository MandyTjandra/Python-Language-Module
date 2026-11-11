# 🧠 Python Language Learning Module

> A structured, hands-on Python curriculum designed for **self-paced learners** and **instructors / educators**. Learn fundamental programming concepts through bite-sized, runnable code examples, clear explanations, and guided exercises.

---

## 📖 About This Project

This repository serves as a modular study guide for mastering the **Python programming language**, from foundational syntax up to Object-Oriented Programming (OOP) and numerical computing.

- 🎓 **For Learners**: Code you can run, break, and modify immediately. Each chapter builds progressively on previous concepts.
- 👨‍🏫 **For Educators & Mentors**: A clean, modular syllabus suitable for classroom lectures, lab sessions, coding bootcamps, and assignments.
- 🌐 **Bilingual Friendly**: Written with accessible English summaries, with code comments and contextual notes in Indonesian (🇮🇩), making it ideal for Indonesian students and bilingual classrooms.

---

## 🗺️ Curriculum Roadmap & Syllabus

| Module | Level | Core Topics | Key Learning Objectives | Link |
| :--- | :---: | :--- | :--- | :---: |
| **01. Intro to Python** | `Beginner` | Variables, Data Types, Casting, I/O, Operators | Understand Python syntax, declare variables, convert data types, accept user input, and evaluate arithmetic/logical expressions. | [Explore Module 1](./Modules/Module%201%20(Intro)) |
| **02. Conditionals** | `Beginner` | `if`, `elif`, `else`, Dictionary-based Switch | Direct control flow with conditional branching and emulate switch-case logic efficiently. | [Explore Module 2](./Modules/Module%202%20(Conditional)) |
| **03. Looping** | `Beginner` | `for` loops, `range()`, `while` loops, infinite loop prevention | Automate repetitive tasks, iterate over numeric sequences, and manage loop counters safely. | [Explore Module 3](./Modules/Module%203%20(Looping)) |
| **04. Arrays & Lists** | `Intermediate` | Python Lists, Indexing, List Methods, NumPy | Store and manipulate ordered collections; perform fast vectorized math using the NumPy library. | [Explore Module 4](./Modules/Module%204%20(Array)) |
| **05. Strings in Depth** | `Intermediate` | String Slicing, Methods, F-Strings, Escape Codes | Format text dynamically, slice substrings, sanitize inputs, and format console outputs. | [Explore Module 5](./Modules/Module%205%20(String)) |
| **06. Functions & OOP** | `Intermediate` | `def`, Arguments, Memory/IDs, Classes, `__init__`, Methods | Encapsulate logic in reusable functions and design object-oriented programs using classes and instances. | [Explore Module 6](./Modules/Module%206%20(Function)) |

---

## 🚀 Getting Started

### 1. Prerequisites
Make sure you have **Python 3.8+** installed on your system.

```bash
# Verify Python installation
python --version
# or on macOS/Linux
python3 --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/MandyTjandra/Python-Language-Module.git
cd Python-Language-Module
```

### 3. (Optional) Set Up a Virtual Environment & Install NumPy
Module 4 includes scientific computing examples using `numpy`:

```bash
# Create a virtual environment
python -m venv venv

# Activate it:
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Windows (Command Prompt):
.\venv\Scripts\activate.bat
# macOS / Linux:
source venv/bin/activate

# Install NumPy
pip install numpy
```

---

## 💡 Recommended Learning & Teaching Methodology

To get the most out of these modules, we recommend the **4-Step Learning Cycle**:

```
 ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
 │  1. OBSERVE │ ──> │   2. RUN    │ ──> │ 3. EXPERIMENT│ ──> │  4. SOLVE   │
 │ Read concept│     │ Execute the │     │ Tweak values│     │ Complete the│
 │  & comments │     │   script    │     │ & test errors│    │  challenges │
 └─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

1. **Observe**: Read the module's `README.md` to grasp the core concept and syntax rules.
2. **Run**: Run the corresponding `.py` script in your terminal:
   ```bash
   python "Modules/Module 1 (Intro)/HelloWorld.py"
   ```
3. **Experiment**: Modify numbers, strings, or conditions in the file. Predict what will happen before you re-run it.
4. **Solve**: Complete the hands-on practice challenges listed at the bottom of each module's guide.

### 👨‍🏫 Tips for Instructors
- **Live Coding Starter**: Use each `.py` file as starter code for live classroom demonstrations.
- **Concept Verification**: Pause at the comments to quiz students on expected output before running the code.
- **Assignment Ready**: Direct students to the practice exercises at the end of each module for homework or lab sessions.

---

## 📂 Repository Directory Overview

```text
Python-Language-Module/
├── README.md                                  # Main course overview & getting started guide
└── Modules/
    ├── README.md                              # Curriculum index & chapter navigation
    ├── Module 1 (Intro)/                      # Fundamentals: Syntax, Types, I/O, Operators
    │   ├── Casting.py
    │   ├── Comments.py
    │   ├── DataTypes.py
    │   ├── HelloWorld.py
    │   ├── IdentityOperator.py
    │   ├── Input_and_Output.py
    │   ├── LogicalOperator.py
    │   ├── Operator.py
    │   └── README.md
    ├── Module 2 (Conditional)/                # Branching & Decision Making
    │   ├── Conditionals.py
    │   ├── SwitchCase.py
    │   └── README.md
    ├── Module 3 (Looping)/                    # Repetition & Sequences
    │   ├── For.py
    │   ├── While.py
    │   └── README.md
    ├── Module 4 (Array)/                      # Lists & Numerical Computing
    │   ├── Array.py
    │   ├── Array_Syntax.py
    │   ├── Numpy.py
    │   └── README.md
    ├── Module 5 (String)/                     # Text Manipulation & Formatting
    │   ├── Concanate String/
    │   ├── Escape Character/
    │   ├── Format String/
    │   ├── Modify String/
    │   ├── Python String/
    │   ├── Slicing String/
    │   ├── String Methods/
    │   └── README.md
    └── Module 6 (Function)/                   # Functions & Object-Oriented Programming
        ├── Class/
        ├── Function/
        ├── Pointer/
        └── README.md
```

---

## 🎯 Suggested Next Topics (Future Roadmap)

Looking to expand your Python mastery? Here are suggested next topics to build upon these modules:
- [ ] **Error & Exception Handling**: `try`, `except`, `finally`, and custom exceptions.
- [ ] **File Input/Output**: Reading and writing `.txt`, `.csv`, and `.json` files.
- [ ] **Python Modules & Packages**: `import`, `__name__ == '__main__'`, and organizing multi-file projects.
- [ ] **List & Dictionary Comprehensions**: Writing concise, idiomatic Python.
- [ ] **Virtual Environments & Dependency Management**: `pip`, `venv`, and `requirements.txt`.

---

## 🤝 Contributing

Contributions are welcome! If you would like to:
- Add new exercise challenges or solutions
- Translate comments or add documentation
- Fix typos or suggest new topic modules

Please feel free to open a Pull Request or create an Issue.

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE) (or free for personal educational use). Happy coding! 💻✨
