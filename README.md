# BMW Engines Search CLI Tool

A lightweight and efficient Command Line Interface (CLI) tool written in Python to search and retrieve detailed technical specifications of various BMW engines from a CSV database.

## 🚀 Features
* **Modular Architecture:** Clean code divided into dedicated functions for reading data, processing input, searching, and displaying results.
* **Smart Search:** Case-insensitive search with automatic whitespace trimming (e.g., searching `b48` or `  M20  ` works perfectly).
* **Robust Error Handling:** Smooth user experience that handles non-existent engines without crashing the application.
* **CSV Powered:** Dynamically loads data from an external `Data.csv` file using Python's native `csv.DictReader`.

## 🏎️ Supported Engines
The database currently supports detailed technical lookups for the following BMW engine families:
* **M20** (Classic Inline-6)
* **S14** (High-performance Inline-4)
* **S54 & S54HP** (Legendary Naturally Aspirated M-Power Inline-6)
* **B58** (Modern Turbocharged TwinPower Cargo Inline-6)
* **B48** (Efficient TwinPower Turbo Inline-4)

## 📂 Project Structure
* `main.py` - The core Python script containing the application logic.
* `Data.csv` - The database containing engine specs (Name, Code, Capacity, Cylinders, Horsepower, Torque, etc.).
* `README.md` - Documentation of the project.

## 🛠️ Requirements & Installation
1. Make sure you have **Python 3.x** installed.
2. Clone this repository or download the source files.
3. Place your `Data.csv` in the same directory as `main.py`.

## 💻 How to Run
Open your terminal/command prompt in the project folder and run:
```bash
python main.py


## 📊 Sample Output
```Text
What the Engine you search: b48
--The engine was successfully found--
Name engine: B48
Code engine: B48B20
Engine displacement: 1998 CC
...
```

## ⚖️ Disclaimer
This project is for educational and informational purposes only. The technical data provided within this database is gathered for general reference. The author is not responsible for any misuse, incorrect mechanical modifications, part installations, or diagnostic errors resulting from the use of this software. Always consult official BMW factory service manuals for actual garage operations or engine swaps.
