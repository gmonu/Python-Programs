a = list(input("Enter some numbers"))
min = -123455322
max = 123455322

# using sort()
# a.sort()
# print(a[0], a[len(a)-1])

# without using sort()
for i in a:
    i = int(i)
    if i > min:
        min = i
for j in a:
    j = int(j)
    if j < max:
        max = j

print("maximum: ", min, "minimum: ", max)
