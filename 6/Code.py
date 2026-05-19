COMP_BIN_CODES = {
    "0" : "0101010",
    "1" : "0111111",
    "-1" : "0111010",
    "D" : "0001100",
    "A": "0110000",
    "M" : "1110000",
    "!D": "0001101",
    "!A" : "0110001",
    "-M" : "1110011",
    "D+1" : "0011111",
    "A+1" : "0110111",
    "M+1" : "1110111",
    "D-1" : "0001110",
    "A-1" : "0110010",
    "M-1" : "1110010",
    "D+A" : "0000010",
    "D+M" : "1000010",
    "D-A" : "0010011",
    "D-M" : "1010011",
    "A-D" : "0000111",
    "M-D" : "1000111",
    "D&A" : "0000000",
    "D&M" : "1000000",
    "D|A" : "0010101",
    "D|M" : "1010101"
}

DEST_BIN_CODES = {
    "null" : "000",
    "M" : "001",
    "D" : "010",
    "DM" : "011",
    "A" : "100",
    "AM" : "101",
    "AD" : "110",
    "ADM" : "111"
}

JUMP_BIN_CODES = {
    "null" : "000",
    "JGT" : "001",
    "JEQ" : "010",
    "JGE" : "011",
    "JLT" : "100",
    "JNE" : "101",
    "JLE" : "110",
    "JMP" : "111",
}

class Code:
    def dest(self, d):
        if not d=="null":
            sorted_num = sorted([ord(a) for a in d])
            sorted_d = [chr(d_item) for d_item in sorted_num]
            d = "".join(sorted_d)
        if d in DEST_BIN_CODES:
            return DEST_BIN_CODES[d]
        else:
            return None

    def comp(self, c):
        if c in COMP_BIN_CODES:
            return COMP_BIN_CODES[c]
        else:
            return None

    def jump(self, j):
        if j in JUMP_BIN_CODES:
            return JUMP_BIN_CODES[j]
        else:
            return None