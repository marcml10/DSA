def consecutive(str: list[int]) -> list[int]:
    hashed = set(str)
    numbers = []

    for elements in str:
        if elements -1 not in hashed:
            currentnum = elements 
            longest = []

            while currentnum in hashed:
                longest.append(currentnum)
                currentnum+=1

            if len(longest) > len(numbers):
                numbers = longest
            
    return numbers

obtain = consecutive([200, 3,5,2,4 , 202, 203])
print(obtain)



# possible issues unable to store the largest sequence 