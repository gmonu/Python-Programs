import random
size = random.randint(1, 100)
nums1 = []
nums2 = []
for i in range(size):
    temp = random.randint(1, 100)
    temp1 = random.randint(1, 100)
    nums1.append(temp)
    nums2.append(temp1)
print(nums1)
print(nums2)
unionnums = []
for i in nums1:
    if i in unionnums:
        pass
    else:
        unionnums.append(i)
for j in nums2:
    if j in unionnums:
        pass
    else:
        unionnums.append(j)
print("Union")
print(unionnums)

print("intersect")
intersectnums = []
z = 0
for i in range(len(nums1)):
    if nums1[i] in nums2:
        pass
    else:
        intersectnums.append(nums1[i])

    if nums2[i] in nums1:
        pass
    else:
        intersectnums.append(nums2[i])


print(intersectnums)


