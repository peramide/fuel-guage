# ⛽ Fuel Gauge

A Python program that simulates a car’s fuel gauge.
It prompts the user to enter a fuel fraction (X/Y), validates the input, and displays the tank’s fuel level as a percentage or indicator (`E` for empty, `F` for full).

Inspired by Harvard’s **CS50 “Fuel” problem**.

---

## 📘 Description

The program asks the user for a fraction (e.g., `3/4`) and outputs how full the fuel tank is:

* Displays the percentage rounded to the nearest integer.
* Displays `E` if the tank is essentially empty (≤1%).
* Displays `F` if the tank is essentially full (≥99%).

The program repeatedly prompts for input until a valid fraction is entered, handling errors gracefully:

* Non-integer values
* Zero denominators
* Negative numbers
* Fractions greater than 1

---

## 🧠 Features

* Handles `ValueError` and `ZeroDivisionError` exceptions
* Accepts only valid integer fractions (e.g., `1/4`, `3/5`)
* Automatically re-prompts on invalid input
* Rounds percentages correctly using Python’s `round()`

---

## ⚙️ Usage

Run the program in your terminal:

```bash
python fuel.py
```

Enter a fraction like:

```
Fraction: 3/4
```

**Output:**

```
75%
```

---

## 🧪 How to Test

Try the following manual tests:

| Input        | Expected Output | Description                 |
| ------------ | --------------- | --------------------------- |
| `3/4`        | `75%`           | 75% full                    |
| `1/4`        | `25%`           | 25% full                    |
| `4/4`        | `F`             | Full tank                   |
| `0/4`        | `E`             | Empty tank                  |
| `4/0`        | Prompt again    | Handles `ZeroDivisionError` |
| `three/four` | Prompt again    | Handles `ValueError`        |
| `1.5/3`      | Prompt again    | Handles invalid float input |
| `-3/4`       | Prompt again    | Handles negative input      |
| `5/4`        | Prompt again    | Handles `X > Y`             |

---

## 🧩 Example Run

```
Fraction: 3/4
75%
Fraction: 4/4
F
Fraction: 0/4
E
Fraction: 4/0
ZeroDivisionError — try again!
Fraction: 1/4
25%
```

---

## 🛠️ Technologies Used

* Python 3
* Exception Handling (`try`/`except`)
* Input Validation
* Basic Arithmetic and Rounding

