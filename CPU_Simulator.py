class SimpleCPU:
    def __init__(self):
        self.registers = [0] * 8  # 8 general-purpose registers
        self.memory = [0] * 256  # Memory with 256 addresses
        self.pc = 0  # Program counter
        self.instructions = []
        self.cycle = 0

    def load_instructions(self, instructions):
        """Load a list of instructions into the CPU."""
        self.instructions = instructions

    def run(self):
        """Run the loaded instructions."""
        while self.pc < len(self.instructions):
            instruction = self.fetch()
            opcode, operands = self.decode(instruction)
            self.execute(opcode, operands)

    def fetch(self):
        """Fetch the instruction from memory."""
        instruction = self.instructions[self.pc]
        print(f"Cycle {self.cycle}: FETCH instruction '{instruction}' at PC = {self.pc}")
        self.pc += 1
        self.cycle += 1
        return instruction

    def decode(self, instruction):
        """Decode the fetched instruction."""
        parts = instruction.split()
        opcode = parts[0]
        operands = parts[1:]
        print(f"Cycle {self.cycle}: DECODE opcode '{opcode}' with operands {operands}")
        self.cycle += 1
        return opcode, operands

    def execute(self, opcode, operands):
        """Execute the instruction."""
        if opcode == "ADD":
            reg1 = int(operands[0][1])
            reg2 = int(operands[1][1])
            reg3 = int(operands[2][1])
            self.registers[reg1] = self.registers[reg2] + self.registers[reg3]
            print(f"Cycle {self.cycle}: EXECUTE ADD R{reg1} = R{reg2} + R{reg3}")
        elif opcode == "SUB":
            reg1 = int(operands[0][1])
            reg2 = int(operands[1][1])
            reg3 = int(operands[2][1])
            self.registers[reg1] = self.registers[reg2] - self.registers[reg3]
            print(f"Cycle {self.cycle}: EXECUTE SUB R{reg1} = R{reg2} - R{reg3}")
        elif opcode == "LOAD":
            reg = int(operands[0][1])
            mem_addr = int(operands[1])
            self.registers[reg] = self.memory[mem_addr]
            print(f"Cycle {self.cycle}: EXECUTE LOAD R{reg} = MEM[{mem_addr}]")
        elif opcode == "STORE":
            reg = int(operands[0][1])
            mem_addr = int(operands[1])
            self.memory[mem_addr] = self.registers[reg]
            print(f"Cycle {self.cycle}: EXECUTE STORE MEM[{mem_addr}] = R{reg}")
        elif opcode == "MOV":
            reg1 = int(operands[0][1])
            reg2 = int(operands[1][1])
            self.registers[reg1] = self.registers[reg2]
            print(f"Cycle {self.cycle}: EXECUTE MOV R{reg1} = R{reg2}")
        else:
            print(f"Cycle {self.cycle}: EXECUTE Unknown instruction '{opcode}'")

        self.cycle += 1

    def display_registers(self):
        """Display the current state of the registers."""
        print("Registers:", self.registers)

    def display_memory(self):
        """Display the current state of the memory."""
        print("Memory:", self.memory)


# Example usage:
cpu = SimpleCPU()

# Load a simple set of instructions
instructions = [
    "LOAD R1 10",  # Load value from memory[10] into R1
    "LOAD R2 11",  # Load value from memory[11] into R2
    "ADD R3 R1 R2",  # Add R1 and R2, store result in R3
    "STORE R3 12",  # Store R3 into memory[12]
    "MOV R4 R3",  # Copy R3 to R4
]

cpu.load_instructions(instructions)
cpu.run()
cpu.display_registers()
cpu.display_memory()

