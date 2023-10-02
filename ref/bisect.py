arr = [1, 2, 3, 4, 10]
target = 1.5

# 1
left = 0
right = len(arr)-1
while left < right:
    mid = (left + right)//2
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid
        
print('#1')
print(arr)
print(left, right, '\n')

# 2
left = 0
right = len(arr)-1
while left <= right:
    mid = (left + right)//2
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
print('#2')
print(arr)
print(left, right, '\n')

# 3

arr = [1, 2, 3, 4, 10]
target = 2.5

left = 0
right = len(arr)-1
while left < right:
    mid = (left + right)//2
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1


print('#3')
print(arr)
print(left, right, '\n')



left = 0
right = len(arr)-1
while left + 1 < right:
    mid = (left + right)//2
    if arr[mid] < target:
        left = mid
    else:
        right = mid


print('#4')
print(arr)
print(left, right, '\n')