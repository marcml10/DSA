def anagram(s:str, t:str) ->bool:
    if len(s)!=len(t):
        return False

    counting={}
    for char in s:
        counting[char]=counting.get(char, 0) + 1
    
    for char in t:
        if char not in counting or counting[char]==0:
            return False
        counting[char]-=1
    return True

checking = anagram("working", "bathing")
print("anagram" if anagram("working", "bathing") else "aint anagram")