with open("day14-example.txt") as f:
    input = f.read().strip()

start, instr = input.split("\n\n")

rules = {}

for pair, a in instr.split("->"):
    rules[pair] = a

print(rules)

def next_step(str):
    new_str = ""
    
