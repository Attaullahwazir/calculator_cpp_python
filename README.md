# 🔢 C++ Powered Calculator with Python Interface

This project demonstrates how to integrate **C++** and **Python** using `ctypes`, building a simple yet effective calculator. The Python script handles user interaction, while the C++ code performs the core arithmetic operations for better performance and language interoperability.

---

## 📁 Project Structure
- calculator_cpp_python/ 
- ├── main.py # Python user interface & logic 
- ├── calc.cpp # C++ source code for arithmetic operations 
- ├── build.sh # Shell script to compile C++ into a shared library 
- ├── calc.so # Compiled C++ shared object (auto-generated)


---

## 🛠 Features

- Addition, Subtraction, Multiplication, Division,Modulo,Square
- Uses C++ for faster, lower-level computation
- Demonstrates Python ↔ C++ inter-language communication using `ctypes`
- Cross-platform compatible (Linux/macOS; WSL for Windows)

---

## 🚀 How to Run

## ✅ Option 1: Run on Replit (Recommended for Beginners)

1. Go to [https://replit.com](https://replit.com) and create a new **Python Repl**.
2. Add the following files to your Replit:
   - `main.py`
   - `calc.cpp`
   - `build.sh`
3. Open the **Shell tab** in Replit.
4. Run the following commands:
   ```bash
   chmod +x build.sh
   ./build.sh
   python3 main.py

## ✅ Option 2: Run Locally on Your Computer
📌 Requirements:
- Python 3.x
- g++ compiler
- Unix-like system (Linux, macOS, or WSL for Windows)
 1) 📥 Steps: 
Clone or download this repository:
```bash
git clone https://github.com/attaullahwazir/calculator_cpp_python.git
cd calculator_cpp_python 
```
 2) 📥 Steps:
 Make the build script executable and compile:
```bash
chmod +x build.sh
./build.sh
```
 3) 📥 Steps: 
Run the calculator:
```bash
python3 main.py
```
## 🧠 Technical Overview
- calc.cpp: Defines basic arithmetic functions and exposes them using extern "C" for C-compatible linkage.
- build.sh: Compiles the C++ code into a shared object (.so) using g++.
- main.py: Loads the shared object using ctypes, handles user input, and calls C++ functions.

## 🔗 Example
```txt
==== C++ + Python Calculator ====
Enter first number: 10
Enter second number: 5
Choose operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Your choice: 3
Result: 50
```

## 📚 Concepts Covered
- Calling C++ from Python using ctypes
- Shared library creation (.so)
- Cross-language integration for performance and modularity

## 📄 License
This project is open-source and available under the MIT License.

## 👨‍💻 Author
Built with 💻 by Attaullah Wazir — feel free to contribute or fork this project!




