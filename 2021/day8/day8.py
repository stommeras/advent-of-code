### Part One

with open("day8-input.txt") as f:
    input = f.read().splitlines()

count = 0

for line in input:
    signals, outputs = line.split(" | ")    # split signals and outputs
    outputs = outputs.split()               # split outputs to seperate elements

    for o in outputs:
        if len(o) in (2, 3, 4, 7):          # check if output is of a unique length
            count += 1

print("---Part One---")
print(f"Digits 1, 4, 7, or 8 appear {count} times.")


### Part Two


sum = 0

for line in input:
    signals, outputs = line.split(" | ")                # split signals and outputs
    l = {len(s): set(s) for s in signals.split()}       # number of segments
    
    n = ""
    for o in map(set, outputs.split()):                 # loop over output digits
        match len(o), len(o&l[4]), len(o&l[2]):         # mask with known digits
            case 2,_,_: n += "1"
            case 3,_,_: n += "7"
            case 4,_,_: n += "4"
            case 7,_,_: n += "8"
            case 5,2,_: n += "2"
            case 5,3,1: n += "5"
            case 5,3,2: n += "3"
            case 6,4,_: n += "9"
            case 6,3,1: n += "6"
            case 6,3,2: n += "0"
    sum += int(n)

print("\n---Part Two---")
print("Sum of all displays:", sum)