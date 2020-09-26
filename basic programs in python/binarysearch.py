import  random
lis = [1, 2, 10, 54, 100, 121, 145, 165]
n = len(lis)
# print(lis[0])
req = 1
low = 0
high = n-1
mid = 0
while low <= high:
    mid = int((low + high) / 2)
    if req == lis[mid]:
        print("ele found {}".format(lis[mid]))
        break
    elif lis[mid] < req:
        low = mid + 1
    else:
        high = mid - 1
    print(low, mid, high)


x = [random.random() for i in range(5)]
print(x)
