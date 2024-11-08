# 🖥️ Simple CPU Simulator

A Python-based simulation of a simple CPU with basic instructions like `ADD`, `SUB`, `LOAD`, `STORE`, and `MOV`. This program demonstrates the process of fetching, decoding, and executing instructions, providing a step-by-step output of each cycle.

## 📋 Table of Contents
- [🖥️ Simple CPU Simulator](#️-simple-cpu-simulator)
  - [📋 Table of Contents](#-table-of-contents)
  - [📝 About](#-about)
  - [✨ Features](#-features)
  - [🚀 How to Run](#-how-to-run)
    - [Prerequisites](#prerequisites)
    - [Running the Project](#running-the-project)
  - [🖱️ Instructions](#️-instructions)
  - [📂 Project Structure](#-project-structure)
  - [🔍 Example Output](#-example-output)
  - [🛠️ Technologies Used](#️-technologies-used)
  - [🤝 Contributions](#-contributions)
    - [How to Contribute](#how-to-contribute)
  - [📄 License](#-license)
  - [🙌 Acknowledgements](#-acknowledgements)

## 📝 About
This project simulates a simple CPU using Python. The CPU has:
- **8 general-purpose registers** (`R0` to `R7`).
- **256 memory addresses**.
- A set of basic instructions (`ADD`, `SUB`, `LOAD`, `STORE`, and `MOV`).
- A step-by-step simulation that shows the fetch, decode, and execute cycles for each instruction.

## ✨ Features
- **Simulates basic CPU operations**: Fetch, decode, and execute cycles.
- **Supports arithmetic and memory operations**.
- Provides detailed output for each cycle to help understand how a CPU works.
- Easy to extend with additional instructions if needed.

## 🚀 How to Run

### Prerequisites
Ensure you have Python installed on your system:
```bash
python3 --version
```

### Running the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/JoAnCaRo/CPU_Simulator.git
   cd CPU_Simulator
   ```
2. Run the program:
   ```bash
   python3 CPU_Simulator.py
   ```

## 🖱️ Instructions
Here’s a list of supported instructions:
- **ADD R1 R2 R3**: Adds the values in `R2` and `R3`, storing the result in `R1`.
- **SUB R1 R2 R3**: Subtracts the value in `R3` from `R2`, storing the result in `R1`.
- **LOAD R1 X**: Loads the value at memory address `X` into register `R1`.
- **STORE R1 X**: Stores the value in register `R1` into memory address `X`.
- **MOV R1 R2**: Copies the value from register `R2` to register `R1`.

## 📂 Project Structure
```
CPU_Simulator/
│
├── CPU_Simulator.py   # Main Python script
└── README.md          # Project documentation
```

## 🔍 Example Output
After running the program with the given set of instructions, you might see an output similar to:
```
Cycle 0: FETCH instruction 'LOAD R1 10' at PC = 0
Cycle 1: DECODE opcode 'LOAD' with operands ['R1', '10']
Cycle 2: EXECUTE LOAD R1 = MEM[10]
Cycle 3: FETCH instruction 'LOAD R2 11' at PC = 1
Cycle 4: DECODE opcode 'LOAD' with operands ['R2', '11']
Cycle 5: EXECUTE LOAD R2 = MEM[11]
Cycle 6: FETCH instruction 'ADD R3 R1 R2' at PC = 2
Cycle 7: DECODE opcode 'ADD' with operands ['R3', 'R1', 'R2']
Cycle 8: EXECUTE ADD R3 = R1 + R2
Cycle 9: FETCH instruction 'STORE R3 12' at PC = 3
Cycle 10: DECODE opcode 'STORE' with operands ['R3', '12']
Cycle 11: EXECUTE STORE MEM[12] = R3
Cycle 12: FETCH instruction 'MOV R4 R3' at PC = 4
Cycle 13: DECODE opcode 'MOV' with operands ['R4', 'R3']
Cycle 14: EXECUTE MOV R4 = R3
Registers: [0, value_from_mem[10], value_from_mem[11], sum, sum, 0, 0, 0]
Memory: [0, 0, ..., sum_at_mem[12], ...]
```

## 🛠️ Technologies Used
- Python 3.x

## 🤝 Contributions
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository, make changes, and submit a pull request.

### How to Contribute
1. Fork the project.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and commit:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## 📄 License
This project is open-source and available under the MIT License.

## 🙌 Acknowledgements
Special thanks to everyone who has supported this project!

Happy coding! 🚀
