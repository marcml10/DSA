nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
highest=nums[0]
c_highest=nums[0]
"basically what i have to do is:"
"   checking line by line"
"   i can only throw from behind"
"   In each step the highest should keep changing"
for i in range(1,len(nums)):
    highest += nums[i]
    if highest > c_highest:
        c_highest = highest
    elif highest < 0:
        highest=0
print(c_highest)

