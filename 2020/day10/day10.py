with open("day10-input.txt") as f:
    input = f.read().strip().splitlines()

joltages = [int(x) for x in input]

joltages.append(0)                  # outlet
joltages.append(max(joltages) + 3)  # my device
joltages.sort()

n1 = 0
n3 = 0

# check for each adapter if the difference to the next is 1 or 3
for i in range(len(joltages) - 1):
    diff = joltages[i + 1] - joltages[i]
    if diff == 1:
        n1 += 1
    elif diff == 3:
        n3 += 1

print("---Part One---")
print("Number of each differences multiplied:", n1 * n3)


### Part Two

# dynamic programming
DP = {}

# dp(i) = the number of ways to complete the adapter chain given
#         that you are currently at adapter joltages[i]
def dp(i):
    if i == len(joltages) - 1:
        return 1
    if i in DP:
        return DP[i]

    ans = 0
    
    for j in range(i+1, len(joltages)):
        if joltages[j] - joltages[i] <= 3:
            # one way to get from i to the end is to first step to j
            # the number of paths from i that *start* by stepping to joltages[j] is just DP[j]
            # So dp(i) = \sum_{valid j} dp(j)
            ans += dp(j)
    DP[i] = ans
    return ans

print("\n---Part Two---")
print("Total number of distinct ways you can arrange the adapters:", dp(0))