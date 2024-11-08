class SimpleCPU:
    def __init__(self):
        # Initialize the CPU with:
        self.registers = [0] * 8  # 8 general-purpose registers (R0 to R7)
        self.memory = [0] * 256  # Memory with 256 addresses
        self.pc = 0  # Program counter (points to the current instruction)
        self.instructions = []  # List to store loaded instructions
        self.cycle = 0  # Cycle counter to track execution time

    def load_instructions(self, instructions):
        """Load a list of instructions into the CPU."""
        self.instructions = instructions

    def run(self):
        """Run the loaded instructions in the CPU."""
        # Continue running as long as there are instructions to execute
        while self.pc < len(self.instructions):
            # Fetch the current instruction
            instruction = self.fetch()
            # Decode the fetched instruction into opcode and operands
            opcode, operands = self.decode(instruction)
            # Execute the decoded instruction
            self.execute(opcode, operands)

    def fetch(self):
        """Fetch the current instruction based on the program counter."""
        instruction = self.instructions[self.pc]  # Get the instruction at the current program counter
        print(f"Cycle {self.cycle}: FETCH instruction '{instruction}' at PC = {self.pc}")
        self.pc += 1  # Move to the next instruction
        self.cycle += 1  # Increment the cycle count
        return instruction  # Return the fetched instruction

    def decode(self, instruction):
        """Decode the fetched instruction into opcode and operands."""
        parts = instruction.split()  # Split the instruction into parts
        opcode = parts[0]  # The first part is the opcode (operation)
        operands = parts[1:]  # The remaining parts are the operands
        print(f"Cycle {self.cycle}: DECODE opcode '{opcode}' with operands {operands}")
        self.cycle += 1  # Increment the cycle count
        return opcode, operands  # Return the opcode and operands

    def execute(self, opcode, operands):
        """Execute the instruction based on its opcode."""
        if opcode == "ADD":
            # ADD operation: R1 = R2 + R3
            reg1 = int(operands[0][1])
            reg2 = int(operands[1][1])
            reg3 = int(operands[2][1])
            self.registers[reg1] = self.registers[reg2] + self.registers[reg3]
            print(f"Cycle {self.cycle}: EXECUTE ADD R{reg1} = R{reg2} + R{reg3}")

        elif opcode == "SUB":
            # SUB operation: R1 = R2 - R3
            reg1 = int(operands[0][1])
            reg2 = int(operands[1][1])
            reg3 = int(operands[2][1])
            self.registers[reg1] = self.registers[reg2] - self.registers[reg3]
            print(f"Cycle {self.cycle}: EXECUTE SUB R{reg1} = R{reg2} - R{reg3}")

        elif opcode == "LOAD":
            # LOAD operation: Load value from memory into register
            reg = int(operands[0][1])
            mem_addr = int(operands[1])
            self.registers[reg] = self.memory[mem_addr]
            print(f"Cycle {self.cycle}: EXECUTE LOAD R{reg} = MEM[{mem_addr}]")

        elif opcode == "STORE":
            # STORE operation: Store value from register into memory
            reg = int(operands[0][1])
            mem_addr = int(operands[1])
            self.memory[mem_addr] = self.registers[reg]
            print(f"Cycle {self.cycle}: EXECUTE STORE MEM[{mem_addr}] = R{reg}")

        elif opcode == "MOV":
            # MOV operation: Copy value from one register to another
            reg1 = int(operands[0][1])
            reg2 = int(operands[1][1])
            self.registers[reg1] = self.registers[reg2]
            print(f"Cycle {self.cycle}: EXECUTE MOV R{reg1} = R{reg2}")

        else:
            # Handle unknown instructions
            print(f"Cycle {self.cycle}: EXECUTE Unknown instruction '{opcode}'")

        # Increment the cycle count after execution
        self.cycle += 1

    def display_registers(self):
        """Display the current state of the registers."""
        print("Registers:", self.registers)

    def display_memory(self):
        """Display the current state of the memory."""
        print("Memory:", self.memory)


# Example usage of the SimpleCPU class
cpu = SimpleCPU()

# Load a set of instructions to simulate
instructions = [
    "LOAD R1 10",  # Load value from memory[10] into register R1
    "LOAD R2 11",  # Load value from memory[11] into register R2
    "ADD R3 R1 R2",  # Add values in R1 and R2, store the result in R3
    "STORE R3 12",  # Store the value in R3 into memory[12]
    "MOV R4 R3",  # Copy the value from R3 to R4
]

# Load the instructions into the CPU
cpu.load_instructions(instructions)

# Run the CPU to execute the instructions
cpu.run()

# Display the current state of the registers and memory after execution
cpu.display_registers()
cpu.display_memory()
