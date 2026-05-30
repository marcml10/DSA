numbers = [2, 7, 11, 15]
target=9
count=0
left=0
right=len(numbers)-1
while left < right:
    if numbers[left] + numbers[right] < target:
        left+=1
    elif numbers[left] + numbers[right] > target:
        right-=1
    elif numbers[left] + numbers[right] == target:
        print(left, right)
        break
