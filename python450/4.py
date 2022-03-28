import time
import random
size = random.randint(1, 10000)
nums = []
for i in range(size):
    temp = random.randint(0, 2)
    nums.append(temp)
print(nums)

start_time = time.time()
temp1 = sorted(nums)
print(temp1)
print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
sorted_list = []
for i in range(len(nums)):
    if nums[i] == 0:
        sorted_list.append(nums[i])
for i in range(len(nums)):
    if nums[i] == 1:
        sorted_list.append(nums[i])
for i in range(len(nums)):
    if nums[i] == 2:
        sorted_list.append(nums[i])
print(sorted_list)
print("end")
print("--- %s seconds ---" % (time.time() - start_time))