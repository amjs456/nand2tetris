from enum import Enum, auto

class InstructionType(Enum):
    A_INSTRUCTION = auto()
    C_INSTRUCTION = auto()
    L_INSTRUCTION = auto()


class Parser:
    def __init__(self, filepath):

        with open(filepath, encoding='utf-8') as f:
            text = f.read()
        self.lines = text.split('\n')
        for i, line in enumerate(self.lines):
            self.lines[i] = line.replace(" ", "")
        self.index = 0
        self.current_line_number = 0


    def hasMoreLines(self):
        return len(self.lines) - 1 > self.index

    def advance(self):
        if self.hasMoreLines():
            self.index += 1

        while(self.hasMoreLines() and (self.lines[self.index].startswith("//") or self.lines[self.index]=="")):
            self.index += 1

        if self.instructionType() in [InstructionType.A_INSTRUCTION, InstructionType.C_INSTRUCTION]:
            self.current_line_number += 1

            

    def instructionType(self):
        if self.lines[self.index].startswith("@"):
            return InstructionType.A_INSTRUCTION
        elif self.lines[self.index].startswith("(") and self.lines[self.index].endswith(")"):
            return InstructionType.L_INSTRUCTION
        else:
            return InstructionType.C_INSTRUCTION

    def symbol(self):
        if(self.instructionType()==InstructionType.A_INSTRUCTION):
            line = self.lines[self.index].replace("@", "")
            return line
        elif(self.instructionType()== InstructionType.L_INSTRUCTION):
            line = self.lines[self.index].replace("(", "").replace(")", "")
            return line
        else:
            return None

    def dest(self):
        if(self.instructionType()==InstructionType.C_INSTRUCTION):
            if "=" in self.lines[self.index]:
                d = self.lines[self.index].split("=")[0]
                return d
            else:
                return "null"
        else:
            return None

    def comp(self):
        if(self.instructionType()==InstructionType.C_INSTRUCTION):
            if "=" in self.lines[self.index]:
                c = self.lines[self.index].split("=")[1]
                return c
            elif ";" in self.lines[self.index]:
                c = self.lines[self.index].split(";")[0]
                return c
            if(self.lines[self.index]=="MD=M+1"):
                print(c)
        else:
            return None

    def jump(self):
        if(self.instructionType()==InstructionType.C_INSTRUCTION):
            if ";" in self.lines[self.index]:
                j = self.lines[self.index].split(";")[1]
                return j
            else:
                return "null"
        else:
            return None
        
    def reset_index_and_current_line_number(self):
        self.index = 0
        self.current_line_number = 0


    def get_current_line_number(self):
        return self.current_line_number