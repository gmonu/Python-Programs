import time
import random
nums = []
size = random.randint(1, 10**4)
for i in range(size):
    x = random.randint(-10**9, 10**9)
    nums.append(x)

k = random.randint(1, size)
print(len(nums))
print(k)

min = nums[0]

start_time = time.time()
temp = sorted(nums)
print("kth element:", temp[k-1])
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(0, len(nums)):
    count = 1
    for j in range(0, len(nums)):
        if nums[i] > nums[j]:
            count += 1
    if count == k:
        min = nums[i]
        break

print("kth element :", min)
print("--- %s seconds ---" % (time.time() - start_time))