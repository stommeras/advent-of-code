### Part One

with open("day8-input.txt") as f:
    input = f.read().splitlines()

accumulator = 0
visited = set()

# recursively call next instruction (would be easier with while True)
def next_instruction(index):
    if index in visited:
        return None
    else:
        visited.add(index)
    
    instr = input[index].split()
    op = instr[0]
    arg = int(instr[1])

    if op == "nop":
        next_instruction(index + 1)
    elif op == "acc":
        global accumulator
        accumulator += arg
        next_instruction(index + 1)
    elif op == "jmp":
        next_instruction(index + arg)

next_instruction(0)

print("---Part One---")
print(f"Accumulator value: {accumulator}")


### Part Two

# tried a given set of instructions until it loops or terminates
def try_program(prog):
    acc = 0
    index = 0
    visited = set()

    while True:
        if index in visited:
            return None
        elif index == len(prog):
            return acc
        
        visited.add(index)

        instr = prog[index]

        op, arg = instr.split()
        arg = int(arg)
    
        if op == "jmp":
            index += arg
            continue
        elif op == "acc":
            acc += arg
        elif op == "nop":
            pass

        index += 1

print("\n---Part Two---")

# calls try_program with a changed jmp or nop instruction, until it terminates
for i in range(len(input)):
    prog = input[:]
    if prog[i].startswith("jmp"):
        prog[i] = prog[i].replace("jmp", "nop")
    elif prog[i].startswith("nop"):
        prog[i] = prog[i].replace("nop", "jmp")
    x = try_program(prog)
    if x:
        print(f"Accumulator value: {x}")
        break
