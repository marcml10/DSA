words = "nurses run"
change= words.replace(" ", "")
palindrome=""
for i in range(len(change)-1,-1,-1):
    palindrome+=change[i]
if palindrome==change:
    print("True")