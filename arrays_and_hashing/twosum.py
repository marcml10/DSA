def twosum (nums: list[int], target: int) -> list:
    matching={}

    for i, num in enumerate(nums):
        required = target - num
        position = matching.get(required, -1) 
        if position != -1:
            final = [i,position]
            print(final) 
        matching[num]= i

twosum([2, 7, 11, 15], 9)
