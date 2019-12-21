from itertools import permutations
import sys

def parseInstr(instr: str):
    '''Returns opcode, mode1, mode2, mode3
    '''
    instr = f"{instr:05}"
    return instr[3:], instr[2], instr[1], instr[0]


def diagonise(instr: list, phase: int, input: int):
    res = 0
    i = 0
    input_count = 0
    while instr[i] != 99:
        opcode, mode1, mode2, mode3 = parseInstr(instr[i])

        if opcode == "03":
            if input_count == 0:
                instr[instr[i+1]] = phase
                input_count += 1
            else:
                instr[instr[i+1]] = input
            i += 2
        elif opcode == "04":
            res = instr[instr[i+1]]
            i += 2
        else:
            index1 = instr[i+1] if mode1 == "0" else i+1
            index2 = instr[i+2] if mode2 == "0" else i+2
            index3 = instr[i+3] if mode3 == "0" else i+3

            if opcode == "01":
                instr[index3] = instr[index1] + instr[index2]
                i += 4 
            elif opcode == "02":
                instr[index3] = instr[index1] * instr[index2]
                i += 4
            elif opcode == "05":
                if instr[index1]:
                    i = instr[index2]
                else:
                    i += 3
            elif opcode == "06":
                if not instr[index1]:
                    i = instr[index2]
                else:
                    i += 3
            elif opcode == "07":
                instr[index3] = 1 if instr[index1] < instr[index2] else 0
                i += 4
            elif opcode == "08":
                instr[index3] = 1 if instr[index1] == instr[index2] else 0
                i += 4

    return res

if __name__ == "__main__":
    instr = ""
    with open("input.txt", "r") as fp:
        instr = fp.read()
    instr = list(map(int, instr.split(",")))
    perm = [p for p in permutations([0, 1, 2, 3, 4], 5)]
    
    curr_max = sys.maxsize*-1
    best_combo = None
    for i in range(len(perm)):
        res = 0
        for x in perm[i]:
            res = diagonise(instr, x, res)
        print(res, curr_max)
        if res > curr_max:
            curr_max = res
            best_combo = perm[i]
            print(best_combo)
    print(curr_max, best_combo)