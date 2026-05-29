liste = [1, 2, 3, 4, 5]
for i in range(len(liste)//2):
  liste[i], liste[-i-1]=  liste[-i-1] , liste[i]
  print(liste)