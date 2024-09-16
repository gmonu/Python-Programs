import time
import random
size = random.randint(1, 100)
nums = []
for i in range(size):
    temp = random.randint(-100,100)
    nums.append(temp)

print(nums)
j = 0
for i in range(len(nums)):
    if nums[i] < 0:
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t
        j += 1
print(nums)