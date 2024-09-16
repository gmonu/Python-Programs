import random
size = random.randint(1, 10)
nums = []
for i in range(size):
    temp = random.randint(1, 100)
    nums.append(temp)

print(nums)

print('left cyclic rotate')
j = 0
for i in range(len(nums)):
    temp = nums[i]

