what = [1, 2, 4, 5, 6]
summing=0
overall=((len(what)+1)*((len(what)+1)+1))//2
for an in what:
    summing=summing+an
print(overall - summing)