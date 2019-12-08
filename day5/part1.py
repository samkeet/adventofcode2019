
'''
Opcodes
1: add
2: mul
3: read
4: write
99: exit

Parameter mode:
0: addr
1: value

IP Increments:
2: read, write
4: add, mul
'''

def parseInstr(instr: str):
    '''Returns opcode, mode1, mode2, mode3
    '''
    instr = f"{instr:05}"
    return instr[3:], instr[2], instr[1], instr[0]


def diagonise(instr: list):
    i = 0
    while instr[i] != 99:
        opcode, mode1, mode2, mode3 = parseInstr(instr[i])

        if opcode == "03":
            # only read operation takes input as 1
            instr[instr[i+1]] = 1
            i += 2
        elif opcode == "04":
            print(instr[instr[i+1]])
            i += 2
        else:

            index1 = instr[i+1] if mode1 == "0" else i+1
            index2 = instr[i+2] if mode2 == "0" else i+2
            index3 = instr[i+3] if mode3 == "0" else i+3

            res = 0
            if opcode == "01":
                res = instr[index1] + instr[index2]
            elif opcode == "02":
                res = instr[index1] * instr[index2]

            instr[index3] = res
            i += 4 

if __name__ == "__main__":
    instr = ""
    with open("input1.txt", "r") as fp:
        instr = fp.read()
    diagonise(list(map(int, instr.split(","))))
