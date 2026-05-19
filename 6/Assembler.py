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
    bin_codes = []

    while(p.hasMoreLines()):
        if p.instructionType() == InstructionType.L_INSTRUCTION:
            symbol = p.symbol()
            if not st.contains(symbol):
                st.addEntry(symbol, str(p.get_current_line_number()))
        p.advance()

    p.reset_index_and_current_line_number()

    ram_addr_for_variable = 16
    while(p.hasMoreLines()):
        ins_type = p.instructionType()
        if ins_type == InstructionType.L_INSTRUCTION:
            pass
        elif ins_type == InstructionType.A_INSTRUCTION:
            symbol = p.symbol()
            if not symbol.isdigit():
                if not st.contains(symbol):
                    st.addEntry(symbol, ram_addr_for_variable)
                    addr_bin = str(bin(int(ram_addr_for_variable)))[2:]
                    addr_bin_padding = "".join(["0" for _ in range(16-len(addr_bin))])
                    addr_bin_16 = addr_bin_padding + addr_bin
                    bin_codes.append(addr_bin_16)
                    ram_addr_for_variable += 1
                else:
                    addr = st.getAddress(symbol)
                    addr_bin = str(bin(int(addr)))[2:]
                    addr_bin_padding = "".join(["0" for _ in range(16-len(addr_bin))])
                    addr_bin_16 = addr_bin_padding + addr_bin
                    bin_codes.append(addr_bin_16)
            else:
                numeric_bin = str(bin(int(symbol)))[2:]
                numeric_bin_padding = "".join(["0" for _ in range(16-len(numeric_bin))])
                numeric_bin_16 = numeric_bin_padding + numeric_bin
                bin_codes.append(numeric_bin_16)
        else:
            comp = c.comp(p.comp())
            dest = c.dest(p.dest())
            jump = c.jump(p.jump())
            if(comp and dest and jump):
                c_bin_16 = "111" + comp + dest + jump
                bin_codes.append(c_bin_16)
        p.advance()

    full_bin_code = "\n".join(bin_codes)
    
    out_file_path = filepath.split(".")[0] + ".hack"
    with open(out_file_path, 'w', encoding='utf-8') as f:
        f.write(full_bin_code)