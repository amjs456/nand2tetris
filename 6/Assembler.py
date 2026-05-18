from Parser import Parser, InstructionType
from Code import Code
from SymbolTable import SymbolTalbe

import sys, os

if __name__ == "__main__":
    filename = sys.argv[1]
    cwd = os.getcwd()
    filepath = os.path.join(cwd, filename)
    p = Parser(filepath=filepath)
    c = Code()
    st = SymbolTalbe()

    while(p.hasMoreLines()):
        if p.instructionType() == InstructionType.L_INSTRUCTION:
            symbol = p.symbol()
            if not st.contains(symbol):
                st.addEntry(symbol, str(p.get_current_line_number() + 1))
        p.advance()

    p.reset_index_and_current_line_number()

    ram_addr_for_variable = 16
    while(p.hasMoreLines()):
        ins_type = p.instructionType()
        if ins_type == InstructionType.L_INSTRUCTION:
            symbol = p.symbol()
            if st.contains(symbol):
                symbol = st.getAddress(symbol)

            symbol_bin = str(bin(int(symbol)))[2:]
            symbol_bin_padding = "".join(["0" for _ in range(16-len(symbol_bin))])
            symbol_bin_16 = symbol_bin_padding + symbol_bin
        elif ins_type == InstructionType.A_INSTRUCTION:
            symbol = p.symbol()
            if not symbol.isdigit():
                if not st.contains(symbol):
                    st.addEntry(symbol, ram_addr_for_variable)
                    ram_addr_for_variable += 1
        else:
            comp = c.comp(p.comp())
            dest = c.dest(p.dest())
            jump = c.jump(p.jump())
        p.advance()