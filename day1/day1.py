input = open("day1-input.txt")
nums = input.readlines()

sum = 0

# check for each element of nums if it's bigger than the previous element
for i in range(1, len(nums)):
    if (nums[i] > nums[i - 1]):
        sum += 1

print(sum)
# 1687