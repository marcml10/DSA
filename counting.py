elements=['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
countingem={}
for ele in elements:
    if ele not in countingem:
        countingem[ele]=1
    else:
        countingem[ele] +=1
print(countingem)