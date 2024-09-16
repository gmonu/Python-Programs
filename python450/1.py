# print("Enter size of list")
# size = int(input())
# inputlist = []
# for i in range(0, size):
#     ele = input()
#     inputlist.append(ele)
# for i in reversed(inputlist):
#     print(i)

name = input("Enter any string")



for i in reversed(range(len(name))):
    print(name[i], end='')