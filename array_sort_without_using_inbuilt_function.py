import random
size = random.randint(10,50)
unsorted_list = []
unsorted_list = [random.randint(-100, 100) for _ in range(size)]
print(f"Unsorted array --> {unsorted_list}")
n = len(unsorted_list)
for i in range(n):
    for j in range(0, n-i-1):
        if unsorted_list[j] > unsorted_list[j+1]:
            unsorted_list[j+1], unsorted_list[j] = unsorted_list[j], unsorted_list[j+1]
print(f"sorted list --> {unsorted_list}")


print(f"Unsorted array --> {unsorted_list}")
sorted_list = sorted(unsorted_list)
print(f"Sorted list --> {sorted_list}")
