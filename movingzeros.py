zeros = [0, 1, 0, 3, 12]
track=0
for i in range(len(zeros)):
  if zeros[i]!=0:
    zeros[track], zeros[i] = zeros[i], zeros[track]
    track+=1
    print(zeros)
