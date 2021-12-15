from collections import Counter

with open("day14-input.txt") as f:
    input = f.read().strip()

tpl, _, *rules = input.split("\n")
rules = dict(r.split(" -> ") for r in rules)

pairs = Counter(map(str.__add__, tpl, tpl[1:]))
chars = Counter(tpl)

for _ in range(40):
    for (a, b), c in pairs.copy().items():
        x = rules[a + b]
        pairs[a + b] -= c
        pairs[a + x] += c
        pairs[x + b] += c
        chars[x] += c

print(max(chars.values()) - min(chars.values()))